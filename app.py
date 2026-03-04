import streamlit as st

def render_landing():
    # URL de tu imagen en GitHub (Reemplaza con tu link Raw)
    IMG_URL = "https://github.com/jorgeolmosTN/veep-fi/blob/5a80393b3b059c16fe6fa1335c3bc1e238776758/assets/image_44a13a.png"

    st.markdown(f"""
        <style>
        /* Fondo de pantalla completa */
        .stApp {{
            background-image: url("{IMG_URL}");
            background-size: cover;
            background-position: center;
        }}

        /* Contenedor principal para organizar Welcome y Login */
        .main-container {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            height: 80vh;
            padding: 50px;
        }}

        /* Texto Welcome abajo a la izquierda */
        .welcome-text {{
            color: white;
            font-size: 80px;
            font-weight: bold;
            font-family: sans-serif;
            margin-bottom: 20px;
        }}

        /* Caja de Login abajo a la derecha */
        .login-box {{
            background: rgba(0, 0, 0, 0.4); /* Fondo oscuro traslúcido */
            padding: 20px;
            border-radius: 10px;
            width: 300px;
        }}

        /* Estilo para etiquetas de texto de Streamlit dentro del login */
        .stTextInput label {{
            color: white !important;
            font-weight: bold !important;
            text-transform: uppercase;
            font-size: 12px;
        }}
        
        /* Ocultar elementos innecesarios de la landing */
        [data-testid="stHeader"], [data-testid="stFooter"] {{
            visibility: hidden;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Estructura de la página
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown('<div class="welcome-text">welcome</div>', unsafe_allow_html=True)

    with col_right:
        # Usamos un formulario para que se vea como una caja compacta
        with st.container():
            st.markdown('<div class="login-box">', unsafe_allow_html=True)
            user = st.text_input("USER", placeholder="Introduce tu usuario", key="l_user")
            password = st.text_input("PASS", type="password", placeholder="••••••••", key="l_pass")
            
            if st.button("INGRESAR", use_container_width=True):
                if user == "admin" and password == "1234": # Ejemplo simple
                    st.success("¡Bienvenido!")
                    st.session_state.seccion_activa = "Transporte"
                    st.rerun()
                else:
                    st.error("Credenciales inválidas")
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
