import cv2
import numpy as np
from os import path

"""
Turn Photos into Cartoons using OpenCV library
Adapted from https://towardsdatascience.com/turn-photos-into-cartoons-using-python-bb1a9f578a7e
"""

class Cartooner:
    def __init__(self, file, cartoonize=True):
        self.file = file
        self.filename, self.file_extension = path.splitext(file)
        if cartoonize:
            self.new_filename = self.filename.split('/')[-1] + '_cartoon' + self.file_extension
        else:
            self.new_filename = self.filename + self.file_extension

        self.img = cv2.imread(self.file)
        self.edges = self.edge_mask()
        self.img = self.color_quantisation()
        self.blur = cv2.bilateralFilter(self.img, d=7, sigmaColor=200,sigmaSpace=200)
        self.cartoon = cv2.bitwise_and(self.blur, self.blur, mask=self.edges)

    
    def edge_mask(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.medianBlur(gray, 7)
        edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
        return edges
    
    def color_quantisation(self):
        # Transform the image
        data = np.float32(self.img).reshape((-1, 3))

        # Determine criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

        # Implementing K-Means
        ret, label, center = cv2.kmeans(data, 9, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        result = center[label.flatten()]
        result = result.reshape(self.img.shape)
        return result

    def save_cartoon(self, directory=None):
        if directory is not None:
            filepath = directory + '/' + self.new_filename
            cv2.imwrite(filepath, self.cartoon)
            return filepath

        cv2.imwrite(self.new_filename, self.cartoon)
        return self.new_filename

if __name__ == "__main__":
    filename = input("Enter filename: ")
    cartoon = Cartooner(filename)
    cartoon.save_cartoon()