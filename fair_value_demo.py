import streamlit as st

st.set_page_config(page_title="Fair Value Level 3 Demo", layout="centered")

st.title("AI FinInvest – Fair Value (MHXS 13, Level 3)")
st.markdown("Faol bozor mavjud emas → Model-based baholash (DCF)")

st.header("1. Moliyaviy investitsiya shartlari")

cf1 = st.number_input("1-yil pul oqimi (mln so‘m)", value=120.0)
cf2 = st.number_input("2-yil pul oqimi (mln so‘m)", value=130.0)
cf3 = st.number_input("3-yil pul oqimi (mln so‘m)", value=150.0)

st.header("2. Makro risk darajasi")

risk_level = st.selectbox(
    "Makro risk darajasi",
    ["Low", "Medium", "High"]
)

risk_free = 0.10  # 10% shartli
risk_premium = {
    "Low": 0.03,
    "Medium": 0.06,
    "High": 0.10
}

discount_rate = risk_free + risk_premium[risk_level]

st.write(f"Diskont stavkasi (avtomatik): {discount_rate*100:.1f}%")

st.header("3. Fair Value hisoblash (Level 3)")

fair_value = (
    cf1 / (1 + discount_rate)**1 +
    cf2 / (1 + discount_rate)**2 +
    cf3 / (1 + discount_rate)**3
)

st.success(f"Fair Value (DCF, Level 3): {fair_value:.2f} mln so‘m")

st.markdown("""
### Izoh:
- Faol bozor mavjud emas
- MHXS 13 ga ko‘ra Fair Value Level 3 qo‘llanildi
- Baholash modeli: Discounted Cash Flow (DCF)
""")
