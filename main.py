import streamlit as st
import google.generativeai as genai

# 1. API Yapılandırması
genai.configure(api_key=st.secrets["KEY"])
# 2. Model Seçimi ve Sistem Talimatı
# Listenizdeki en stabil ve hızlı modellerden birini seçtik
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    system_instruction=(
        "Role: Strict Technical Proofreader. "
        "Task: Fix only typos, grammatical errors, and incorrect word usage. "
        "Constraints: Do not change the author's tone or writing style. "
        "Do not paraphrase. If there are no errors, return the original text. "
        "Output ONLY the corrected text without any comments or greetings."
    )
)

# 3. Streamlit Arayüzü
st.set_page_config(page_title="JustCorrect", page_icon="✍️")
st.title("✍️JustCorrect: Your Quick AI Proofreader")
st.markdown(
    '<p style="font-size: 24px; color: #555555; margin-top: -15px;">'
    'Corrects only spelling and grammatical errors; does not alter the style.'
    'It is still your text--just free of errors!'
    '</p>', 
    unsafe_allow_html=True
)

user_input = st.text_area("Please paste your text here:", height=250, placeholder="The text I want to correct is ...")

if st.button("Give me the corrected text"):
    if user_input.strip():
        with st.spinner("Working hard..."):
            try:
                response = model.generate_content(user_input)
                st.subheader("Output:")
                st.success(response.text)
                st.button("Copy the output", on_click=lambda: st.write("Copied to clipboard"))
            except Exception as e:
                st.error(f"An error has occurred: {e}")
    else:
        st.warning("Please enter a text first.")