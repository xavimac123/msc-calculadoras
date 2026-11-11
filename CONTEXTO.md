# ARCHIVO MAESTRO DE CONTEXTO · MSC Gestor Legal

Actualizado: 2026-11-10.

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
1. Aviso «Todos los derechos reservados» y archivo LICENSE.
2. Traslado a Cloudflare Pages con Access; volver privado el repositorio; agregar el dominio nuevo al cliente OAuth de Google.
3. Tras el traslado, actualizar en MSC PD la dirección de Gestor Legal (Ajustes).

## 5. Flujo de trabajo
Editar `fuente/index.html` › `python build_pwa.py` › probar en 390 px y 1200 px › commit en español en `main` (GitHub Pages publica `/docs`).

## 6. Sesión en curso (2026-11-11) · retomar desde aquí
Pedido: (1) Inicio interactivo: saludo, fecha/hora, clima con ubicación, resumen, herramientas a la mano, casillero judicial de pendientes, detección de correos de Función Judicial/Fiscalía vía Gmail; (2) reparar botones sin acción; (3) formato USD con centavos en todo valor de dinero; (4) corregir tasa de éxito (valor estimado no se contabiliza) y verificar rubros; (5) actualizar interfaz y diseño; licencia.
Hallazgos:
- Auditoría automática (Playwright, 390 px): todos los botones tienen manejador. Los «sin acción» son de retroalimentación invisible (mensaje fuera de pantalla, p. ej. Restablecer plantilla, Guardar audiencia con validación).
- Tasa de éxito: los campos `type=number` leen «10.000» como 10 (punto de miles) → prima casi cero. Además, con cuantía indeterminada en materias de prima fija se oculta el valor estimado.
- Gmail: remitentes reales `sender.satje@funcionjudicial.gob.ec`, `satje.guayas@funcionjudicial.gob.ec`; excluir `Escuela.Judicial@`. Fiscalía: dominio `fiscalia.gob.ec`.
- `fusionar0` descarta claves no listadas: toda colección nueva del registro debe agregarse allí.
Herramientas de prueba en la sesión: /home/claude/tools (audit_*.py).
Estado: [ ] moneda [ ] tasa de éxito [ ] inicio [ ] Gmail/casillero [ ] retroalimentación botones [ ] diseño [ ] LICENSE
