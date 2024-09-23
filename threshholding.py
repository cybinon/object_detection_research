import cv2

def thresholding(image):  
    _, thresholded_image = cv2.threshold(image, 110, 255, cv2.THRESH_BINARY)    
    return thresholded_image
