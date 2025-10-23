import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("🧠 MNIST Digit Classifier")

# Load pre-trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('mnist_cnn_model.h5')
    return model

model = load_model()

uploaded_file = st.file_uploader("📤 Upload a handwritten digit image (28x28 px)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('L')
    img = img.resize((28, 28))
    st.image(img, caption="🖼️ Uploaded Image", width=150)

    img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0
    pred = model.predict(img_array)
    st.success(f"✅ Predicted Digit: {np.argmax(pred)}")
