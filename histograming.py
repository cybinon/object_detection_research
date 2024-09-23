import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the grayscale image
image = cv2.imread('1.jpeg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.plot(histogram)
plt.xlim([0, 256])  # Set x-axis limits
plt.show()
