$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

function Get-PreferredPython {
    $candidates = @()

    $venvPython = Join-Path $repoRoot '.venv\Scripts\python.exe'
    if (Test-Path $venvPython) { $candidates += $venvPython }

    if (Get-Command uv -ErrorAction SilentlyContinue) {
        $uvPython = & uv python find 2>$null
        if ($LASTEXITCODE -eq 0 -and $uvPython) {
            $candidates += $uvPython.Trim()
        }
    }

    if (Get-Command mise -ErrorAction SilentlyContinue) {
        $misePython = & mise which python 2>$null
        if ($LASTEXITCODE -eq 0 -and $misePython) {
            $candidates += $misePython.Trim()
        }
    }

    $localBin = Join-Path $env:USERPROFILE '.local\bin'
    $localMatches = Get-ChildItem (Join-Path $localBin 'python*.exe') -ErrorAction SilentlyContinue |
        Sort-Object Name -Descending
    foreach ($match in $localMatches) {
        if ($match.FullName -notmatch 'WindowsApps') {
            $candidates += $match.FullName
        }
    }

    foreach ($candidate in $candidates) {
        if ($candidate -and (Test-Path $candidate)) {
            return $candidate
        }
    }

    $pythonCmd = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCmd -and $pythonCmd.Source -notmatch 'WindowsApps') {
        return $pythonCmd.Source
    }

    $pyCmd = Get-Command py -ErrorAction SilentlyContinue
    if ($pyCmd) {
        return 'py'
    }

    throw 'No usable Python interpreter was found. Install Python via uv/mise or add a .venv, then rerun this script.'
}

$python = Get-PreferredPython
& $python (Join-Path $repoRoot 'scripts\sync_agents.py') @args
