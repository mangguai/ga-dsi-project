import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input
from PIL import Image

# Load the trained CNN model
model = tf.keras.models.load_model('cnn_model.keras')

# Function to preprocess the uploaded image
def preprocess_image(img, target_size):
    img = img.resize(target_size)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Streamlit app
def main():
    st.title('Cancer Classification')
    st.write('Upload an image to classify it as cancerous or non-cancerous.')

    # File uploader
    uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Get the input shape of the model
        input_shape = model.input_shape[1:3]

        # Preprocess the image
        preprocessed_image = preprocess_image(image, input_shape)

        # Make predictions
        predictions = model.predict(preprocessed_image)
        class_names = ['Non-Cancerous', 'Cancerous']
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions) * 100

        # Display the prediction result
        st.subheader('Prediction Result')
        st.write(f'Class: {predicted_class}')
        st.write(f'Confidence: {confidence:.2f}%')

if __name__ == '__main__':
    main()