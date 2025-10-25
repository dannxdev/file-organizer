# 📁 file-organizer

**file-organizer** es un script en Python que organiza archivos automáticamente en carpetas según su tipo (documentos, imágenes, videos, audio, código, etc.). Ideal para limpiar directorios desordenados y clasificar archivos por extensión.

---

## 🚀 ¿Cómo funciona?

El script identifica la **extensión de cada archivo** dentro de una carpeta llamada `__source__` y los **mueve** a subcarpetas específicas según su categoría:

- `.pdf`, `.docx`, `.txt` → `Documentos`
- `.jpg`, `.png`, `.gif` → `Imagenes`
- `.mp4`, `.mkv`, `.mov` → `Videos`
- `.mp3`, `.wav`, `.flac` → `Audio`
- `.py`, `.js`, `.html`, `.css` → `Codigo`
- Las anteriores son solo algunas de las extensiones que el script puede agrupar.
- Otros tipos se agrupan en carpetas genéricas como `Otros`

---

## 📦 Instrucciones de uso

1. **Mover el script** `file_organizer.py` al directorio que deseas organizar.
2. El script buscará (o creará si no existe) una carpeta llamada `__source__` en la misma ruta.
3. **Coloca todos los archivos y carpetas que deseas organizar dentro de `__source__`.**
4. Ejecuta el script (haz doble click en `file_organizer.py` ):
   ```bash
   python file_organizer.py
   ```

5. Los archivos serán movidos automáticamente a carpetas organizadas por tipo.
6. La consola mostrara un informe de los archivos modificados.

### ⚠️ Recomendaciones importantes

- Evita ejecutar el script en directorios que ya han sido organizados previamente, ya que puede reubicar archivos de forma no deseada.
- Si el script ya fue ejecutado, no reorganices manualmente los archivos antes de volver a correrlo.
- El script puede presentar errores menores si se incluyen carpetas con demasiadas subcarpetas anidadas. Se recomienda mantener los archivos lo más cerca posible de la carpeta `__source__`.
- Si `__source__` no existe, el script la creará automáticamente. En ese caso, cierra el programa, mueve los archivos a `__source__` y vuelve a ejecutarlo.

---

## 🛠️ Estado actual

- ✅ Funcional para la mayoría de casos simples
- ⚠️ Error menor al procesar estructuras de carpetas excesivamente profundas
- 🧪 Recomendado para directorios no organizados

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## ✨ Autor

DannyDev
