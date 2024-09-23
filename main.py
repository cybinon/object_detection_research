import cv2
from threshholding import *
from resize_img import *
import os


def main():
  # Directories
  input_dir = 'tmp/input'
  output_dir = 'tmp/out'
  
  # Ensure output directory exists
  os.makedirs(output_dir, exist_ok=True)
  
  # Read all files in the input directory
  for filename in os.listdir(input_dir):
      if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add more extensions if needed
          # Full file path
          img_path = os.path.join(input_dir, filename)
          
          # Read the image with OpenCV
          image = cv2.imread(img_path)
          
          if image is not None:
              # Convert the image to grayscale
              image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
              # Apply thresholding
              image = thresholding(image)
              
              # Save the processed image to the output directory
              output_path = os.path.join(output_dir, filename)
              cv2.imwrite(output_path, image)
          else:
              print(f"Failed to read image {filename}")

print("Processing complete.")



if __name__ == '__main__':
  main() 