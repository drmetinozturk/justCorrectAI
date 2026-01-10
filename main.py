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

user_input = st.text_area("Please paste your text here:", height=250, placeholder="The text I want to correct is ...")

if st.button("Give me the corrected text"):
    if user_input.strip():
        with st.spinner("Working hard..."):
            try:
                response = model.generate_content(user_input)
                corrected_text = response.text.strip()
                original_text = user_input.strip()

                st.divider()
                st.subheader("Output:")

                # Değişiklik Kontrolü
                if corrected_text == original_text:
                    st.info("✅ NO CHANGES: Your text is already perfect!")
                else:
                    st.success("Changes applied successfully:")
                    # Copy-paste kolaylığı için st.code kullanıyoruz (Kendinden kopyalama butonu vardır)
                    st.code(corrected_text, language=None)
            
            except Exception as e:
                st.error(f"An error has occurred: {e}")
    else:
        st.warning("Please enter a text first.")