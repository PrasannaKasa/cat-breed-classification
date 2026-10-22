
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Cat Breed Identification AI",
    page_icon="🐱",
    layout="wide"
)

st.title("🐱 Cat Breed Identification AI")
st.write("Upload a cat image to get started!")

st.sidebar.header("About")
st.sidebar.write(
    "This project aims to identify cat breeds "
    "using Artificial Intelligence."
)

uploaded_file = st.file_uploader(
    "Upload your cat image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Your uploaded cat image",
        width=400
    )

    st.success("Image uploaded successfully!")

    st.info(
        "AI model is not connected yet. "
        "Breed prediction will be added after "
        "training and connecting the model."
    )
else:
    st.caption("Supported formats: JPG, JPEG, PNG")
