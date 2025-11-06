# ✅ Checklist de Verificación

## Antes de iniciar la aplicación

### 1. Entorno Virtual
- [ ] El entorno virtual está creado (`entorno/` existe)
- [ ] El entorno virtual está activado (ves `(entorno)` en tu terminal)
- [ ] Comando para activar: `.\entorno\Scripts\Activate.ps1`

### 2. Dependencias Instaladas
- [ ] Flask instalado
- [ ] python-dotenv instalado
- [ ] openai instalado
- [ ] pypdf instalado
- [ ] python-docx instalado
- [ ] python-pptx instalado
- [ ] werkzeug instalado

**Verificar con:**
```powershell
pip list | Select-String "flask|openai|pypdf|python-docx|python-pptx|werkzeug|python-dotenv"
```

**Instalar si falta:**
```powershell
pip install -r requirements.txt
```

### 3. Configuración de API Keys
- [ ] Archivo `.env` existe en la raíz del proyecto
- [ ] `OPENROUTER_API_KEY` está configurada en `.env`
- [ ] `OPENAI_API_KEY` está configurada en `.env`
- [ ] Las claves son válidas (no están vacías o son de ejemplo)

**Verificar con:**
```powershell
Get-Content .env
```

### 4. Estructura de Carpetas
- [ ] Carpeta `templates/` existe
- [ ] Archivo `templates/index.html` existe
- [ ] Carpeta `uploads/` existe
- [ ] Carpeta `outputs/` existe

**Crear si faltan:**
```powershell
New-Item -ItemType Directory -Force -Path "uploads", "outputs", "templates"
```

### 5. Archivos del Proyecto
- [ ] `app.py` existe
- [ ] `requirements.txt` existe
- [ ] `templates/index.html` existe
- [ ] `README.md` existe
- [ ] `GUIA_RAPIDA.md` existe

### 6. Permisos y Firewall
- [ ] Python tiene permisos para crear archivos
- [ ] Firewall permite conexiones en puerto 5000
- [ ] No hay otra aplicación usando el puerto 5000

**Verificar puerto:**
```powershell
netstat -an | Select-String ":5000"
```

### 7. Conexión a Internet
- [ ] Tienes conexión a internet activa
- [ ] Puedes acceder a https://openrouter.ai/
- [ ] Puedes acceder a https://api.openai.com/

---

## Al iniciar la aplicación

### 8. Inicio Correcto
- [ ] La aplicación inicia sin errores
- [ ] Ves el mensaje: `Running on http://0.0.0.0:5000`
- [ ] No hay mensajes de error en rojo

### 9. Acceso a la Interfaz
- [ ] Puedes abrir http://localhost:5000 en el navegador
- [ ] La página carga correctamente
- [ ] Ves el título "Generador de Cuentos en Audio"
- [ ] Los tabs funcionan (Subir Archivo / Escribir Texto)

---

## Durante el uso

### 10. Funcionalidades Básicas
- [ ] Puedes hacer clic en "Subir Archivo"
- [ ] Puedes arrastrar archivos al área de carga
- [ ] Puedes seleccionar archivos con el selector
- [ ] Puedes escribir texto en el área de texto
- [ ] El botón "Generar Cuento en Audio" está habilitado

### 11. Procesamiento
- [ ] Al enviar, aparece el spinner de carga
- [ ] Ves mensajes en la terminal del proceso
- [ ] El proceso no toma más de 2 minutos
- [ ] No hay errores en la terminal

### 12. Resultado
- [ ] El audio se genera correctamente
- [ ] Puedes reproducir el audio en el navegador
- [ ] Puedes ver el texto del cuento generado
- [ ] El archivo MP3 se guarda en `outputs/`

---

## Solución de problemas

### Si algo falla, verifica:

#### Error: "Module not found"
```powershell
# Verifica que el entorno virtual esté activo
pip list
# Reinstala dependencias
pip install -r requirements.txt
```

#### Error: "Template not found"
```powershell
# Verifica que exista templates/index.html
Test-Path "templates\index.html"
```

#### Error: "API key not found"
```powershell
# Verifica el archivo .env
Get-Content .env
# Asegúrate de que las claves no estén vacías
```

#### Error: "Port already in use"
```powershell
# Encuentra qué proceso usa el puerto
netstat -ano | Select-String ":5000"
# Mata el proceso o cambia el puerto en app.py
```

#### Error: "File not found" al procesar
```powershell
# Verifica que las carpetas existan
Test-Path "uploads"
Test-Path "outputs"
```

---

## Comandos útiles

### Ver logs en tiempo real
```powershell
# La terminal donde ejecutaste `python app.py` muestra logs automáticamente
```

### Limpiar archivos generados
```powershell
Remove-Item -Path "outputs\*.mp3" -Force
```

### Limpiar archivos temporales
```powershell
Remove-Item -Path "uploads\*" -Exclude ".gitkeep" -Force
```

### Detener la aplicación
```
Ctrl + C en la terminal
```

### Reiniciar la aplicación
```powershell
# Detén con Ctrl+C, luego:
python app.py
```

---

## Estado esperado después de todo OK

```
✅ Entorno virtual activo
✅ Dependencias instaladas
✅ Claves API configuradas
✅ Servidor web corriendo en puerto 5000
✅ Interfaz accesible en http://localhost:5000
✅ Puedes subir archivos o escribir texto
✅ El sistema genera cuentos en audio MP3
✅ Puedes reproducir y descargar los audios
```

---

## Última verificación antes de usar

Ejecuta estos comandos para verificar todo:

```powershell
# 1. Verificar entorno virtual
if ($env:VIRTUAL_ENV) { Write-Host "✅ Entorno virtual activo" } else { Write-Host "❌ Activa el entorno virtual" }

# 2. Verificar dependencias críticas
python -c "import flask, openai, pypdf, docx, pptx; print('✅ Todas las dependencias instaladas')"

# 3. Verificar archivo .env
if (Test-Path .env) { Write-Host "✅ Archivo .env existe" } else { Write-Host "❌ Crea el archivo .env" }

# 4. Verificar estructura
if ((Test-Path templates) -and (Test-Path uploads) -and (Test-Path outputs)) { 
    Write-Host "✅ Estructura de carpetas correcta" 
} else { 
    Write-Host "❌ Faltan carpetas" 
}
```

Si todo marca ✅, ¡estás listo para usar la aplicación! 🚀
