import streamlit as st

st.set_page_config(page_title="AI FinInvest Demo Platform", layout="wide")

st.title("AI FinInvest – MHXS 9 & MHXS 13 Demo Platforma")

st.sidebar.title("Demo bo‘limlar")

demo = st.sidebar.radio(
    "Bo‘limni tanlang:",
    [
        "MHXS 9: Classification & SPPI",
        "MHXS 9: Expected Credit Loss (ECL)",
        "MHXS 13: Fair Value (Level 3)"
    ]
)

# =========================================================
# 1) MHXS 9 CLASSIFICATION + SPPI
# =========================================================
if demo == "MHXS 9: Classification & SPPI":
    st.header("MHXS 9 — Classification va SPPI testi")

    st.subheader("1. Moliyaviy instrument shartlari")

    interest_type = st.selectbox(
        "Foiz turi",
        [
            "Oddiy foiz (faqat asosiy qarz + foiz)",
            "Murakkab / indeksatsiyalangan foiz"
        ]
    )

    extra_features = st.multiselect(
        "Qo‘shimcha shartlar (ixtiyoriy)",
        ["Penalty", "Indeksatsiya", "Leverage"],
        default=[]
    )

    st.subheader("2. Business model")

    business_model = st.selectbox(
        "Biznes model",
        [
            "Hold to collect",
            "Hold to collect and sell",
            "Trading"
        ]
    )

    # --- SPPI LOGIKA (TO‘G‘RI) ---
    sppi_passed = (
        interest_type == "Oddiy foiz (faqat asosiy qarz + foiz)"
        and len(extra_features) == 0
    )

    st.subheader("3. SPPI test natijasi")

    if sppi_passed:
        st.success("SPPI testi: PASSED (faqat asosiy qarz va oddiy foiz)")
    else:
        st.error("SPPI testi: FAILED (murakkab shartlar mavjud)")

    st.subheader("4. MHXS 9 bo‘yicha tasnif")

    if sppi_passed and business_model == "Hold to collect":
        classification = "Amortized Cost"
    elif sppi_passed and business_model == "Hold to collect and sell":
        classification = "FVOCI"
    else:
        classification = "FVTPL"

    st.success(f"Moliyaviy instrument tasnifi: **{classification}**")

    st.markdown("""
**Izoh (MHXS 9):**
- SPPI faqat asosiy qarz + oddiy foiz bo‘lsa o‘tadi  
- Murakkab shartlar mavjud bo‘lsa → FVTPL  
- Tasnif avtomatik aniqlanadi
""")

# =========================================================
# 2) ECL DEMO
# =========================================================
elif demo == "MHXS 9: Expected Credit Loss (ECL)":
    st.header("Expected Credit Loss (ECL) — MHXS 9")

    pd = st.slider("PD – Default ehtimoli (%)", 0.0, 100.0, 5.0)
    lgd = st.slider("LGD – Yo‘qotish darajasi (%)", 0.0, 100.0, 45.0)
    ead = st.number_input("EAD – Kredit summasi (mln so‘m)", value=100.0)

    ecl = (pd / 100) * (lgd / 100) * ead

    st.success(f"ECL (Expected Credit Loss): **{ecl:.2f} mln so‘m**")

    st.markdown("""
**Izoh:**
- PD × LGD × EAD formulasi asosida hisoblandi  
- MHXS 9 talablariga mos
""")

# =========================================================
# 3) FAIR VALUE LEVEL 3
# =========================================================
elif demo == "MHXS 13: Fair Value (Level 3)":
    st.header("Fair Value — MHXS 13 (Level 3)")

    st.subheader("1. Kutilayotgan pul oqimlari")

    cf1 = st.number_input("1-yil pul oqimi (mln so‘m)", value=120.0)
    cf2 = st.number_input("2-yil pul oqimi (mln so‘m)", value=130.0)
    cf3 = st.number_input("3-yil pul oqimi (mln so‘m)", value=150.0)

    st.subheader("2. Makroiqtisodiy risk darajasi")

    risk_level = st.selectbox(
        "Risk darajasi",
        ["Low", "Medium", "High"]
    )

    risk_free = 0.10
    risk_premium = {
        "Low": 0.03,
        "Medium": 0.06,
        "High": 0.10
    }

    discount_rate = risk_free + risk_premium[risk_level]

    fair_value = (
        cf1 / (1 + discount_rate) ** 1 +
        cf2 / (1 + discount_rate) ** 2 +
        cf3 / (1 + discount_rate) ** 3
    )

    st.success(f"Fair Value (DCF, Level 3): **{fair_value:.2f} mln so‘m**")

    st.markdown("""
**Izoh (MHXS 13):**
- Faol bozor mavjud emas  
- Level 3 — modelga asoslangan baholash  
- Diskont stavka makro risk asosida shakllandi
""")
