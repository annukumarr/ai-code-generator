import streamlit as st
from generator import generate_code
from config import LANGUAGES


st.set_page_config(page_title="AI Code Generator", page_icon="⚡", layout="centered")

st.title("⚡ AI Code Generator")


if "output" not in st.session_state:
    st.session_state.output = None

if "language" not in st.session_state:
    st.session_state.language = None


if st.session_state.output is None:
    with st.form("generator_form"):
        language = st.selectbox("Programming Language", LANGUAGES)

        prompt = st.text_area(
            "What do you want to build?",
            height=150,
            placeholder="e.g. A REST API endpoint that validates email addresses"
        )

        submitted = st.form_submit_button("Generate Code ⚡", use_container_width=True)

    if submitted:
        if not prompt.strip():
            st.warning("Please enter a valid prompt.")
        else:
            with st.spinner(f"Generating {language} code..."):
                result = generate_code(language, prompt)

            st.session_state.output = result
            st.session_state.language = language
            st.rerun()


else:
    st.success(f"Generated {st.session_state.language} Code")

    code_output = st.session_state.output or ""
    lang = (st.session_state.language or "text").lower()

    st.code(code_output, language=lang)

    col1, col2 = st.columns(2)

  
    with col1:
        if st.button("⬅ Generate Another", use_container_width=True):
            st.session_state.output = None
            st.session_state.language = None
            st.rerun()

    
    with col2:
        st.download_button(
            "⬇ Download Code",
            data=code_output,
            file_name=f"generated.{lang}",
            mime="text/plain",
            use_container_width=True
        )