import streamlit as st
import os
from main import extractedText
from main import OCRpredict

file = st.file_uploader("Upload the image.")
if file:
    st.image(file)
    data = file.read()
    with open('temp.png','wb') as f:
        f.write(data)
    extractedText = OCRpredict('temp.png')
    st.write(extractedText)

    if st.button("Start OCR"):
        with st.spinner("Loading.........."):
            extractedText = OCRpredict('temp.png')
            with open('text.txt','wb') as f:
                f.write(extractedText)
        st.write(extractedText)

    os.remove('temp.png')