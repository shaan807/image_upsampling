### Project Description:
Welcome to our Image Resolution Enhancement project! This application, built using Streamlit, offers a seamless solution for enhancing image resolution. Unlike traditional methods that rely on paired low and high-resolution images, our model doesn't necessitate such pairs. Instead, it employs cutting-edge techniques to boost image quality, ensuring sharper, more detailed results.

### Libraries Used:
1. **Streamlit**: Powering the user-friendly web application interface.
2. **OpenCV (cv2)**: Enabling image processing tasks like reading, processing, and saving images, alongside resolution enhancement techniques.
3. **NumPy**: Supporting numerical computations and array manipulation.
4. **Pillow**: Facilitating image manipulation and processing, especially handling various image formats.
5. **scikit-image**: Augmenting the project with additional image processing capabilities, such as exposure adjustment.

### Functions:
1. **`enhance_image(image)`:** Takes a low-resolution image and enhances its resolution using advanced algorithms, possibly involving interpolation, super-resolution, or deep learning-based methods.

## Image Comparison

![Original Image](original.png) ![Enhanced Image](upscaled_test.png)
*Left: Original Image | Right: Enhanced Image*

![Original Image](pexels-eberhardgross-2437297.jpg) ![Enhanced Image](enhanced_image%20(5).jpg)
*Left: Original Image | Right: Enhanced Image*

![Original Image](img4.jpg) ![Enhanced Image](enhanced_image%20(7).jpg)

*Left: Original Image | Right: Enhanced Image*

![Original Image](pexels-snapwire-6992.jpg) ![Enhanced Image](enhanced_image%20(4).jpg)

*Left: Original Image | Right: Enhanced Image*

2. **Streamlit Interface Functions:**
   - **`st.title("Image Resolution Enhancement")`:** Sets the title of the Streamlit app.
   - **`st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])`:** Allows users to upload images.
   - **`st.image(image, caption="Image", use_column_width=True)`:** Displays images in the app with an optional caption and adjustable width.
   - **`st.button("Save Image")`:** Lets users save the enhanced image.

### Model Working:
1. **Image Upload:** Users upload an image via the file uploader widget.
2. **Image Processing:** OpenCV processes the uploaded image to a suitable format for resolution enhancement.
3. **Resolution Enhancement:** The `enhance_image()` function boosts the uploaded image's resolution using appropriate algorithms.
4. **Display:** The enhanced image appears in the Streamlit app interface for user viewing.
5. **Download:** Users have the option to download the enhanced image using the "Save Image" button.

### Overall Working:
1. Users upload an image.
2. The app processes the uploaded image and enhances its resolution.
3. The enhanced image is displayed in the app interface.
4. Users can download the enhanced image if desired.

This project streamlines the process of enhancing image resolution by leveraging Streamlit and OpenCV, eliminating the need for paired low and high-resolution images. Additionally, you can directly utilize the pre-trained model "image_processor_model.joblib" for optimal results, skipping the training phase for added convenience.
