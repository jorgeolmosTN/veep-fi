import streamlit as st

def render_landing():
    # REEMPLAZA ESTE LINK POR TU LINK RAW DE GITHUB
    IMG_URL = "https://raw.githubusercontent.com/tu_usuario/tu_repo/main/assets/fondo.png"

    st.markdown(f"""
        <style>
        /* Aplicar fondo a toda la app solo en esta sección */
        .stApp {{
            background-image: url("{IMG_URL}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* Contenedor del Login a la derecha */
        .login-wrapper {{
            display: flex;
            justify-content: flex-end;
            align-items: flex-end;
            height: 70vh;
            padding-right: 10%;
        }}

        .login-box {{
            background: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 15px;
            width: 320px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(5px); /* Efecto esmerilado */
        }}

        /* Estilo de los textos de entrada */
        .stTextInput label p {{
            color: white !important;
            font-size: 14px !important;
            letter-spacing: 1px;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:white; text-align:center; margin-top:0;'>LOGIN</h2>", unsafe_allow_html=True)
        
        user = st.text_input("USUARIO", key="login_user")
        password = st.text_input("CONTRASEÑA", type="password", key="login_pass")
        
        if st.button("INGRESAR", use_container_width=True):
            if user == "admin" and password == "1234": # Cambiá esto por tus credenciales
                st.session_state.seccion_activa = "Transporte"
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
