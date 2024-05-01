import cv2
import numpy as np
from skimage import exposure
import tensorflow as tf
import joblib
def enhance_image(image):
    if image is None:
        # st.error("Error: Input image is empty or could not be loaded.")
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

def deblur_image(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Wiener deconvolution for image deblurring
    psf = np.ones((5, 5)) / 25  # Example: Point spread function (PSF) for blurring
    deblurred_image = cv2.filter2D(gray_image, -1, psf)
    return deblurred_image



# Serialize and save the functions to a file
joblib.dump(enhance_image, 'image_processor_model.joblib')


