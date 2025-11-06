# 🤖 Modelos Disponibles en OpenRouter

## Modelos Recomendados (ordenados por calidad)

### 1. ⭐ Claude 3.5 Sonnet (RECOMENDADO - ACTUAL)
```python
AI_MODEL = "anthropic/claude-3.5-sonnet"
```
- ✅ **Excelente calidad narrativa**
- ✅ Muy bueno para crear cuentos creativos
- ✅ Rápido y confiable
- ✅ Entiende contexto complejo
- 💰 Costo: ~$3 por millón de tokens
- 🎯 **Mejor para: Cuentos de alta calidad**

### 2. GPT-4 Turbo
```python
AI_MODEL = "openai/gpt-4-turbo"
```
- ✅ Muy buena calidad general
- ✅ Creativo y coherente
- ✅ Amplio conocimiento
- 💰 Costo: ~$10 por millón de tokens
- 🎯 **Mejor para: Contenido técnico complejo**

### 3. GPT-3.5 Turbo (Económico)
```python
AI_MODEL = "openai/gpt-3.5-turbo"
```
- ✅ Buena calidad
- ✅ Muy rápido
- ✅ Más económico
- ✅ Ideal para uso frecuente
- 💰 Costo: ~$0.50 por millón de tokens
- 🎯 **Mejor para: Uso diario, muchos cuentos**

### 4. Claude 3 Haiku (Rápido)
```python
AI_MODEL = "anthropic/claude-3-haiku"
```
- ✅ Extremadamente rápido
- ✅ Buena calidad
- ✅ Muy económico
- 💰 Costo: ~$0.25 por millón de tokens
- 🎯 **Mejor para: Pruebas rápidas**

### 5. Llama 3.1 70B (GRATIS) 🎁
```python
AI_MODEL = "meta-llama/llama-3.1-70b-instruct"
```
- ✅ **GRATIS o muy económico**
- ✅ Buena calidad
- ⚠️ Puede ser más lento en horas pico
- 💰 Costo: GRATIS o ~$0.10 por millón
- 🎯 **Mejor para: Experimentar sin costo**

### 6. Mistral Large
```python
AI_MODEL = "mistralai/mistral-large"
```
- ✅ Buena calidad narrativa
- ✅ Buen balance precio/calidad
- ✅ Multilingüe
- 💰 Costo: ~$2 por millón de tokens
- 🎯 **Mejor para: Balance calidad-precio**

---

## 🔧 Cómo cambiar el modelo

### Opción 1: Editar config.py (RECOMENDADO)
1. Abre el archivo `config.py`
2. Busca la línea `AI_MODEL = "..."`
3. Cambia el valor por el modelo deseado
4. Guarda el archivo
5. Reinicia la aplicación

### Opción 2: Editar app.py directamente
1. Abre `app.py`
2. Busca la función `procesar_y_generar_audio`
3. Cambia `MODELO_TEXTO = "..."`
4. Guarda y reinicia

---

## 💰 Comparación de Costos Reales

Para generar **1 cuento** (aproximadamente 500 palabras de entrada + 500 de salida):

| Modelo | Costo por Cuento | Cuentos por $1 |
|--------|------------------|----------------|
| Claude 3.5 Sonnet | $0.003 | ~333 cuentos |
| GPT-4 Turbo | $0.010 | ~100 cuentos |
| GPT-3.5 Turbo | $0.0005 | ~2,000 cuentos |
| Claude 3 Haiku | $0.0002 | ~5,000 cuentos |
| Llama 3.1 70B | GRATIS | ∞ cuentos |
| Mistral Large | $0.002 | ~500 cuentos |

---

## 📊 Tabla Comparativa Completa

| Característica | Claude 3.5 | GPT-4 | GPT-3.5 | Haiku | Llama 3.1 | Mistral |
|----------------|------------|-------|---------|-------|-----------|---------|
| **Calidad** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Velocidad** | ⚡⚡⚡⚡ | ⚡⚡⚡ | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡⚡ | ⚡⚡⚡ | ⚡⚡⚡⚡ |
| **Creatividad** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Precio** | $$ | $$$ | $ | $ | GRATIS | $$ |
| **Narrativa** | Excelente | Excelente | Muy buena | Muy buena | Buena | Muy buena |

---

## 💡 Recomendación por Caso de Uso

### 🎓 Para proyectos educativos/universitarios:
**Claude 3.5 Sonnet** o **Llama 3.1 70B** (gratis)

### 💼 Para uso profesional:
**Claude 3.5 Sonnet** o **GPT-4 Turbo**

### 🚀 Para pruebas y desarrollo:
**GPT-3.5 Turbo** o **Claude 3 Haiku**

### 💰 Para minimizar costos:
**Llama 3.1 70B** (gratis) o **Claude 3 Haiku**

### ⚡ Para máxima velocidad:
**Claude 3 Haiku** o **GPT-3.5 Turbo**

---

## ⚠️ Notas Importantes

1. **Modelo anterior (no usar):**
   - `nousresearch/nous-hermes-2-mixtral-8x7b-dpo` → ❌ YA NO DISPONIBLE

2. **Verificar disponibilidad:**
   - Algunos modelos pueden no estar disponibles temporalmente
   - Visita https://openrouter.ai/models para ver el estado actual

3. **Límites de uso:**
   - OpenRouter puede tener límites de cuota según tu plan
   - Verifica tu dashboard: https://openrouter.ai/credits

4. **Calidad vs Costo:**
   - Modelos más caros no siempre son mejores para todos los casos
   - Claude 3.5 Sonnet ofrece el mejor balance para cuentos

---

## 🔗 Recursos Adicionales

- **OpenRouter Dashboard:** https://openrouter.ai/
- **Documentación de Modelos:** https://openrouter.ai/docs
- **Precios Actualizados:** https://openrouter.ai/models
- **API Keys:** https://openrouter.ai/keys

---

## 🆘 Solución de Problemas

### Error: "Model not found"
→ El modelo no está disponible. Prueba con otro de la lista.

### Error: "Insufficient credits"
→ Necesitas agregar créditos en OpenRouter.

### Respuestas de baja calidad:
→ Prueba Claude 3.5 Sonnet o GPT-4 Turbo.

### Muy lento:
→ Prueba Claude 3 Haiku o GPT-3.5 Turbo.

### Muy caro:
→ Usa Llama 3.1 70B (gratis) o Claude 3 Haiku.

---

**Última actualización:** Noviembre 2025
