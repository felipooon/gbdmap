# 🦅 Radar GBD Chile en Vivo

Un visor web interactivo diseñado para seguir en tiempo real el progreso de los observadores de aves en Chile durante el Global Big Day (GBD). 

Este mapa consume datos públicos directamente desde la API de eBird, transformándolos en una interfaz visual optimizada para su uso en terreno desde dispositivos móviles.

## ✨ Características
* **Tiempo Real:** Actualización automática de listas y especies cada 5 minutos.
* **Filtros por Región:** Visualización focalizada desde Arica hasta Magallanes, o vista panorámica de todo el país.
* **Optimización en Terreno:** Diseño UI tipo "App Nativa" con alto contraste para lectura a plena luz del sol.
* **Escudo de Privacidad:** Filtrado automático para proteger y omitir observadores anónimos.

## 🛠️ Stack Tecnológico
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Leaflet.js (Mapas).
* **Hosting Frontend:** GitHub Pages.
* **Backend / Proxy:** Servidor intermediario en Python/Django (alojado en Render) para caché y protección de API Keys de eBird.

## 🚀 Uso
Simplemente selecciona tu región en el menú desplegable y el mapa cargará los últimos registros del día. Puedes buscar observadores específicos y hacer clic en el botón para ir directamente a la lista oficial en eBird.

---
*Desarrollado para la comunidad pajarera.*
