import streamlit as st

st.title("Contact us")
st.write("movierecommender@gmail.com")
st.text_input("Enter movies you would suggest to other viewers")
submit = st.button("Submit")
if submit:
    st.write("thank you for your suggestion😁")

st.text_input("Enter your contact number for future reference(optional)")
enter = st.button("Enter")
if enter:
    st.write("Thank you for cooperation🙏")
