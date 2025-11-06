# 🧪 Ejemplos de Prueba

## Ejemplo 1: Texto sobre Inteligencia Artificial

### Entrada (texto directo):
```
La inteligencia artificial es una rama de la informática que busca crear máquinas 
capaces de realizar tareas que normalmente requieren inteligencia humana. Esto incluye 
el aprendizaje, el razonamiento, la percepción y el lenguaje natural. Las aplicaciones 
de IA van desde asistentes virtuales hasta sistemas de diagnóstico médico.
```

### Salida esperada:
Un cuento sobre robots que aprenden a pensar y ayudar a los humanos.

---

## Ejemplo 2: Texto sobre Historia

### Entrada (texto directo):
```
La Revolución Industrial fue un período de grandes cambios que comenzó en Inglaterra 
en el siglo XVIII. Las máquinas de vapor transformaron la producción, las fábricas 
reemplazaron a los talleres artesanales, y las ciudades crecieron rápidamente. 
Este cambio transformó la sociedad de forma permanente.
```

### Salida esperada:
Un cuento sobre un viaje en el tiempo a la época de las fábricas y el vapor.

---

## Ejemplo 3: Texto sobre Ciencia

### Entrada (texto directo):
```
La fotosíntesis es el proceso mediante el cual las plantas convierten la luz solar 
en energía química. Utilizan dióxido de carbono del aire y agua del suelo para 
producir glucosa y oxígeno. Este proceso es fundamental para la vida en la Tierra, 
ya que produce el oxígeno que respiramos.
```

### Salida esperada:
Un cuento sobre pequeñas plantas mágicas que convierten luz en alimento.

---

## Ejemplo 4: Documento PDF

### Archivo de prueba:
Puedes crear un PDF simple con este contenido:

```
El Sistema Solar

El sistema solar está formado por el Sol y todos los cuerpos celestes que orbitan 
a su alrededor. Incluye ocho planetas: Mercurio, Venus, Tierra, Marte, Júpiter, 
Saturno, Urano y Neptuno. Cada planeta tiene características únicas y algunos tienen 
sus propias lunas.

La Tierra es el único planeta conocido que alberga vida. Tiene agua líquida, una 
atmósfera protectora y está a la distancia perfecta del Sol.
```

### Salida esperada:
Un cuento sobre un viaje espacial visitando los diferentes planetas.

---

## Ejemplo 5: Documento Word (.docx)

### Contenido sugerido:
```
Los Océanos

Los océanos cubren más del 70% de la superficie de la Tierra. Son el hogar de 
millones de especies, desde el plancton microscópico hasta las ballenas gigantes. 
Los océanos juegan un papel crucial en el clima global, absorben dióxido de carbono 
y producen más de la mitad del oxígeno que respiramos.

Sin embargo, los océanos enfrentan amenazas como la contaminación por plásticos, 
el cambio climático y la sobrepesca. Es importante proteger estos ecosistemas 
vitales para las futuras generaciones.
```

### Salida esperada:
Un cuento sobre una aventura submarina descubriendo los secretos del océano.

---

## Ejemplo 6: Presentación PowerPoint (.pptx)

### Contenido de las diapositivas:
```
Diapositiva 1: La Energía Renovable
Diapositiva 2: Energía Solar - Paneles que capturan luz del sol
Diapositiva 3: Energía Eólica - Turbinas movidas por el viento
Diapositiva 4: Energía Hidráulica - Presas que aprovechan el agua
Diapositiva 5: Conclusión - Un futuro sostenible es posible
```

### Salida esperada:
Un cuento sobre un mundo que transforma su energía de formas sostenibles.

---

## Cómo probar

### Método 1: Con texto directo
1. Abre http://localhost:5000
2. Haz clic en "Escribir Texto"
3. Copia y pega uno de los ejemplos de texto
4. Haz clic en "Generar Cuento en Audio"

### Método 2: Con archivos
1. Crea un documento con el contenido sugerido
2. Guárdalo como PDF, Word o PowerPoint
3. Abre http://localhost:5000
4. Haz clic en "Subir Archivo"
5. Arrastra o selecciona tu archivo
6. Haz clic en "Generar Cuento en Audio"

---

## Tips para mejores resultados

✅ **Usa contenido claro y estructurado**
- El sistema funciona mejor con textos bien organizados

✅ **Contenido de 200-500 palabras**
- Muy corto: no hay suficiente material
- Muy largo: solo se procesan los primeros 4000 caracteres

✅ **Temas educativos**
- El sistema está optimizado para transformar contenido educativo en cuentos

✅ **Idioma español**
- El sistema funciona mejor con contenido en español

❌ **Evita:**
- Archivos muy grandes (más de 16MB)
- Contenido confuso o mal estructurado
- Tablas complejas o gráficos (no se extraen bien)
- Archivos escaneados (no son texto real)

---

## Verificación de resultados

### Audio generado
- ✅ Duración: 1-3 minutos aproximadamente
- ✅ Voz: Femenina (Nova) clara y profesional
- ✅ Formato: MP3 de alta calidad (HD)

### Texto generado
- ✅ Estructura narrativa (inicio, desarrollo, fin)
- ✅ Tono amigable y educativo
- ✅ Uso de metáforas y personajes
- ✅ 300-400 palabras aproximadamente

---

## Solución de problemas comunes

### "No se pudo extraer suficiente contenido"
- El texto es muy corto (menos de 50 caracteres)
- El archivo está corrupto
- El archivo es una imagen escaneada

### "Archivo no válido"
- El formato no es soportado (solo PDF, DOCX, PPTX, TXT)
- El archivo está protegido con contraseña

### "Error generando texto"
- Problema con la clave de OpenRouter
- Límite de cuota alcanzado

### "Error generando audio"
- Problema con la clave de OpenAI
- Límite de cuota alcanzado

---

## Monitoreo del proceso

En la terminal verás mensajes como:
```
📝 Procesando texto directo...
Iniciando generación de texto con OpenRouter...
✅ Texto generado con éxito por OpenRouter.
Convirtiendo texto generado a MP3 con TTS-1...
✅ Proceso completado. Archivo MP3 guardado en: outputs/cuento_xxx.mp3
```

¡Todo listo para probar! 🚀
