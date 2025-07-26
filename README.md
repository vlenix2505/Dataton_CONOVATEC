# Análisis de Prestaciones de salud para pacientes con diabetes (SIS)

## 📌 Descripción del proyecto

Este proyecto explora de manera integral las **prestaciones de salud** brindadas a pacientes con diagnóstico de **diabetes mellitus afiliados al Seguro Integral de Salud (SIS)** en Perú. Usamos el conjunto de datos abierto del SIS que registra atenciones médicas, medicamentos y procedimientos desde 2018 [Prestaciones de salud asociadas a los asegurados con Diabetes Mellitus](https://datosabiertos.gob.pe/dataset/prestaciones-de-salud-asociadas-los-asegurados-con-diabetes-mellitus-sis) para analizar cómo se atiende esta enfermedad crónica en la población asegurada.

El propósito es **generar información procesable usando análisis de datos** para mejorar la atención médica, apoyando tanto a comunidades vulnerables como a tomadores de decisiones en salud pública.

Actualmente, el procesamiento y análisis de datos se está desarrollando en **Microsoft Fabric Notebooks utilizando PySpark** para manejar de manera eficiente más de 40 millones de registros, garantizando escalabilidad y reproducibilidad.

## 🎯 Objetivos del proyecto

- **Describir tendencias de atención:** analizar la evolución de consultas, procedimientos y medicaciones para pacientes diabéticos a lo largo del tiempo y por regiones.
- **Identificar brechas y patrones:** detectar desigualdades geográficas o demográficas en el acceso a servicios (por edad, género o zona) y necesidades no cubiertas.
- **Visualizar datos de forma accesible:** generar gráficos y mapas claros que faciliten la interpretación para tomadores de decisiones y público general.
- **Proponer recomendaciones:** traducir hallazgos en recomendaciones prácticas para optimizar recursos (programas de prevención, campañas de tamizaje, dotación de insumos, etc.).

## 🚨 Problemática

La **diabetes mellitus** es altamente prevalente en Perú, afectando aproximadamente al 5.5% de adultos (~1.3 millones de personas). Es una de las principales causas de complicaciones graves y mortalidad, afectando especialmente a poblaciones con limitado acceso a servicios de salud.

El SIS, que cubre a más de 26.3 millones de peruanos (71% de la población asegurada), brinda cobertura gratuita a pacientes con diabetes, pero dada la magnitud del problema, es fundamental mejorar la eficiencia en el uso de recursos, monitorear brechas de atención y optimizar la planificación de intervenciones preventivas y de tratamiento.

Este proyecto aborda esta problemática aprovechando **datos abiertos para generar soluciones basadas en evidencia** que contribuyan a fortalecer la salud pública.

## 🛠️ Estructura de la solución

1. **Definición del problema y objetivos**.
2. **Recolección e integración de datos SIS 2022–2023 (40M registros)**.
3. **Tratamiento y limpieza de datos en PySpark:**
   - Estandarización de fechas.
   - Imputación de nulos relevantes.
   - Conversión de tipos de datos.
   - Detección de duplicados y consistencia.
4. **Análisis exploratorio de datos (EDA):**
   - Patrones de atenciones por región, género y edad.
   - Análisis de continuidad de controles.
   - Identificación de brechas de acceso.
5. **Visualización en Power BI para insights interactivos.**
6. **Recomendaciones de intervenciones basadas en datos.**

## 👥 Población involucrada y beneficiada

- **Base analizada:** +40 millones de registros de prestaciones 2022–2023.
- **Potencialmente beneficiados:**
  - +200,000 pacientes afiliados al SIS con diagnóstico de diabetes.
  - Tomadores de decisiones (Minsa y SIS).
  - Profesionales de salud y gestores públicos.
  - Ciudadanía e investigadores mediante publicaciones abiertas.

## 🧰 Herramientas y métodos utilizados

- **Lenguaje:** PySpark (Python) para ETL y limpieza.
- **EDA:** pandas, matplotlib, seaborn.
- **Entornos reproducibles:** Microsoft Fabric Notebooks con PySpark para escalabilidad y colaboración.
- **Visualización:** Power BI.
- **Metodología:** CRISP-DM para estructuración del proyecto.

## 🔄 Proceso de selección y tratamiento de datos

✅ **Carga y procesamiento con PySpark** para datasets de gran volumen.  
✅ Validación de claves de afiliado, establecimiento y prestaciones.  
✅ Limpieza de:
- Fechas (`string` ➔ `TimestampType` estandarizado).
- Imputación de nulos relevantes (`VALOR_NETO`, fechas de fallecimiento, etc.).
- Eliminación de registros inconsistentes.
  ✅ Reparticionamiento y optimización del dataset para Spark.  
  ✅ Análisis de calidad de datos:
- Nulos por columna y fila.
- Distribución de valores y detección de outliers.
  ✅ Exportación de subconjuntos limpios para Power BI.

## 🚀 Valor agregado de la propuesta

- **Información procesable para decisiones de salud pública:** identifica zonas y poblaciones con baja cobertura para priorizar recursos y estrategias.
- **Monitoreo de equidad en salud:** permite evaluar diferencias en atención según región y demografía, apoyando la asignación justa de recursos.
- **Transparencia y rendición de cuentas:** uso de datos abiertos y publicación de resultados de forma accesible, empoderando a la sociedad civil.
- **Escalabilidad técnica:** la metodología puede aplicarse a otras enfermedades o conjuntos de datos del sector salud.
- **Impacto social tangible:** contribuye a mejorar la calidad de vida de las personas con diabetes y a reducir complicaciones y costos asociados, fortaleciendo la salud pública mediante el uso de datos abiertos.

---

🔗 **Repositorio y avances:** este proyecto se encuentra en desarrollo y actualización constante, documentado para facilitar su revisión y colaboración.
