# 🔧 Solución de Problemas Comunes

## ❌ Error: "No endpoints found for model"

### Síntoma:
```
Error code: 404 - {'error': {'message': 'No endpoints found for nousresearch/nous-hermes-2-mixtral-8x7b-dpo.'}}
```

### ✅ Solución:
El modelo ya no está disponible. **Ya está corregido** en tu código.

**Modelo anterior (no funciona):**
```python
MODELO_TEXTO = "nousresearch/nous-hermes-2-mixtral-8x7b-dpo"  # ❌ OBSOLETO
```

**Modelo actual (funciona):**
```python
MODELO_TEXTO = "anthropic/claude-3.5-sonnet"  # ✅ ACTUALIZADO
```

**Cambios aplicados:**
1. ✅ Actualizado en `app.py`
2. ✅ Creado `config.py` para cambios fáciles
3. ✅ Documentado en `MODELOS_DISPONIBLES.md`

---

## ❌ Error: "Invalid API Key"

### Síntoma:
```
Error: Authentication failed
Invalid API key
```

### ✅ Solución:

#### Paso 1: Verifica tu archivo `.env`
```bash
# El archivo debe existir en la raíz del proyecto
OPENROUTER_API_KEY=sk-or-v1-xxxxx
OPENAI_API_KEY=sk-xxxxx
```

#### Paso 2: Obtén claves válidas

**Para OpenRouter (genera el texto del cuento):**
1. Ve a: https://openrouter.ai/
2. Crea una cuenta o inicia sesión
3. Ve a "Keys" o "API Keys"
4. Crea una nueva clave
5. Copia y pega en `.env` → `OPENROUTER_API_KEY=`

**Para OpenAI (genera el audio MP3):**
1. Ve a: https://platform.openai.com/
2. Crea una cuenta o inicia sesión
3. Ve a: https://platform.openai.com/api-keys
4. Crea una nueva clave secreta
5. Copia y pega en `.env` → `OPENAI_API_KEY=`

#### Paso 3: Verifica las claves
```powershell
# Ver contenido del .env (sin mostrar claves completas)
Get-Content .env | ForEach-Object { $_.Substring(0, [Math]::Min(30, $_.Length)) + "..." }
```

#### Paso 4: Reinicia la aplicación
```powershell
# Detén con Ctrl+C y vuelve a iniciar
python app.py
```

---

## ❌ Error: "Insufficient credits"

### Síntoma:
```
Error: You have insufficient credits
```

### ✅ Solución:

#### Para OpenRouter:
1. Ve a: https://openrouter.ai/credits
2. Agrega créditos a tu cuenta
3. Mínimo recomendado: $5 USD

#### Alternativa GRATIS:
Usa el modelo Llama 3.1 (gratis) en `app.py`:
```python
MODELO_TEXTO = "meta-llama/llama-3.1-70b-instruct"  # GRATIS
```

---

## ❌ Error al leer archivos PDF/Word/PowerPoint

### Síntoma:
```
Error al leer PDF: ...
Error al leer Word: ...
```

### ✅ Solución:

#### Opción 1: Reinstalar dependencias
```powershell
.\entorno\Scripts\Activate.ps1
pip install --upgrade pypdf python-docx python-pptx
```

#### Opción 2: Verificar el archivo
- ¿El archivo está corrupto?
- ¿Está protegido con contraseña?
- ¿Es un archivo escaneado (imagen)? No se puede extraer texto

#### Opción 3: Convertir el archivo
- PDF escaneado → Usa OCR o convierte a PDF con texto
- Archivo antiguo → Guarda en formato nuevo (.docx, no .doc)

---

## ❌ El audio suena entrecortado o de mala calidad

### ✅ Solución:

Edita `app.py` en la sección de audio:
```python
# Busca esta línea y cámbiala:
model="tts-1-hd",      # HD = Alta calidad
voice="nova",          # Voz clara y profesional
```

**Voces disponibles:**
- `nova` - Femenina, clara (recomendada)
- `alloy` - Neutral
- `echo` - Masculina, clara
- `shimmer` - Femenina, cálida
- `onyx` - Masculina, profunda

---

## ❌ El cuento es muy corto

### ✅ Solución:

En `app.py`, aumenta los tokens:
```python
max_tokens=1500,      # Aumenta a 2000 o más para cuentos más largos
temperature=0.7       # Aumenta a 0.8-0.9 para más creatividad
```

---

## ❌ El cuento es muy largo o tarda mucho

### ✅ Solución:

En `app.py`, reduce los tokens:
```python
max_tokens=800,       # Reduce para cuentos más cortos
temperature=0.5       # Reduce para ser más conciso
```

---

## ❌ Error: "Module not found"

### Síntoma:
```
ModuleNotFoundError: No module named 'flask'
ModuleNotFoundError: No module named 'openai'
```

### ✅ Solución:

#### Paso 1: Verifica el entorno virtual
```powershell
# Debe estar activo (verás "(entorno)" al inicio)
.\entorno\Scripts\Activate.ps1
```

#### Paso 2: Instala todas las dependencias
```powershell
pip install -r requirements.txt
```

#### Paso 3: Verifica instalación
```powershell
pip list | Select-String "flask|openai|pypdf|docx|pptx"
```

---

## ❌ El proceso tarda más de 2 minutos

### ✅ Solución:

**Esto es normal si:**
- Es la primera vez que usas un modelo
- El documento es muy largo
- El servidor está ocupado

**Mejoras:**
1. Usa un modelo más rápido:
   ```python
   MODELO_TEXTO = "anthropic/claude-3-haiku"  # Muy rápido
   ```

2. Reduce el contenido procesado en `app.py`:
   ```python
   {contenido_archivo[:2000]}  # Procesa menos caracteres
   ```

---

## ❌ Error: "Port already in use"

### Síntoma:
```
OSError: [WinError 10048] Solo se permite el uso de cada dirección de socket
```

### ✅ Solución:

#### Opción 1: Cerrar aplicación anterior
```powershell
# Busca el proceso usando el puerto 5000
netstat -ano | Select-String ":5000"

# Mata el proceso (reemplaza XXXX con el PID)
taskkill /PID XXXX /F
```

#### Opción 2: Cambiar el puerto
En `app.py`, al final:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambiar a 5001
```

---

## ❌ No puedo descargar el archivo MP3

### ✅ Solución:

1. **Verifica que se generó:**
   ```powershell
   ls outputs\
   ```

2. **Haz clic en "💾 Guardar Audio en mi PC"**
   - Se abrirá el diálogo "Guardar como"
   - Elige dónde guardarlo

3. **Si no funciona:**
   - Verifica permisos de descarga en tu navegador
   - Desactiva bloqueadores de pop-ups

---

## ❌ El texto extraído está vacío o incompleto

### ✅ Solución:

**Para PDF:**
- Si es PDF escaneado (imagen), no funcionará
- Necesitas un PDF con texto real

**Para Word:**
- Usa formato `.docx` (no `.doc`)
- Verifica que el documento tenga contenido

**Para PowerPoint:**
- Solo extrae texto de las diapositivas
- No extrae texto de imágenes

---

## 🔍 Cómo verificar que todo está bien

### Checklist rápido:
```powershell
# 1. Entorno virtual activo
if ($env:VIRTUAL_ENV) { "✅ Entorno OK" } else { "❌ Activa entorno" }

# 2. Dependencias instaladas
python -c "import flask, openai, pypdf, docx, pptx; print('✅ Dependencias OK')"

# 3. Archivo .env existe
if (Test-Path .env) { "✅ .env OK" } else { "❌ Crea .env" }

# 4. Carpetas existen
if ((Test-Path uploads) -and (Test-Path outputs)) { "✅ Carpetas OK" } else { "❌ Crea carpetas" }
```

---

## 📞 Soporte Adicional

### Recursos útiles:
- `README.md` - Documentación general
- `GUIA_RAPIDA.md` - Inicio rápido
- `CHECKLIST.md` - Verificación completa
- `MODELOS_DISPONIBLES.md` - Lista de modelos
- `EJEMPLOS_PRUEBA.md` - Ejemplos para probar

### Logs útiles:
Los mensajes en la terminal te dicen exactamente qué está pasando:
- `📝 Procesando texto directo...` - Leyendo entrada
- `🤖 Generando texto...` - Creando cuento
- `🔊 Generando audio...` - Creando MP3
- `✅ Proceso completado` - ¡Listo!
- `❌ Error...` - Algo falló (lee el mensaje)

---

## 🆘 Si nada funciona

1. **Desactiva y reactiva el entorno:**
   ```powershell
   deactivate
   .\entorno\Scripts\Activate.ps1
   ```

2. **Reinstala todo:**
   ```powershell
   pip uninstall -y -r requirements.txt
   pip install -r requirements.txt
   ```

3. **Verifica las claves API:**
   - OpenRouter: https://openrouter.ai/keys
   - OpenAI: https://platform.openai.com/api-keys

4. **Lee los logs completos** en la terminal donde ejecutas `python app.py`

---

**Última actualización:** Noviembre 2025
**Estado del código:** ✅ Actualizado y funcional
