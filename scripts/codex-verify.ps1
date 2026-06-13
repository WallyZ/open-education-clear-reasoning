[CmdletBinding()]
param(
    [string]$RepoRoot = '.',
    [ValidateSet('32k', '64k', 'cloud')]
    [string]$ContextProfile = 'cloud',
    [ValidateSet('changed', 'full')]
    [string]$Mode = 'changed',
    [string]$BaseRef = '',
    [switch]$IncludeUntracked,
    [switch]$KeepArtifacts,
    [string]$PitfallSolution = '',
    [string]$PitfallSourcePath = '',
    [string]$PitfallCategory = '',
    [string[]]$PitfallTags = @(),
    [switch]$PromptForPitfallSolution,
    [switch]$DisablePitfallHook
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-RepoRootPath {
    param([string]$Start)

    $resolved = (Resolve-Path $Start).Path
    try {
        $top = git -C $resolved rev-parse --show-toplevel 2>$null
        if ($LASTEXITCODE -eq 0 -and $top) {
            return $top.Trim()
        }
    }
    catch {
    }

    return $resolved
}

function Format-CommandPart {
    param([string]$Value)

    if ($Value -match '[\s''"]') {
        return ("'{0}'" -f ($Value -replace "'", "''"))
    }

    return $Value
}

function Get-VerificationCommandText {
    param(
        [string]$ContextProfileValue,
        [string]$ModeValue,
        [string]$BaseRefValue,
        [bool]$IncludeUntrackedValue,
        [bool]$KeepArtifactsValue
    )

    $parts = @(
        'pwsh',
        '-NoProfile',
        '-ExecutionPolicy',
        'Bypass',
        '-File',
        '.\scripts\codex-verify.ps1',
        '-RepoRoot',
        '.',
        '-ContextProfile',
        $ContextProfileValue,
        '-Mode',
        $ModeValue
    )

    if (-not [string]::IsNullOrWhiteSpace($BaseRefValue)) {
        $parts += @('-BaseRef', $BaseRefValue)
    }
    if ($IncludeUntrackedValue) {
        $parts += '-IncludeUntracked'
    }
    if ($KeepArtifactsValue) {
        $parts += '-KeepArtifacts'
    }

    return (($parts | ForEach-Object { Format-CommandPart -Value ([string]$_) }) -join ' ')
}

function Get-LogTailText {
    param(
        [string]$Path,
        [int]$TailLines = 120,
        [int]$MaxChars = 12000
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        return ''
    }

    $text = ((Get-Content -LiteralPath $Path -Tail $TailLines -ErrorAction SilentlyContinue) -join "`n").Trim()
    if ($text.Length -gt $MaxChars) {
        return $text.Substring($text.Length - $MaxChars)
    }

    return $text
}

function Write-PendingPitfall {
    param(
        [string]$PendingRoot,
        [string]$RunId,
        [string]$Repo,
        [string]$CommandText,
        [string]$ModeValue,
        [string]$ContextProfileValue,
        [int]$FailureExitCode,
        [string]$FailureLogPath
    )

    New-Item -ItemType Directory -Force -Path $PendingRoot | Out-Null

    $pendingPath = Join-Path $PendingRoot ("{0}.json" -f $RunId)
    $latestPath = Join-Path $PendingRoot 'latest.json'
    $pending = [pscustomobject]@{
        schema_version = 1
        status = 'pending'
        id = $RunId
        created_at_utc = (Get-Date).ToUniversalTime().ToString('o')
        repo_root = $Repo
        command = $CommandText
        mode = $ModeValue
        context_profile = $ContextProfileValue
        exit_code = $FailureExitCode
        log_path = $FailureLogPath
        output_tail = (Get-LogTailText -Path $FailureLogPath)
    }

    $json = $pending | ConvertTo-Json -Depth 6
    Set-Content -LiteralPath $pendingPath -Encoding utf8 -Value $json
    Set-Content -LiteralPath $latestPath -Encoding utf8 -Value $json
    Write-Output ("codex-verify pending pitfall captured: {0}" -f $latestPath)
}

function Resolve-PendingPitfall {
    param(
        [string]$PendingRoot,
        [string]$Repo,
        [string]$CurrentCommandText,
        [string]$Solution,
        [string]$SourcePath,
        [string]$Category,
        [string[]]$Tags,
        [bool]$Prompt
    )

    $latestPath = Join-Path $PendingRoot 'latest.json'
    if (-not (Test-Path -LiteralPath $latestPath)) {
        return
    }

    $pending = Get-Content -LiteralPath $latestPath -Raw | ConvertFrom-Json
    $solutionText = $Solution

    if ([string]::IsNullOrWhiteSpace($solutionText) -and $Prompt) {
        Write-Output ("codex-verify found pending pitfall from failed run: {0}" -f $latestPath)
        $solutionText = Read-Host 'Solution to record in memory-bank/commonPitfalls.md (blank skips recording)'
    }

    if ([string]::IsNullOrWhiteSpace($solutionText)) {
        Write-Output ("codex-verify pending pitfall available: {0}" -f $latestPath)
        Write-Output "After the fix is known, rerun verification with -PitfallSolution '<short reusable fix>' or -PromptForPitfallSolution."
        return
    }

    $recordScript = Join-Path $Repo 'scripts/memory/record_pitfall.ps1'
    if (-not (Test-Path -LiteralPath $recordScript)) {
        Write-Output ("codex-verify could not record pending pitfall because recorder is missing: {0}" -f $recordScript)
        return
    }

    $errorText = [string]$pending.output_tail
    if ([string]::IsNullOrWhiteSpace($errorText)) {
        $errorText = "Prior verification failed with exit code $($pending.exit_code). Failed log: $($pending.log_path)."
    }
    else {
        $errorText = "Failure output tail:`n$errorText"
    }

    $context = "Verification failed in a prior run and now passes. Failed command: $($pending.command). Failed log: $($pending.log_path)."
    $recordArgs = @(
        '-NoProfile',
        '-ExecutionPolicy',
        'Bypass',
        '-File',
        $recordScript,
        '-RepoRoot',
        $Repo,
        '-ErrorText',
        $errorText,
        '-Solution',
        $solutionText,
        '-Context',
        $context,
        '-VerificationCommand',
        $CurrentCommandText
    )

    if (-not [string]::IsNullOrWhiteSpace($SourcePath)) {
        $recordArgs += @('-SourcePath', $SourcePath)
    }
    if (-not [string]::IsNullOrWhiteSpace($Category)) {
        $recordArgs += @('-Category', $Category)
    }
    if ($Tags -and $Tags.Count -gt 0) {
        $recordArgs += '-Tags'
        $recordArgs += $Tags
    }

    & pwsh @recordArgs 2>&1 | ForEach-Object { Write-Output $_ }
    $recordExit = $LASTEXITCODE
    if ($recordExit -ne 0) {
        Write-Output ("codex-verify could not record pending pitfall; recorder exit={0}" -f $recordExit)
        return
    }

    $resolvedPath = Join-Path $PendingRoot ("resolved_{0}.json" -f $pending.id)
    $resolved = [pscustomobject]@{
        schema_version = 1
        status = 'recorded'
        id = $pending.id
        recorded_at_utc = (Get-Date).ToUniversalTime().ToString('o')
        repo_root = $Repo
        failed_command = $pending.command
        passing_command = $CurrentCommandText
        failed_log_path = $pending.log_path
        solution = $solutionText
    }
    Set-Content -LiteralPath $resolvedPath -Encoding utf8 -Value ($resolved | ConvertTo-Json -Depth 6)
    Remove-Item -LiteralPath $latestPath -Force -ErrorAction SilentlyContinue
    Write-Output ("codex-verify recorded pending pitfall and cleared latest marker: {0}" -f $resolvedPath)
}

$repo = Get-RepoRootPath -Start $RepoRoot
$runId = ('{0:yyyyMMdd_HHmmss}_{1}' -f (Get-Date), [Guid]::NewGuid().ToString('N').Substring(0, 8))
$cacheRoot = Join-Path $repo '.codex-cache'
$logRoot = Join-Path $cacheRoot 'logs'
$tmpRoot = Join-Path (Join-Path $cacheRoot 'tmp') $runId
$logPath = Join-Path $logRoot ("codex-verify_{0}.log" -f $runId)
$pendingPitfallRoot = Join-Path $cacheRoot 'pending-pitfalls'
$verificationCommandText = Get-VerificationCommandText -ContextProfileValue $ContextProfile -ModeValue $Mode -BaseRefValue $BaseRef -IncludeUntrackedValue ([bool]$IncludeUntracked) -KeepArtifactsValue ([bool]$KeepArtifacts)

New-Item -ItemType Directory -Force -Path $logRoot, $tmpRoot | Out-Null

$prevTemp = $env:TEMP
$prevTmp = $env:TMP
$exitCode = 1

try {
    $env:TEMP = $tmpRoot
    $env:TMP = $tmpRoot

    Push-Location $repo
    try {
        if ($Mode -eq 'full') {
            $args = @{
                RepoRoot = '.'
                ContextProfile = $ContextProfile
            }
            & ./scripts/lint/run_all.ps1 @args 2>&1 | Tee-Object -FilePath $logPath
            $exitCode = $LASTEXITCODE
        }
        else {
            $args = @{
                RepoRoot = '.'
                ContextProfile = $ContextProfile
            }
            if (-not [string]::IsNullOrWhiteSpace($BaseRef)) {
                $args['BaseRef'] = $BaseRef
            }
            if ($IncludeUntracked) {
                $args['IncludeUntracked'] = $true
            }

            & ./scripts/lint/run_changed_scope.ps1 @args 2>&1 | Tee-Object -FilePath $logPath
            $exitCode = $LASTEXITCODE
        }
    }
    finally {
        Pop-Location
    }
}
finally {
    $env:TEMP = $prevTemp
    $env:TMP = $prevTmp

    if (-not $KeepArtifacts) {
        Remove-Item -LiteralPath $tmpRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}

if ($exitCode -ne 0) {
    if (-not $DisablePitfallHook) {
        Write-PendingPitfall -PendingRoot $pendingPitfallRoot -RunId $runId -Repo $repo -CommandText $verificationCommandText -ModeValue $Mode -ContextProfileValue $ContextProfile -FailureExitCode $exitCode -FailureLogPath $logPath
    }
    Write-Output ("codex-verify failed: mode={0} profile={1} exit={2} log={3}" -f $Mode, $ContextProfile, $exitCode, $logPath)
    exit $exitCode
}

if (-not $DisablePitfallHook) {
    Resolve-PendingPitfall -PendingRoot $pendingPitfallRoot -Repo $repo -CurrentCommandText $verificationCommandText -Solution $PitfallSolution -SourcePath $PitfallSourcePath -Category $PitfallCategory -Tags $PitfallTags -Prompt ([bool]$PromptForPitfallSolution)
}

Write-Output ("codex-verify passed: mode={0} profile={1} log={2}" -f $Mode, $ContextProfile, $logPath)
exit 0
