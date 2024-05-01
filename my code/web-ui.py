import streamlit as st
import cv2
import numpy as np
from skimage import exposure
import io

def deblur_image(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Wiener deconvolution for image deblurring
    psf = np.ones((5, 5)) / 25  # Example: Point spread function (PSF) for blurring
    deblurred_image = cv2.filter2D(gray_image, -1, psf)  # Wiener deconvolution
    
    return deblurred_image

def enhance_image(image):
    if image is None:
        st.error("Error: Input image is empty or could not be loaded.")
        return None
    
    # Convert image to LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split LAB image into channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Apply adaptive histogram equalization (CLAHE) to L channel for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    clahe_l_channel = clahe.apply(l_channel)

    # Merge CLAHE-enhanced L channel with original A and B channels
    enhanced_lab_image = cv2.merge((clahe_l_channel, a_channel, b_channel))

    # Convert enhanced LAB image to BGR color space
    enhanced_bgr_image = cv2.cvtColor(enhanced_lab_image, cv2.COLOR_LAB2BGR)

    # Apply gamma correction to enhance brightness
    gamma = 1.2
    enhanced_bgr_image = exposure.adjust_gamma(enhanced_bgr_image, gamma)

    return enhanced_bgr_image

st.title("AI Powered Image Resolution Enhancer")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
enhanced_image = None
upscale_factor = st.slider("Upscale Factor", key="upscale_slider", min_value=1, max_value=4, step=1, value=1)

if uploaded_file is not None:
    # Read the image from the uploaded file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    input_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Display the original image
    st.image(input_image, caption="Original Image", use_column_width=True, channels="BGR")

    # Perform enhancement on the input image
    enhanced_image = enhance_image(input_image)

    # Display the enhanced image
    # if enhanced_image is not None:
    #     st.image(enhanced_image, caption="Enhanced Image", use_column_width=True, channels="BGR")

# Allow the user to increase the upscaling factor for the enhanced image
if enhanced_image is not None:
    upscaled_image = cv2.resize(enhanced_image, None, fx=upscale_factor, fy=upscale_factor, interpolation=cv2.INTER_LINEAR)
    st.image(upscaled_image, caption=f"Upscaled Enhanced Image (Factor: {upscale_factor})", use_column_width=True, channels="BGR")

    # Add a "Save Image" button
    if st.button("Save Image"):
        # Convert image to bytes
        enhanced_image_bytes = cv2.imencode('.jpg', upscaled_image)[1].tobytes()

        # Create a file stream and save the bytes to it
        output_file = io.BytesIO(enhanced_image_bytes)
        st.download_button(label="Click here to download", data=output_file, file_name="enhanced_image.jpg", mime="image/jpeg")
