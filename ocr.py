import cv2
import pytesseract
import numpy as np

import config


# Refer to https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/


# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = config.PATH_TO_TESSERACT

def read_text_from_img(image: bytearray):
    # Read image from bytearray
    np_arr = np.frombuffer(image, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    # Preprocessing the image starts
    
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    
    # Specify structure shape and kernel size. 
    # Kernel size increases or decreases the area 
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect 
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    
    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    
    # Finding contours
    contours, hierarchy = cv2.findContours(
        dilation, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_NONE
    )
    
    # output texts
    texts = []
    
    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # # Drawing a rectangle on copied image
        # rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = img[y:y + h, x:x + w]
        
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        
        if text != "":
            texts.append(text)
    
    return texts
