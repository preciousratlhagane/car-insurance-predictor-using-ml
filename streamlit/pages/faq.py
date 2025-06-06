import streamlit as st

st.title("❓ Frequently Asked Questions")

with st.expander("🔍 What is this app for?"):
    st.write(
        "This app predicts car insurance premiums using historical data and machine learning")

with st.expander("🧠 What data does it use?"):
    st.write(
        "It uses inputs like driver's age, vehicle types, fuel type, and past claim history.")

with st.expander("🤖 Is this an official quote?"):
    st.write("No. This is a prototype for educational and demonstration purposes.")

with st.expander("🔒 Is my data stored?"):
    st.write(
        "No. Your data is only used during your session and is not saved or shared.")

with st.expander("📉 What are the limitations?"):
    st.markdown("""
                - No real-time underwriting rules
                - Limited training data
                - Assumes clean and structured input 
                """)

with st.expander("📩 Who can I contact for support?"):
    st.markdown(
        """Please refer to the **About** page for contact and repository links.""")
