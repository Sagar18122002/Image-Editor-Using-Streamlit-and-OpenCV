import streamlit as st
import cv2

from filters import (
    apply_blur,
    apply_sharpness,
    apply_brightness,
    apply_contrast,
    apply_edge_detection,
    apply_grayscale
)

from utils import load_image, convert_image_for_download


st.set_page_config(
    page_title="Image Editor",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Image Editing App")
st.write("Upload an image and apply filters using OpenCV")

# Sidebar Controls
st.sidebar.header("Filters")

blur = st.sidebar.slider("Blur", 1, 51, 1, step=2)

sharpness = st.sidebar.slider(
    "Sharpness",
    0.0,
    3.0,
    0.0,
    step=0.1
)

brightness = st.sidebar.slider(
    "Brightness",
    -100,
    100,
    0
)

contrast = st.sidebar.slider(
    "Contrast",
    0.5,
    3.0,
    1.0,
    step=0.1
)

edge_detect = st.sidebar.checkbox("Edge Detection")

grayscale = st.sidebar.checkbox("Grayscale")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    original_image = load_image(uploaded_file)

    processed_image = original_image.copy()

    # Apply Filters Sequentially
    processed_image = apply_blur(processed_image, blur)

    processed_image = apply_sharpness(
        processed_image,
        sharpness
    )

    processed_image = apply_brightness(
        processed_image,
        brightness
    )

    processed_image = apply_contrast(
        processed_image,
        contrast
    )

    if grayscale:
        processed_image = apply_grayscale(processed_image)

    if edge_detect:
        processed_image = apply_edge_detection(
            processed_image,
            100,
            200
        )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(
            cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB),
            use_container_width=True
        )

    with col2:
        st.subheader("Processed Image")
        st.image(
            cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB),
            use_container_width=True
        )

    download_image = convert_image_for_download(processed_image)

    st.download_button(
        label="Download Image",
        data=download_image,
        file_name="edited_image.png",
        mime="image/png"
    )