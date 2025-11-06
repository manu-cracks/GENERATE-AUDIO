"""
Configuración del sistema de generación de cuentos
Edita este archivo para cambiar el comportamiento del sistema
"""

# ============================================
# CONFIGURACIÓN DEL MODELO DE IA
# ============================================

# Modelo principal (puedes cambiarlo fácilmente aquí)
AI_MODEL = "anthropic/claude-3.5-sonnet"

# Modelos alternativos (descomenta el que quieras usar):
# AI_MODEL = "openai/gpt-4-turbo"                     # Muy buena calidad, más caro
# AI_MODEL = "openai/gpt-3.5-turbo"                   # Rápido y económico
# AI_MODEL = "anthropic/claude-3-haiku"               # Muy rápido y barato
# AI_MODEL = "meta-llama/llama-3.1-70b-instruct"      # GRATIS o muy económico
# AI_MODEL = "mistralai/mistral-large"                # Buen balance precio/calidad

# Parámetros de generación de texto
MAX_TOKENS = 1500       # Cantidad máxima de tokens para el cuento
TEMPERATURE = 0.7       # 0.0 = más preciso/consistente, 1.0 = más creativo/variable

# ============================================
# CONFIGURACIÓN DEL AUDIO (OpenAI TTS)
# ============================================

# Modelo de conversión texto-a-voz
TTS_MODEL = "tts-1-hd"  # "tts-1-hd" = alta calidad, "tts-1" = más rápido

# Voz para el audio
TTS_VOICE = "nova"      # Voz femenina clara y profesional

# Voces disponibles (descomenta para cambiar):
# TTS_VOICE = "alloy"   # Neutral, versátil
# TTS_VOICE = "echo"    # Masculina, clara
# TTS_VOICE = "fable"   # Expresiva, con acento británico
# TTS_VOICE = "onyx"    # Masculina, profunda y autoritaria
# TTS_VOICE = "shimmer" # Femenina, cálida y amigable

# ============================================
# CONFIGURACIÓN DE ARCHIVOS
# ============================================

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'pptx'}

# ============================================
# CONFIGURACIÓN DE PROCESAMIENTO
# ============================================

# Máximo de caracteres a procesar del documento
MAX_CHARS_PROCESS = 4000

# Palabras objetivo para el cuento generado
TARGET_WORDS_MIN = 400
TARGET_WORDS_MAX = 600
