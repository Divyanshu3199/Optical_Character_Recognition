import easyocr
import cv2
import os
import matplotlib.pyplot as plt

def OCRpredict(img):
    img = cv2.imread('text.png')
    reader = easyocr.Reader(['en'])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = reader.readtext(img)
    extractedText = " ".join([text for i, text, j in result])
    return extractedText

extractedText = OCRpredict('text.png')
with open('text.txt','w') as f:
    f.write(extractedText)