import streamlit as st

st.title("Select your favourite genre")
options = st.multiselect(
    'What are your favorite colors',
    ['Action', 'Adventure', 'comedy', 'Drama', 'Fantasy', 'Horror', 'Romantic', 'Sci-fi', 'Thriller']
   )
if options:
    st.text_input("Any other genre that you like")

submit = st.button("Submit")
if submit:
    st.write("thank you for your suggestion😁")
