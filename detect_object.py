import cv2

def find_shape_center(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Find contours in the image
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Convert grayscale to BGR for drawing
    output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Loop over each contour
    for contour in contours:
        # Calculate the moments of the contour
        M = cv2.moments(contour)

        # Calculate the center (centroid) of the shape
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
        else:
            # In case the contour area (m00) is zero, set center to some default value (like zero)
            center_x, center_y = 0, 0

        # Mark the center of the shape with a red circle
        cv2.circle(output_image, (center_x, center_y), 5, (0, 0, 255), -1)

        # Optionally, print the center coordinates
        print(f"Shape center: (x: {center_x}, y: {center_y})")
    
    return output_image
