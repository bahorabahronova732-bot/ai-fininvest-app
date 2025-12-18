import streamlit as st

st.set_page_config(page_title="AI FinInvest Demo", layout="centered")

st.title("AI FinInvest Platform (Demo)")
st.subheader("Expected Credit Loss (ECL) – AI asosida baholash")

st.markdown("""
Ushbu demo platforma kredit risklarini **AI yordamida** baholash g‘oyasiga asoslangan.
Model **PD, LGD va EAD** ko‘rsatkichlari orqali **ECL** hisoblaydi.
""")

st.header("Kiritish ma’lumotlari")

pd = st.slider("PD – Default ehtimoli (%)", 0.0, 100.0, 5.0)
lgd = st.slider("LGD – Yo‘qotish darajasi (%)", 0.0, 100.0, 45.0)
ead = st.number_input("EAD – Kredit summasi (mln so‘m)", value=100.0)

ecl = (pd / 100) * (lgd / 100) * ead

st.header("Natija")
st.success(f"Expected Credit Loss (ECL): {ecl:.2f} mln so‘m")

st.markdown("""
### Izoh:
- **PD** – qarzdorlikni bajarmaslik ehtimoli  
- **LGD** – defolt holatidagi yo‘qotish  
- **EAD** – risk ostidagi kredit summasi  

Bu demo loyiha **AI FinInvest** konsepsiyasining soddalashtirilgan modeli hisoblanadi.
""")
