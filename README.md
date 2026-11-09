# MSC · Calculadoras legales

Herramienta de uso interno de **Macías Sánchez Consultores** (Guayaquil, Ecuador). App web instalable en el teléfono (PWA) que funciona sin internet.

**Abrir / instalar:** https://xavimac123.github.io/msc-calculadoras/

## Qué incluye
- **Honorarios – procesos y trámites:** honorario operativo + prima de éxito (sin éxito, parcial 50 %, total 100 %), IVA 15 %, retenciones, descuentos, plan de pago y ganancia neta.
- **Honorarios – consultas:** tarifa por complejidad (baja fija, media, alta con techo), tiempo, materia y modalidad; documentos a pedir al cliente; mensaje e imagen de confirmación para WhatsApp.
- **Clientes y casos:** registro cifrado con contraseña (AES-GCM 256, PBKDF2-SHA256), clave de recuperación, casos vinculados a cada cliente, vista por mes (casos del mes y, debajo, inactivos y sin concretar para seguimiento; CSV al final), llamadas pendientes en rojo y enlaces a Google Calendar. Sincronización opcional con la carpeta oculta de Google Drive (`drive.appdata`), con una versión diaria (10 días) y una mensual (12 meses). Ni el repositorio ni Google reciben los datos sin cifrar.
- **Audiencias:** registro por caso con fecha, hora, tipo, modalidad (presencial o telemática), dependencia (Unidad Judicial Florida Norte (Norte 1), Unidad Judicial Valdivia Sur, Unidad Judicial Albán Borja (Norte 2), Fiscalía Montecrísti, Fiscalía La Merced u otra, normalmente fuera de la ciudad), juez, secretario, causa y materia; vistas de próximas, mes (calendario) y día, con filtros. Opcional: agenda automática en Google Calendar (`calendar.events`) con recordatorios 7 y 3 días antes; el evento se actualiza o se elimina con la audiencia.
- **Configuración:** apariencia (claro, oscuro, automático), Google Drive, contraseña, respaldo manual y datos del despacho (cuentas, firma, logo).
- **Proforma:** lista de clientes oculta hasta pulsar "Visualizar" (Código – NOMBRES – CÉDULA – CONTACTO – CORREO), servicios del catálogo con valor único u honorarios operativos + prima de éxito (contingente, no se suma al total), tasa notarial por trámite, duración tentativa (días, meses o años), cláusula de contrato de servicios cuando los honorarios superan $500,00. Forma de pago: pago total con descuento editable (10 % por defecto), cuotas (mínimo 3, ampliables) o etapas según el procedimiento (COGEP, COIP, COA) con valor en dólares, agregar y reordenar. Gastos operativos estimados se muestran sin sumarse al total. Exporta PDF y Word y se comparte por WhatsApp o correo. Numeración PRF-AAAA-NNN.
- **Catálogo de servicios:** códigos por materia (FAM-01, CIV-05, TRA-04…), procedimiento del COGEP/COIP/COA de cada servicio (define las etapas de pago), descripción para factura, IVA y exportación CSV. Civil por servicios (reivindicación, herencias, posesión efectiva, inquilinato, contratos, gestión notarial con tabla de tasas notariales de referencia). Penal-Tránsito. Protección de datos con los servicios S01 a S28 del portafolio DPD (precios por tamaño de empresa: criterio propio). Gastos operativos: los paga el cliente y no forman parte de los honorarios.
- **Pensiones alimenticias:** Tabla 2026 (Acuerdo MDH-DM-2026-0005-A, SBU $482). Se registra cada hijo con su edad (0 a 2 años o 3 en adelante) y grado de discapacidad; calcula el porcentaje por número de hijos, el reparto por hijo y el adicional por discapacidad (por hogar, el de mayor grado). La tabla de otro año se carga con todas sus columnas, incluida discapacidad.
- **Plazos y términos:** COGEP, COA y COIP, con feriados nacionales 2026 y 2027.
- **Penal-Tránsito (calculadora):** notificación de la boleta en 72 horas (art. 179 LOTTTSV) e impugnación en 3 días (art. 644 COIP).

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
