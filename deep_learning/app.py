import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("mnist_model.h5")

st.title("Handwritten Digits Identification")
st.write("Upload a grayscale image of 28x28 dimension of digits (0-9)")

uploaded_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])

if uploaded_file:
    image=Image.open(uploaded_file).convert("L")
    image=image.resize((28,28))

    st.image(image,caption="Uploaded image",width=150)

    #Input Image preprocess
    img_array=np.array(image)/255.0
    img_array=img_array.reshape(1,28,28,1)

    prediction=model.predict(img_array) # Input -->7 prediction = [0,0,0,0,0,0,0,1,0,0] 
    predicted_class=np.argmax(prediction)
    st.success(f"Predicted Digit is : {predicted_class}")

    