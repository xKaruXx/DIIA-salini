param(
    [int]$Port = 8851,
    [string]$HostName = "127.0.0.1",
    [switch]$SkipModelPull,
    [switch]$PullComparisonModels,
    [switch]$NoOpen
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
Set-Location $RootDir

function Test-HttpOk {
    param([string]$Url, [int]$TimeoutSec = 2)

    try {
        Invoke-RestMethod -Uri $Url -TimeoutSec $TimeoutSec | Out-Null
        return $true
    } catch {
        return $false
    }
}

function Wait-HttpOk {
    param([string]$Url, [int]$Seconds = 30)

    for ($i = 0; $i -lt $Seconds; $i++) {
        if (Test-HttpOk -Url $Url) {
            return $true
        }
        Start-Sleep -Seconds 1
    }
    return $false
}

function Get-EnvValue {
    param([string]$Name, [string]$DefaultValue)

    $envPath = Join-Path $RootDir ".env"
    if (-not (Test-Path $envPath)) {
        return $DefaultValue
    }

    $line = Get-Content $envPath | Where-Object { $_ -match "^\s*$Name\s*=" } | Select-Object -First 1
    if (-not $line) {
        return $DefaultValue
    }

    return ($line -replace "^\s*$Name\s*=\s*", "").Trim()
}

function Get-PythonCommand {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        return "py"
    }
    if (Get-Command python -ErrorAction SilentlyContinue) {
        return "python"
    }
    throw "No se encontro Python. Instalar Python 3.11 o habilitar el launcher 'py'."
}

function Test-OllamaModel {
    param([string]$ModelName)

    $escaped = [regex]::Escape($ModelName)
    $list = & ollama list 2>$null
    return [bool]($list | Select-String -Pattern "^$escaped\s")
}

function Ensure-OllamaModel {
    param([string]$ModelName)

    if ([string]::IsNullOrWhiteSpace($ModelName)) {
        return
    }
    if (Test-OllamaModel -ModelName $ModelName) {
        Write-Host "Modelo disponible: $ModelName"
        return
    }

    if ($SkipModelPull) {
        Write-Warning "Modelo no encontrado: $ModelName. Ejecutar: ollama pull $ModelName"
        return
    }

    Write-Host "Descargando modelo faltante: $ModelName"
    & ollama pull $ModelName
}

$ollama = Get-Command ollama -ErrorAction SilentlyContinue
if (-not $ollama) {
    throw "No se encontro Ollama en PATH. Instalar Ollama antes de ejecutar la demo."
}

$ollamaUrl = "http://127.0.0.1:11434/api/tags"
if (-not (Test-HttpOk -Url $ollamaUrl)) {
    Write-Host "Iniciando Ollama..."
    Start-Process -FilePath $ollama.Source -ArgumentList @("serve") -WindowStyle Hidden | Out-Null
    if (-not (Wait-HttpOk -Url $ollamaUrl -Seconds 30)) {
        throw "Ollama no respondio en http://127.0.0.1:11434. Abrir Ollama manualmente y reintentar."
    }
}

$chatModel = Get-EnvValue -Name "CHAT_MODEL_NAME" -DefaultValue "qwen3.5:0.8b"
$embeddingModel = Get-EnvValue -Name "EMBEDDING_MODEL_NAME" -DefaultValue "nomic-embed-text:latest"
Ensure-OllamaModel -ModelName $chatModel
Ensure-OllamaModel -ModelName $embeddingModel

if ($PullComparisonModels) {
    @(
        "gemma3:270m",
        "granite4:350m",
        "lfm2.5-thinking:1.2b",
        "qwen3.5:0.8b",
        "deepseek-r1:1.5b",
        "llama3.2:3b",
        "granite4.1:3b",
        "nemotron-3-nano:4b",
        "qwen3.5:4b",
        "qwen3.5:latest",
        "gemma4:e4b"
    ) | ForEach-Object { Ensure-OllamaModel -ModelName $_ }
}

$healthUrl = "http://$HostName`:$Port/health"
if (-not (Test-HttpOk -Url $healthUrl)) {
    $python = Get-PythonCommand
    Write-Host "Iniciando backend FastAPI en http://$HostName`:$Port ..."
    Start-Process -FilePath $python -ArgumentList @("run.py", "--host", $HostName, "--port", "$Port") -WorkingDirectory $RootDir -WindowStyle Hidden | Out-Null
    if (-not (Wait-HttpOk -Url $healthUrl -Seconds 45)) {
        throw "El backend no respondio en $healthUrl. Revisar dependencias con: py -m pip install -r requirements.txt"
    }
}

$presentationUrl = "http://localhost:$Port/docs/presentacion_final_chatbot_coradir.html"
if ($NoOpen) {
    Write-Host "Presentacion lista en: $presentationUrl"
} else {
    Write-Host "Abriendo presentacion: $presentationUrl"
    Start-Process $presentationUrl
}

Write-Host ""
Write-Host "Demo lista."
Write-Host "En la seccion Demo, usar 'Cargar chat' o 'Cargar modelos'."
