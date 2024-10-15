import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title of the app
st.title("Image Smoothing App")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image file is uploaded
if uploaded_file is not None:
    # Convert the file to an OpenCV image
    image = np.array(Image.open(uploaded_file))
    
    # Display the original image
    st.subheader("Original Image")
    st.image(image, channels="RGB")

    # Select smoothing method
    option = st.selectbox(
        "Choose a smoothing technique",
        ("Gaussian Blur", "Median Blur", "Bilateral Filter")
    )

    # Gaussian Blur
    if option == "Gaussian Blur":
        # Slider for kernel size
        kernel_size = st.slider("Gaussian Kernel Size", 3, 15, 7, step=2)
        blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    # Median Blur
    elif option == "Median Blur":
        # Slider for kernel size (odd values)
        kernel_size = st.slider("Median Kernel Size", 3, 15, 5, step=2)
        blurred_image = cv2.medianBlur(image, kernel_size)
    
    # Bilateral Filter
    elif option == "Bilateral Filter":
        # Sliders for bilateral filter parameters
        d = st.slider("Diameter of pixel neighborhood", 1, 25, 9)
        sigma_color = st.slider("Sigma Color (color space filter strength)", 10, 200, 75)
        sigma_space = st.slider("Sigma Space (coordinate space filter strength)", 10, 200, 75)
        blurred_image = cv2.bilateralFilter(image, d, sigma_color, sigma_space)

    # Display the blurred image
    st.subheader(f"{option} Result")
    st.image(blurred_image, channels="RGB")
