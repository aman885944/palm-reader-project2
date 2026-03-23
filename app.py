import streamlit as st
from image_processing import process_hand_image
from predictor import predict_future
import cv2

st.title("🖐️ AI Palm Reading System")

uploaded_file = st.file_uploader("Upload your hand image", type=["jpg", "png"])

if uploaded_file is not None:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    st.image("temp.jpg", caption="Uploaded Image", use_column_width=True)

    st.write("Processing Image...")

    edges = process_hand_image("temp.jpg")

    st.image(edges, caption="Detected Palm Lines")

    st.write("🔮 Predicting Your Future...")

    personality, career, love, health = predict_future()

    st.subheader("✨ Results")
    st.write("🧠 Personality:", personality)
    st.write("💼 Career:", career)
    st.write("❤️ Love Life:", love)
    st.write("🏥 Health:", health)