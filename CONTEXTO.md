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
- Repositorio público (ya con licencia de uso privativo): contenido y tarifas siguen a la vista hasta volverlo privado.
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

## 7. Revisión normativa (2026-11-11, con los textos del proyecto)
- **Plazos (`PRE`):** corregido completar demanda a 5 días (COGEP 146). Agregados: niñez 10 días (333.3), audiencia niñez 20 días desde citación (333.4), prueba nueva (151), subsanar defecto (295.2), audiencia de juicio (297), apelación niñez 5 (257), contestar apelación (258), recurso de hecho 3 (280), contestar casación (270), COIP apelación 3 (654), casación 5 hábiles (657), archivo (587), investigación previa 1–2 años (585), LOGJCC apelación 3 (24) y AEP 20 (60), CT prescripción 3 años (635), 1 mes (636), cambio de ocupación 60 días (192). Cada grupo tiene `c` (código) para la etiqueta «Base».
- **Plantillas:** demanda con RUC opcional, sección de documentos (art. 143) y procedimiento con su artículo; fundamentos actualizados (alimentos CONA innumerados + COGEP 332.3; divorcio CC 110/124 + 332.4; reivindicación 933 + 289 + inscripción 146; prescripción 2392/2398/2410/2411 + precedente CNJ 7-2025; monitorio 356-358; laboral CT 188/185/635 + 332.1); contestación con arts. 151-153. Nuevas: apelación (256-258) e impugnación de boleta (COIP 644).
- **Tipos de causa (`CAUSAS`):** 34 causas de familia, civil, cartera, laboral, penal, tránsito y constitucional con su fundamento; selector «Tipo de causa» en el caso (campo `tc`), recuadro de fundamento y nombre en la lista de casos.
- **Interfaz:** ficha de cliente con encabezado y accesos (ver casos, nuevo caso, proforma, WhatsApp); buscador de cliente de la proforma a ancho completo; barra fija en Honorarios con «cliente paga» y «ganancia neta».
- Pendiente de verificar fuera del proyecto: Ley de Inquilinato (no está en los documentos); COIP apelación y archivo marcados «verificar» por el cómputo de días.

## 8. Calculadora laboral (2026-11-11) · Calculadoras › Laboral (`#calc-lab`, `renderLab`)
- Liquidación por 14 modos de terminación y 10 tipos de contrato: sueldo pendiente, horas (art. 55), décimos proporcionales (111, 113; Costa 1-mar / Sierra 1-ago; d13 desde 1-dic), vacaciones proporcionales y no gozadas con antigüedad y recargo del art. 74, fondos de reserva (196), utilidades; indemnización 188 (mín. 3, máx. 25 meses, fracción = año), bonificación 185 (25 % proporcional), ineficaz y discriminación +12 meses (195.3), discapacidad +18 meses (LOD, marcar verificar), abandono −15 días (190), cierre (193), visto bueno del trabajador (191). Deducciones: IESS 9,45 % sobre haberes pendientes y anticipos.
- Validaciones por contrato: prueba >90 días (15 en hogar) = despido; eventual >180; ocasional >30; recargo 35 %; aprendiz 80 % y plazo; temporada; sueldo < SBU; jubilación patronal 20-25 y 25+ años.
- Plazos: pago y acta en SUT 15 días, consignación hasta día 30 (AM MDT-2023-140 reformado por AM MDT-2025-053, días calendario); desde el día 16 denuncia MDT; desde el día 31 demanda sumaria; ineficaz 30 días (195.2); prescripción 3 años (635/637).
- Visto bueno: notificación 24 h, contestación 2 días, resolución al tercer día (621), suspensión con consignación de un mes (622), prescripción de un mes para el empleador (636).
- Comparativa de neto por modo y botón de resumen / WhatsApp.

## 9. Consultas: aceptada vs. propuesta (2026-11-11)
- Selector «Estado de la consulta» (`CN.est`: `ok` aceptada/agendada, `prop` propuesta por confirmar), guardado en `store('cons')`.
- Propuesta: oculta fecha, hora, lugar y modalidad; muestra «fecha y modalidad por acordar» con dos opciones: presencial tarifa normal y virtual con descuento (ahorro). `cotiz(mod)` acepta la modalidad.
- Mensaje de WhatsApp e imagen: el valor con IVA va grande («IVA incluido») y el valor sin IVA + IVA en letra pequeña; la propuesta muestra ambas modalidades.

## 10. Laboral: vacaciones, fondos, utilidades y demanda (2026-11-11)
- Nuevos campos: meses de sueldo impagos, vacaciones gozadas no pagadas (art. 69 inc. 2), afiliación al IESS.
- Fondos de reserva automáticos: meses con derecho = meses de servicio − 12; modos mensual / IESS / no pagados / parcial; no afiliado: 6 % anual (art. 202).
- Utilidades del último ejercicio cerrado: 10 % / trabajadores × días/365 + 5 % × cargas/total cargas; tope 24 SBU (97.1, aviso); vencen 15-abr (105); aviso de proporcional del año en curso.
- Bloque «Si se demanda» (`R.dem`): triple art. 94 sobre remuneraciones impagas del último trimestre (no indemnizaciones), 50 % fondos (202), 10 % reintegro ineficaz (195.3), intereses utilidades (104), diferencias SBU, falta de afiliación (COIP 243-244), jubilación; total a demandar = neto + adicionales.
- La fuente de la calculadora está en el bloque `CALCULADORA LABORAL` de index.html (copia de trabajo en /home/claude/tools/laboral.js en la sesión).

## 11. Siguiente
1. Habilitar Gmail API y permiso gmail.readonly; probar «Revisar Gmail» en la app instalada.
2. Traslado a Cloudflare Pages con Access; volver privado el repositorio.
