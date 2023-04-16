import streamlit as st


st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name