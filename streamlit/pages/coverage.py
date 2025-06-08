import streamlit as st

st.set_page_config(page_title="Coverage", page_icon="🛡️")

st.title("🛡️ What Does Your Insurance Cover?")

st.markdown("""
At **SafeDrive Analytics**, our predictive model is designed to assist in pricing premiums for policies that cover:

### 🚘 **Vehicle Coverage**
- Accidental damage
- Theft and hijacking
- Natural disasters (fire, flood, hail)

### 👤 **Personal Liability**
- Injury to third parties
- Damage to third-party property

### 📃 **Optional Add-ons**
- Roadside assistance
- Car hire services
- Windscreen repair

---

*Note: This app does not provide or sell insurance policies. The coverage items listed here are for illustrative purposes only* 
""")
