# Script de inicio rápido para PODCAST-AI
# Ejecutar con: .\start.ps1

Write-Host "🎙️ Iniciando Generador de Cuentos en Audio..." -ForegroundColor Cyan
Write-Host ""

# Verificar si existe el entorno virtual
if (Test-Path ".\entorno\Scripts\Activate.ps1") {
    Write-Host "✅ Activando entorno virtual..." -ForegroundColor Green
    .\entorno\Scripts\Activate.ps1
} else {
    Write-Host "❌ Error: No se encontró el entorno virtual" -ForegroundColor Red
    Write-Host "   Ejecuta primero: python -m venv entorno" -ForegroundColor Yellow
    exit 1
}

# Verificar si existe el archivo .env
if (-not (Test-Path ".\.env")) {
    Write-Host "⚠️  Advertencia: No se encontró el archivo .env" -ForegroundColor Yellow
    Write-Host "   Copia .env.example a .env y configura tus claves API" -ForegroundColor Yellow
    Write-Host ""
}

# Iniciar la aplicación
Write-Host "🚀 Iniciando servidor web..." -ForegroundColor Green
Write-Host "📍 Abre tu navegador en: http://localhost:5000" -ForegroundColor Cyan
Write-Host "⏹️  Presiona Ctrl+C para detener el servidor" -ForegroundColor Yellow
Write-Host ""

python app.py
