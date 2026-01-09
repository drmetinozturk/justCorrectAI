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
st.set_page_config(page_title="AI Proofreader", page_icon="✍️")
st.title("✍️ Hızlı Proofreader")
st.caption("Sadece yazım ve dil bilgisi hatalarını düzeltir, üsluba dokunmaz.")

user_input = st.text_area("Metni buraya yapıştırın:", height=250, placeholder="Düzeltilmesini istediğiniz metin...")

if st.button("Hataları Ayıkla"):
    if user_input.strip():
        with st.spinner("Düzeltiliyor..."):
            try:
                response = model.generate_content(user_input)
                st.subheader("Sonuç:")
                st.success(response.text)
                st.button("Sonucu Kopyala", on_click=lambda: st.write("Panoya kopyalandı (simüle)"))
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen önce bir metin girin.")