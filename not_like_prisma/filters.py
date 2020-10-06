import cv2
import numpy as np

class ImageFilters():
    def __init__(self, image):
        self.image = image
    
    def gray_filter(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def blur_filter(self, strength_of_blur = 5):
        blured_image = cv2.medianBlur(self.image,strength_of_blur)
        return blured_image
    
    def color_filter(self):
        height, width, channels = self.image.shape
        red_img  = np.full((height,width,channels), (0,0,255), np.uint8)
        fused_img  = cv2.addWeighted(self.image, 0.8, red_img, 0.2, 0)
        return fused_img
