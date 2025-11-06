# 🚀 Guía Rápida de Inicio

## Paso 1: Configurar el entorno

1. Asegúrate de que el entorno virtual esté activo:
```powershell
.\entorno\Scripts\Activate.ps1
```

2. Verifica que todas las dependencias estén instaladas:
```powershell
pip install -r requirements.txt
```

## Paso 2: Configurar las claves API

1. Copia el archivo de ejemplo:
```powershell
Copy-Item .env.example .env
```

2. Edita el archivo `.env` y agrega tus claves:
```
OPENROUTER_API_KEY=tu_clave_real_de_openrouter
OPENAI_API_KEY=tu_clave_real_de_openai
```

### ¿Dónde conseguir las claves?

**OpenRouter (para generar el cuento):**
1. Ve a https://openrouter.ai/
2. Regístrate o inicia sesión
3. Ve a "API Keys" en tu perfil
4. Crea una nueva clave API
5. Copia y pega en el archivo `.env`

**OpenAI (para generar el audio):**
1. Ve a https://platform.openai.com/
2. Regístrate o inicia sesión
3. Ve a "API keys" (https://platform.openai.com/api-keys)
4. Crea una nueva clave secreta
5. Copia y pega en el archivo `.env`

## Paso 3: Iniciar la aplicación

### Opción A: Usando el script de inicio
```powershell
.\start.ps1
```

### Opción B: Manual
```powershell
python app.py
```

## Paso 4: Usar la aplicación

1. Abre tu navegador en: **http://localhost:5000**

2. Verás dos opciones:
   - **Subir Archivo**: Arrastra o selecciona un archivo (PDF, Word, PPT, TXT)
   - **Escribir Texto**: Escribe o pega directamente tu contenido

3. Haz clic en **"Generar Cuento en Audio"**

4. Espera unos momentos (30-60 segundos)

5. ¡Listo! Podrás:
   - 🎵 Escuchar el audio en el navegador
   - 📖 Leer el texto del cuento generado
   - 💾 Descargar el archivo MP3

## 📝 Ejemplos de uso

### Ejemplo 1: Documento sobre IA
Sube un PDF sobre inteligencia artificial → El sistema genera un cuento sobre robots que aprenden

### Ejemplo 2: Texto sobre historia
Escribe un texto sobre la Revolución Industrial → El sistema genera un cuento sobre un viaje en el tiempo

### Ejemplo 3: Presentación de negocios
Sube una presentación de PowerPoint → El sistema genera un cuento sobre un emprendedor

## ⚠️ Solución de problemas

### Error: "Module 'flask' not found"
```powershell
pip install flask
```

### Error: "No se encontró el archivo .env"
Crea el archivo `.env` copiando `.env.example` y agregando tus claves

### Error: "Invalid API key"
Verifica que tus claves API sean correctas en el archivo `.env`

### El audio tarda mucho en generarse
Es normal, el proceso puede tardar 30-60 segundos dependiendo del contenido

## 🎯 Consejos

- **Documentos largos**: El sistema toma los primeros 4000 caracteres
- **Mejor calidad**: Usa contenido claro y bien estructurado
- **Idioma**: El sistema funciona mejor con contenido en español
- **Tamaño de archivo**: Máximo 16 MB por archivo

## 📞 Ayuda

Si tienes problemas:
1. Verifica que el entorno virtual esté activo
2. Verifica que las claves API sean válidas
3. Revisa los mensajes de error en la terminal
4. Consulta el archivo README.md para más detalles
