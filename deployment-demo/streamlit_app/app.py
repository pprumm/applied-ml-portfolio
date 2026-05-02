from io import BytesIO

import requests
import streamlit as st
from PIL import Image


API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="EO Object Detection", layout="centered")

st.title("EO Object Detection")
st.write("YOLOv8 inference on NWPU VHR-10 aerial imagery.")

uploaded_file = st.file_uploader(
    "Upload an aerial image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.subheader("Input Image")
    st.image(uploaded_file, use_container_width=True)

    if st.button("Run Detection"):
        with st.spinner("Running YOLOv8 inference..."):
            response = requests.post(
                API_URL,
                files={"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            )

        if response.status_code == 200:
            pred_img = Image.open(BytesIO(response.content))

            st.subheader("Prediction")
            st.image(pred_img, use_container_width=True)

            st.download_button(
                label="Download prediction",
                data=response.content,
                file_name=f"pred_{uploaded_file.name}",
                mime="image/jpeg"
            )
        else:
            st.error("Prediction failed. Check that the FastAPI server is running.")