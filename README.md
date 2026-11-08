# MSC · Calculadoras legales

Herramienta de uso interno de **Macías Sánchez Consultores** (Guayaquil, Ecuador). App web instalable en el teléfono (PWA) que funciona sin internet.

**Abrir / instalar:** https://xavimac123.github.io/msc-calculadoras/

## Qué incluye
- **Honorarios – procesos y trámites:** honorario operativo + prima de éxito (sin éxito, parcial 50 %, total 100 %), IVA 15 %, retenciones, descuentos, plan de pago y ganancia neta.
- **Honorarios – consultas:** tarifa por complejidad (baja fija, media, alta con techo), tiempo, materia y modalidad; documentos a pedir al cliente; mensaje e imagen de confirmación para WhatsApp.
- **Pensiones alimenticias:** Tabla de Pensiones Alimenticias Mínimas 2026 (Acuerdo MDH-DM-2026-0005-A, SBU $482); se puede cargar la tabla de otro año.
- **Plazos y términos:** COGEP, COA y COIP, con feriados nacionales 2026 y 2027.
- **Tránsito:** notificación de la boleta en 72 horas (art. 179 LOTTTSV) e impugnación en 3 días (art. 644 COIP).

## Instalación
- **Android (Chrome):** abrir el enlace → menú ⋮ → *Instalar app*.
- **iPhone (Safari):** abrir el enlace → Compartir → *Agregar a pantalla de inicio*.
Ábrala una vez con internet; después funciona sin conexión.

## Privacidad
El repositorio no contiene datos de clientes. Las cuentas bancarias, parámetros y tablas que se guarden en la app quedan **solo en el teléfono** (almacenamiento local del navegador).

## Mantenimiento
- Código fuente: `fuente/index.html` (es la misma página que la versión en claude.ai).
- Generar la versión instalable: `python3 build_pwa.py` (escribe en `docs/`, que es lo que publica GitHub Pages).
- Valores que cambian cada año: SBU, tabla de pensiones, feriados, IVA y retenciones. Están en el bloque `data` de `fuente/index.html`.

## Aviso
Resultados referenciales. Verifique la norma vigente y el caso concreto antes de actuar. Valores de honorarios y parámetros de consulta: criterio propio.
