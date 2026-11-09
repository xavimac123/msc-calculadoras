# MSC · Calculadoras legales

Herramienta de uso interno de **Macías Sánchez Consultores** (Guayaquil, Ecuador). App web instalable en el teléfono (PWA) que funciona sin internet.

**Abrir / instalar:** https://xavimac123.github.io/msc-calculadoras/

## Qué incluye
- **Honorarios – procesos y trámites:** honorario operativo + prima de éxito (sin éxito, parcial 50 %, total 100 %), IVA 15 %, retenciones, descuentos, plan de pago y ganancia neta.
- **Honorarios – consultas:** tarifa por complejidad (baja fija, media, alta con techo), tiempo, materia y modalidad; documentos a pedir al cliente; mensaje e imagen de confirmación para WhatsApp.
- **Clientes y casos:** registro cifrado con contraseña (AES-GCM 256, PBKDF2-SHA256), clave de recuperación, casos vinculados a cada cliente, vista por mes (vigentes, nuevos, cerrados, por concretar), llamadas pendientes en rojo y enlaces a Google Calendar. Sincronización opcional con la carpeta oculta de Google Drive (`drive.appdata`), con una versión diaria (10 días) y una mensual (12 meses). Ni el repositorio ni Google reciben los datos sin cifrar.
- **Audiencias:** registro por caso con fecha, hora, tipo, modalidad (presencial o telemática), dependencia (Florida, Sur Valdivia, Albán Borja, Fiscalía Montecristi, Fiscalía La Merced u otra), juez, secretario, causa y materia; vistas de próximas, mes (calendario) y día, con filtros.
- **Configuración:** apariencia (claro, oscuro, automático), Google Drive, contraseña, respaldo manual y datos del despacho (cuentas, firma, logo).
- **Proforma:** cliente tomado del registro, servicios del catálogo, etapas de pago según el tipo de procedimiento (COGEP, COIP, COA), forma de pago (pago total −10 %, hasta 3 cuotas o por etapas), retenciones estimadas, cuentas bancarias y firma; exporta PDF y Word y se comparte por WhatsApp o correo. Numeración PRF-AAAA-NNN por dispositivo.
- **Catálogo de servicios:** códigos por materia (FAM-01, IESS-03, FIS-01…), descripción para factura, IVA y exportación CSV para Excel o el sistema de facturación.
- **Pensiones alimenticias:** Tabla de Pensiones Alimenticias Mínimas 2026 (Acuerdo MDH-DM-2026-0005-A, SBU $482); se puede cargar la tabla de otro año.
- **Plazos y términos:** COGEP, COA y COIP, con feriados nacionales 2026 y 2027.
- **Tránsito:** notificación de la boleta en 72 horas (art. 179 LOTTTSV) e impugnación en 3 días (art. 644 COIP).

## Instalación
- **Android (Chrome):** abrir el enlace → menú ⋮ → *Instalar app*.
- **iPhone (Safari):** abrir el enlace → Compartir → *Agregar a pantalla de inicio*.
Ábrala una vez con internet; después funciona sin conexión.

## Privacidad
El repositorio no contiene datos de clientes. El registro de clientes se guarda cifrado en el teléfono y, si se activa, cifrado en Google Drive; la contraseña nunca sale del dispositivo. Las cuentas bancarias, parámetros y tablas quedan en el teléfono. El ID de cliente de Google OAuth incluido en el código es público por diseño; no se usa ningún secreto.

## Mantenimiento
- Código fuente: `fuente/index.html` (es la misma página que la versión en claude.ai).
- Generar la versión instalable: `python3 build_pwa.py` (escribe en `docs/`, que es lo que publica GitHub Pages).
- Valores que cambian cada año: SBU, tabla de pensiones, feriados, IVA y retenciones. Están en el bloque `data` de `fuente/index.html`.

## Aviso
Resultados referenciales. Verifique la norma vigente y el caso concreto antes de actuar. Valores de honorarios y parámetros de consulta: criterio propio.
