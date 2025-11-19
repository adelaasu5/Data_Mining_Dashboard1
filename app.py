import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la Página
st.set_page_config(
    page_title="Dashboard Analítico Universitario",
    layout="wide"
)

# Título del Dashboard
st.title("📊 Análisis de Admisión, Retención y Satisfacción Estudiantil")
st.markdown("Este dashboard ofrece una visión dinámica de las métricas clave de la Universidad.")

# 2. Carga de Datos
# Asumiendo que 'university_student_data.csv' está en el mismo directorio
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    # Crear una columna de 'Departamento' para facilitar el análisis
    department_cols = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
    df['Total Departmental Enrollment'] = df[department_cols].sum(axis=1)
    return df

df = load_data('university_student_data.csv')

# 3. Sidebar y Filtros Interactivos
st.sidebar.header("Filtros de Análisis")

# Filtro de Año
selected_years = st.sidebar.multiselect(
    "Seleccionar Año(s):",
    options=df['Year'].unique().tolist(),
    default=df['Year'].unique().tolist()
)

# Filtro de Período (Term)
selected_terms = st.sidebar.multiselect(
    "Seleccionar Período Académico (Term):",
    options=df['Term'].unique().tolist(),
    default=df['Term'].unique().tolist()
)

# Aplicar los filtros
df_filtered = df[df['Year'].isin(selected_years) & df['Term'].isin(selected_terms)]

# 4. KPI Card (Métrica) - Total Enrolled
total_enrolled = df_filtered['Enrolled'].sum()

st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Matriculados (Filtro Aplicado)", value=f"{total_enrolled:,}")

# 5. Visualización 1: Tendencia de Retención por Año (Line Chart)
retention_data = df_filtered.groupby(['Year', 'Term'])['Retention Rate (%)'].mean().reset_index()

st.subheader("1. Tasa de Retención (%) por Año y Período")
fig_retention = px.line(
    retention_data,
    x='Year',
    y='Retention Rate (%)',
    color='Term',
    markers=True,
    title="Tendencia de Tasa de Retención",
    labels={'Retention Rate (%)': 'Tasa de Retención (%)', 'Year': 'Año'}
)
st.plotly_chart(fig_retention, use_container_width=True)

# 6. Matrícula por Departamento (Bar Chart)
# Derretir/Transformar los datos para Plotly
department_cols = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
df_departments = df_filtered.melt(
    id_vars=['Year', 'Term'],
    value_vars=department_cols,
    var_name='Department',
    value_name='Enrolled_Count'
)

# Agrupar por Departamento para el Bar Chart
department_summary = df_departments.groupby('Department')['Enrolled_Count'].sum().reset_index()
department_summary['Department'] = department_summary['Department'].str.replace(' Enrolled', '')

st.subheader("2. Matrícula Agregada por Departamento")
fig_dept = px.bar(
    department_summary.sort_values(by='Enrolled_Count', ascending=False),
    x='Department',
    y='Enrolled_Count',
    color='Department',
    title=f"Distribución de Matrícula Total ({len(selected_years)} Años, {len(selected_terms)} Períodos)",
    labels={'Enrolled_Count': 'Total Estudiantes Matriculados', 'Department': 'Departamento'}
)
st.plotly_chart(fig_dept, use_container_width=True)
