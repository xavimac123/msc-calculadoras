# ARCHIVO MAESTRO DE CONTEXTO · MSC Gestor Legal

Actualizado: 2026-11-11.

## 1. Identidad y propósito
- **Qué es:** app instalable (PWA) de gestión del despacho Macías Sánchez Consultores: calculadoras legales, honorarios, proforma, registro de clientes y casos, y agenda de audiencias.
- **Usuario:** Abg. Mariano X. Macías Sánchez (Guayaquil). Uso interno del despacho.
- **Stack:** HTML, CSS y JavaScript sin frameworks, en un solo archivo; compilación con Python. Sin dependencias externas por CDN.
- **Publicación actual:** GitHub Pages desde `main`, carpeta `/docs` › `https://xavimac123.github.io/msc-gestorlegal/`. Destino previsto: Cloudflare Pages con Cloudflare Access.
- **Reglas clave:** nunca datos reales de clientes en el repositorio; español de Ecuador, registro formal; commits descriptivos en español.

## 2. Estado arquitectónico
- `fuente/index.html`: toda la app. Los datos de catálogo, tarifas y feriados van en un bloque JSON dentro del archivo (`<script id="data">`).
- `build_pwa.py`: genera `docs/` (lo que se publica) con el service worker y el manifiesto.
- Datos: registro de clientes y casos cifrado en el dispositivo; copia cifrada en la carpeta oculta de Google Drive (`msc-…`); audiencias en Google Calendar. Mismo cliente OAuth que MSC Protección de Datos.
- Proforma: catálogo de servicios por código, exportación y envío por WhatsApp. Recibe servicios S01 a S28 desde MSC Protección de Datos por la clave `msc:pd-handoff` o por el enlace `#prf&pd=…`.

## 3. Bugs y bloqueos activos
- Sin errores conocidos en la app publicada.
- Repositorio público y sin licencia: contenido y tarifas a la vista.
- Los datos no migran solos al cambiar de dirección web (restaurar desde Drive).
- La versión publicada como página en claude.ai no tiene el último cambio de la proforma.

## 4. Backlog (orden de prioridad)
1. Traslado a Cloudflare Pages con Access; volver privado el repositorio; agregar el dominio nuevo al cliente OAuth de Google.
2. Tras el traslado, actualizar en MSC PD la dirección de Gestor Legal (Ajustes).

## 5. Flujo de trabajo
Editar `fuente/index.html` › `python build_pwa.py` › probar en 390 px y 1200 px › commit en español en `main` (GitHub Pages publica `/docs`).

## 6. Cambios del 2026-11-11 (completados)
- **Inicio** (pestaña por defecto): saludo, reloj en vivo, clima Open-Meteo (Guayaquil o ubicación autorizada, redondeada a 2 decimales y guardada solo en el dispositivo), foco del día, indicadores con montos USD, herramientas a la mano, próximas audiencias y enlaces (e-SATJE, Fiscalía SIAF).
- **Casillero judicial** (`R.data.casj`, cifrado y en `fusionar0`): fecha de notificación, causa, actuación, días de término/plazo, vencimiento con `computar()` y feriados, semáforo, vínculo automático al caso por Nº de causa.
- **Gmail** (`gmail.readonly`, token propio `tokenGm`): búsqueda configurable en Configuración; por defecto `sender.satje@` y `satje.guayas@funcionjudicial.gob.ec` y `fiscalia.gob.ec`, excluye la Escuela Judicial. Solo se guardan los ID revisados (`R.data.gm.vistos`). **Requisito pendiente del usuario:** habilitar Gmail API y agregar el permiso gmail.readonly en Google Cloud.
- **Montos USD:** todo campo cuyo rótulo dice «USD» (o `data-k` valor/exito) se convierte en campo de dinero con `$` y centavos (`monetiza`); `num()` entiende 1.500,25 / 1,500.25 / 1500.25.
- **Prima de éxito:** corregido el error del punto de miles; con cuantía indeterminada o de bienes se elige «% del valor estimado» o «monto fijo»; se muestra la fórmula.
- **Botones:** auditoría automática sin manejadores faltantes; los mensajes se llevan a la vista y se resaltan; «Restablecer plantilla» pide confirmación y avisa.
- **Licencia:** archivo `LICENSE` (uso privativo, todos los derechos reservados, COESCCI) y texto en Configuración y pie de página.
- Verificado: SBU 2026 = $482; IVA 15 %.

## 7. Siguiente
1. Habilitar Gmail API y permiso gmail.readonly; probar «Revisar Gmail» en la app instalada.
2. Traslado a Cloudflare Pages con Access; volver privado el repositorio.
3. Revisión de artículos citados en Plazos (COGEP/COIP) contra los textos del proyecto.
