import streamlit as st
from flask import Flask
app = Flask(__name__)


# Configuración de la página
st.set_page_config(page_title="Gestor de Servicios", page_icon="🌐", layout="centered")

# Estilo personalizado
st.markdown("""
    <style>
    /* Fuente y colores globales */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f8f9fa;
        color: #212529;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #0056b3; /* Azul corporativo */
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
        color: #6c757d;
    }
    .instructions {
        font-size: 1rem;
        text-align: justify; /* Justificar texto */
        margin: 0 auto;
        max-width: 700px;
        color: #212529;
        line-height: 1.6;
    }
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }
    .stButton button {
        background-color: #0056b3; /* Azul corporativo */
        color: white;
        border-radius: 12px;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 0.8rem 2rem;
        border: none;
        transition: background-color 0.3s, transform 0.2s;
    }
    .stButton button:hover {
        background-color: #004494; /* Azul más oscuro */
        transform: scale(1.05);
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        font-size: 0.9rem;
        color: #6c757d;
    }
    .footer a {
        color: #0056b3;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .language-selector {
        text-align: right;
        margin-bottom: 1rem;
    }
    .language-selector select {
        font-size: 1rem;
        padding: 0.5rem;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Idiomas disponibles
languages = {
    "es": {
        "title": "Gestor de Servicios",
        "subtitle": "Bienvenidos",
        "instructions": """
            Iniciaremos el proceso para crear la <strong>propuesta de valor</strong> del potencial cliente. <br><br>
            Para generar el cuestionario o calcular el precio sugerido, comience con el paso uno: <strong>Crear el Formulario de Servicios</strong>. <br><br>
            Este proceso rápido generará un documento Excel que le permitirá construir una <strong>propuesta comercial</strong> y 
            el <strong>cuestionario sugerido</strong> basado en los servicios contratados.
        """,
        "button1": "📋 Crear Formulario de Servicios",
        "button2": "📝 Crear Cuestionario",
        "button3": "💰 Identificar el Coste",
        "footer": "Visita nuestro sitio web oficial en <a href='https://www.mygosupply.com/es/' target='_blank'>GoSupply</a>."
    },
    "en": {
        "title": "Service Manager",
        "subtitle": "Welcome",
        "instructions": """
            We will begin the process of creating the <strong>value proposition</strong> for the potential client. <br><br>
            To generate the questionnaire or calculate the suggested price, start with step one: <strong>Create the Service Form</strong>. <br><br>
            This quick process will generate an Excel document that will allow you to build a <strong>commercial proposal</strong> and 
            the <strong>suggested questionnaire</strong> based on the contracted services.
        """,
        "button1": "📋 Create Service Form",
        "button2": "📝 Create Questionnaire",
        "button3": "💰 Identify the Cost",
        "footer": "Visit our official website at <a href='https://www.mygosupply.com/en/' target='_blank'>GoSupply</a>."
    }
}

# Selección de idioma
selected_language = st.selectbox("Seleccione un idioma / Select a language:", ["es", "en"], index=0)
texts = languages[selected_language]

# Título principal y subtítulo
st.markdown(f'<div class="main-title">{texts["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">{texts["subtitle"]}</div>', unsafe_allow_html=True)

# Instrucciones
st.markdown(f'<div class="instructions">{texts["instructions"]}</div>', unsafe_allow_html=True)

# Botones principales con enlaces
st.markdown('<div class="button-container">', unsafe_allow_html=True)

st.markdown(f"""
    <a href="https://formulario-qvdv.onrender.com/" target="_blank">
        <button>{texts["button1"]}</button>
    </a>
""", unsafe_allow_html=True)

st.markdown(f"""
    <a href="https://generador-cuestionario.onrender.com/" target="_blank">
        <button>{texts["button2"]}</button>
    </a>
""", unsafe_allow_html=True)

st.markdown(f"""
    <a href="https://calculadora-s44w.onrender.com/" target="_blank">
        <button>{texts["button3"]}</button>
    </a>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown(f"""
    <div class="footer">
        <p>{texts["footer"]}</p>
    </div>
""", unsafe_allow_html=True)
