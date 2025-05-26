import streamlit as st

car_model_option = st.selectbox("Pick your car model:", [
                                "BMW", "Volkswagen", "Toyota", "Kia", "Haval"])
st.write(f"You selected: {car_model_option}")
