import cv2

def resize_image(image, scale=None, width=None, height=None):
    # If both width and height are provided, resize to those dimensions
    if width and height:
        resized_image = cv2.resize(image, (width, height))
    elif scale:
        # If only scale is provided, resize by the scale factor
        resized_image = cv2.resize(image, None, fx=scale, fy=scale)
    else:
        raise ValueError("Either scale or both width and height must be provided.")

    return resized_image

def pixelate_image(image, pixelation_factor):
    # Get the original dimensions
    height, width = image.shape[:2]

    # Calculate new dimensions based on the pixelation factor
    new_width = width // pixelation_factor
    new_height = height // pixelation_factor

    # Resize the image to the smaller size (pixelation)
    small_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Resize back to the original size
    pixelated_image = cv2.resize(small_image, (width, height), interpolation=cv2.INTER_NEAREST)

    return pixelated_image