import streamlit as st
# ----------------------------------
# streamlit run meu_site.py
# ----------------------------------
# https://fonts.google.com/icons?hl=pt-br&selected=Material+Symbols+Outlined:responsive_layout:FILL@0;wght@400;GRAD@0;opsz@24&icon.size=24&icon.color=%230000F5
# ----------------------------------

#icon = ":material/token:"
icon = "flight_takeoff.svg"
st.set_page_config(
    page_title="CELEVE Assessoria",
    page_icon=icon,
)

with st.container():
    st.subheader('subheader - Meu primeiro site')
    st.title('Title - Letras Grandes')
    st.write('writer - Informe o número do lote CTM: ')
    st.write('Linkes - [clique aqui](https://revistaoeste.com/)')


with st.container():
    st.write('---')

with st.container():
    st.write('---NOVO CONTAINER---')
    st.image("prédio01.jpg", caption="Figura 01")

with st.container():
    title = st.text_input("Aqui vem o título", " ")
    st.write("O que foi digitado: ", title)
    st.text_input("DIGITE AQUI O NÚMERO DO TERRENO CTM", value="", max_chars=12)

st.write('---')
with st.container():
    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    col1, col2 = st.columns(2)

    with col1:
        st.checkbox("Disable text input widget", key="disabled")
        st.radio(
            "Set text input label visibility 👉",
            key="visibility",
            options=["visible", "hidden", "collapsed"],
        )
        st.text_input(
            "Placeholder for the other text input widget",
            "This is a placeholder",
            key="placeholder",
        )

    with col2:
        text_input = st.text_input(
            "Enter some text 👇",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder=st.session_state.placeholder,
        )

        if text_input:
            st.write("You entered: ", text_input)
