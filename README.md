# 🧠 MNIST Digit Classifier (Streamlit App)

This project is an interactive **handwritten digit recognition app** built with **TensorFlow** and **Streamlit**.  
It uses a pre-trained **CNN (Convolutional Neural Network)** model trained on the MNIST dataset to identify digits (0–9) from uploaded images.

---

## 🚀 Features

- Upload an image of a handwritten digit (`.png`, `.jpg`, or `.jpeg`)
- Automatically preprocesses and classifies the digit
- Displays the uploaded image and predicted output
- Built using Streamlit for an interactive web interface

---

## 🧩 Requirements

Before running the app, make sure you have the following installed:

- Python 3.8 or higher  
- TensorFlow ≥ 2.15  
- Streamlit ≥ 1.40  
- Pillow  
- NumPy  

You can install all dependencies using:

```bash
pip install tensorflow streamlit pillow numpy
📁 Project Structure
bash
Copy code
mnist_app/
│
├── app.py                  # Main Streamlit application
├── mnist_cnn_model.h5      # Pre-trained CNN model
└── README.md               # Project documentation
▶️ How to Run the App
Open a terminal and navigate to the project directory:

bash
Copy code
cd C:\Users\user\mnist_app
Run the Streamlit app:

bash
Copy code
streamlit run app.py
A browser window will automatically open at:

arduino
Copy code
http://localhost:8501
Upload a 28x28 pixel grayscale image of a handwritten digit to see the model’s prediction.

🧠 Model Details
Dataset: MNIST Handwritten Digits

Model Type: Convolutional Neural Network (CNN)

Input Shape: 28x28x1

Output: 10 classes (digits 0–9)

Framework: TensorFlow / Keras

⚡ Troubleshooting
If you see:

vbnet
Copy code
TypeError: Error when deserializing class 'InputLayer'
✅ Update TensorFlow to version 2.15.0 or higher:

bash
Copy code
pip install --upgrade tensorflow
If Streamlit doesn’t start, check that it’s properly installed:

bash
Copy code
pip show streamlit
🌐 Deployment
You can easily deploy this app online using:

Streamlit Cloud

Hugging Face Spaces

Both platforms support .py apps and TensorFlow models directly.

📜 License
This project is open source and available under the MIT License.

👨‍💻 Author
James Njuguna
Developer | Machine Learning Enthusiast
📍 Nairobi, Kenya
