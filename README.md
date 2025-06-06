# 🧾 PDF Viewer para PySide6 usando PDF.js + QWebEngine

Este repositorio provee una **solución lista para usar** para visualizar archivos PDF en una aplicación PySide6, utilizando un visor moderno basado en **PDF.js** (de Mozilla) embebido en un `QWebEngineView`.

> 🔍 Esta solución surge por la falta de ejemplos funcionales y prácticos que integren correctamente PDF.js con PySide6. Si estás buscando un visor PDF para tus apps Qt sin depender de bibliotecas externas complicadas, ¡esto es para ti!

---
![Captura de pantalla 2025-05-18 190620](https://github.com/user-attachments/assets/14938b6d-7605-49ec-8c18-3e7d15751d59)

---

## 🚀 Características

- Visualizador de PDF con **PDF.js** (renderizado HTML5).
- Integración limpia con `QWebEngineView` de PySide6.
- Compatible con botones personalizados: imprimir, guardar, cerrar.
- Soporte para archivos PDF locales y temporales.
- Control completo del flujo de impresión con `win32print`.
- Descargar archivos desde el visor con `QFileDialog`.
- Limpieza de caché y manejo robusto de errores.

## 🧩 Estructura del proyecto

A continuación se muestra la estructura de carpetas y archivos del proyecto, con una breve descripción de cada componente.

```bash
├── app.py                            # Punto de entrada de la app
├── module/
│   └── pdf_previewer_functions.py    # Lógica principal del visor
├── utils/
│   ├── pdfjs/                        # PDF.js (versión personalizada)
│   │   └── web/viewer.html           # Visor PDF.js
│   ├── icons/                        # Iconos para los botones
│   └── widgets/
│       └── rotating_circle.py        # Indicador de carga personalizado
├── docs/
    └── PDF Test File HTML5.pdf       # PDF de prueba
```

## 🛠️ Requisitos

- Python 3.8+
- PySide6
- PySide6-WebEngine
- pywin32 (para impresión en Windows)

Instala las dependencias con:

```bash
pip install PySide6==6.7.0
pip install pywin32==306
```

## ▶️ ¿Cómo se usa?
Clona el repositorio:

```bash
git clone https://github.com/Zerous12/PDF-viewer-with-Pyside6-and-QWebEngine.git
cd PDF-viewer-with-Pyside6-and-QWebEngine
```
Coloca tus archivos PDF de prueba en la carpeta docs/ (puedes usar el que ya viene por defecto).

## Ejecuta la aplicación:

```bash
python app.py
```

## 🛠️ Personalización

Puedes personalizar el visor PDF.js: para ocultar o mostrar ciertos botones, modifica este bloque en el archivo viewer.js.

```bash
_app.PDFViewerApplication.run(config);

// ✅ Aquí colocas tu lógica para ocultar botones
const ButtonsToHide = [
  "openFile",             // Abrir archivo
  "viewBookmark",         // Ver marcador
  "editorStamp",          // Editor de sellos
  "editorFreeText",       // Editor de texto libre
  "editorInk",            // Editor de tinta
  "secondaryToolbarToggle", // Barra de herramientas secundaria
  "sidebarToggle",        // Barra lateral
  "viewFind",             // Buscar
  // Añade más IDs si los necesitas
];

function hideButtonsById(ids) {
  ids.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.add("hide-button");
  });
}

hideButtonsById(ButtonsToHide);

```

## 🧠 ¿Cómo funciona internamente?

- El visor **PDF.js** se carga desde un archivo local `viewer.html` usando `QWebEngineView`.
- Se inyecta el PDF mediante una URL con parámetros `file://`.
- Los botones personalizados (**Imprimir, Descargar**) están enlazados con métodos **PySide6**.
- La impresión se maneja directamente vía `win32print`, permitiendo control sobre el spooler de Windows.
- Las descargas se controlan con un `QFileDialog` moderno.

## 📜 Licencia

Este proyecto está basado en [PDF.js](https://mozilla.github.io/pdf.js/), desarrollado por Mozilla y licenciado bajo **Apache License 2.0** cumpliendo con sus términos de uso y redistribución.

Modificaciones realizadas por **Zerous12 (2025)** para su integración con PySide6.

## 🤝 Contribuciones
¿Encontraste un error o quieres mejorar esta herramienta? ¡Pull requests y sugerencias son bienvenidas!  
Este proyecto existe para ayudar a otros devs **Qt/PySide** como tú.

Si te sirvió este proyecto, considera dejar una ⭐ en el repositorio o compartirlo con otros desarrolladores.

---

## 🙋‍♂️ Autor & Contacto

**Zerous12**  
Estudiante de Ingeniería Informática · Automatización · PySide6 · Electrónica aplicada  
📧 [Zerous_12@hotmail.com](mailto:Zerous_12@hotmail.com)  
🔗 [github.com/Zerous12](https://github.com/Zerous12)

---
