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
st.set_page_config(page_title="JustCorrect", page_icon="✍️", layout="centered")

# Mobile-Friendly Title
st.markdown(
    """
    <style>
    .main-title {
        font-size: clamp(1.8rem, 5vw, 2.5rem);
        font-weight: bold;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: clamp(1rem, 3vw, 1.2rem);
        color: #CCCCCC;
        line-height: 1.4;
        margin-bottom: 2rem;
    }
    </style>
    <div class="main-title">✍️ JustCorrect: Your Quick AI Proofreader</div>
    <div class="sub-title">
        Corrects only spelling and grammatical errors; does not alter the style.<br>
        <b>It is still your text—just without errors!</b>
    </div>
    """,
    unsafe_allow_html=True
)