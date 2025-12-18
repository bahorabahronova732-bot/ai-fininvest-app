import streamlit as st

st.set_page_config(page_title="MHXS 9 Classification Demo", layout="centered")

st.title("AI FinInvest – MHXS 9 Classification & SPPI Demo")

st.markdown("""
Ushbu demo moliyaviy instrumentlarni MHXS 9 bo‘yicha
SPPI testi va biznes-model asosida avtomatik tasniflashni ko‘rsatadi.
""")

st.header("1. Moliyaviy instrument shartlari")

interest_type = st.selectbox(
    "Foiz turi",
    ["Oddiy foiz (faqat asosiy qarz + foiz)", "Murakkab / indeksatsiyalangan foiz"]
)

extra_features = st.multiselect(
    "Qo‘shimcha shartlar",
    ["Yo‘q", "Penalty", "Indeksatsiya", "Leverage"]
)

st.header("2. Business model")

business_model = st.selectbox(
    "Biznes model",
    ["Hold to collect", "Hold to collect and sell", "Trading"]
)

# --- SPPI TEST ---
if interest_type == "Oddiy foiz (faqat asosiy qarz + foiz)" and extra_features == ["Yo‘q"]:
    sppi_result = True
else:
    sppi_result = False

st.header("3. SPPI test natijasi")

if sppi_result:
    st.success("SPPI testi: PASSED (faqat asosiy qarz va foiz)")
else:
    st.error("SPPI testi: FAILED (murakkab shartlar mavjud)")

# --- CLASSIFICATION ---
st.header("4. MHXS 9 bo‘yicha tasnif")

if sppi_result and business_model == "Hold to collect":
    classification = "Amortized Cost"
elif sppi_result and business_model == "Hold to collect and sell":
    classification = "FVOCI"
else:
    classification = "FVTPL"

st.success(f"Moliyaviy instrument tasnifi: **{classification}**")

st.markdown("""
### Izoh:
- SPPI testi MHXS 9 talablariga muvofiq baholandi
- Biznes model hisobga olindi
- Tizim avtomatik tasniflash qarorini berdi
""")
