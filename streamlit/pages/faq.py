import streamlit as st

st.title("Frequently Asked Questions")

with st.expander("How is my premium calculated?"):
    st.write("We use a machine learning model based on your inputs")

with st.expander("Can I get a discount?"):
    st.write("Yes, safe drivers may qualify.")
