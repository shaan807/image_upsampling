import cv2
from skimage import exposure

def enhance_image(image):
    if image is None:
        print("Error: Input image is empty or could not be loaded.")
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

# Load the input image
input_image_path = 'original.png'  # Update with your image path
input_image = cv2.imread(input_image_path)

# Check if the input image was loaded successfully
if input_image is None:
    print("Error: Could not load the input image.")
else:
    # Enhance the image quality
    enhanced_image = enhance_image(input_image)
    
    if enhanced_image is not None:
        # Save the enhanced image
        output_path = 'enhanced_image.png'
        cv2.imwrite(output_path, enhanced_image)
        print(f"Enhanced image saved successfully at '{output_path}'")
    else:
        print("Error occurred during image enhancement.")
