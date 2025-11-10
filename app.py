import streamlit as st
import numpy as np
from PIL import Image

st.title("🧠 Brain Tumor Segmentation")
st.write("Upload an MRI scan to visualize predicted tumor region.")

IMG_SIZE = 96

# Upload file
uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "jpeg", "png", "tif"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded MRI", use_container_width=True)

    if st.button("Predict Tumor Mask"):
        st.write("Processing...")

        # Import TensorFlow inside (to avoid crash)
        import tensorflow as tf
        from tensorflow.keras.models import load_model

        # Load model dynamically
        model = load_model("brain_tumor_unet.h5", compile=False)

        # Preprocess
        img = image.convert("RGB").resize((IMG_SIZE, IMG_SIZE))
        img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

        # Predict
        pred_mask = model.predict(img_array)[0].squeeze()
        mask = (pred_mask > 0.5).astype(np.uint8) * 255

        st.image(mask, caption="Predicted Tumor Mask", use_column_width=True)
