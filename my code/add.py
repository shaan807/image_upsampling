from model import enhance_image, deblur_image
import tensorflow as tf
# Define a dummy image for shape inference
image = tf.zeros((1, 224, 224, 3), dtype=tf.float32)

# Restore the functions
enhance_image = tf.function(enhance_image).get_concrete_function(image)
deblur_image= tf.function(deblur_image).get_concrete_function(image)

# Create a SavedModel
tf.saved_model.save({
    'enhance_image': enhance_image,
    'process_image': deblur_image
}, 'saved_model')
