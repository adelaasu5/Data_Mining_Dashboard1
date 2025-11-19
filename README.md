# Dashboard Analítico Universitario

Este repositorio contiene los archivos necesarios para el despliegue de un dashboard analítico en Streamlit Cloud, el proyecto busca proporcionar una visión dinámica y profunda sobre los procesos de admisión, matrícula, retención y satisfacción estudiantil en la universidad.

## Propósito
El objetivo principal es transformar datos crudos en *insights* accionables, utilizando visualizaciones interactivas para apoyar la toma de decisiones informada por datos (Data-Driven Decision Making).

## Contenido del Repositorio
1.  **`app.py`**: El código principal de la aplicación Streamlit, incluye la carga de datos, la lógica de filtrado y las visualizaciones dinámicas (KPI, Gráfico de Líneas, Gráfico de Barras).
2.  **`requirements.txt`**: Lista de dependencias de Python (`pandas`, `streamlit`, `plotly`) para que Streamlit Cloud pueda instalar y ejecutar la aplicación.
3.  **`university_student_data.csv`**: El dataset original utilizado para el análisis.

## Instrucciones de Despliegue (Streamlit Cloud)
Para desplegar el dashboard, sigue estos pasos:
1.  Asegúrate de que `app.py`, `requirements.txt` y `university_student_data.csv` estén en la raíz de este repositorio.
2.  Inicia sesión en Streamlit Cloud.
3.  Selecciona "New app" y conecta con este repositorio de GitHub.
4.  Asegúrate de que la rama sea la correcta y que el archivo principal sea `app.py`.
5.  Haz clic en "Deploy"
