import cv2

# Read the image
image = cv2.imread('puppy.jpeg')

# Check if image is loaded correctly
if image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# Resize the image
image = cv2.resize(image, (500, 800))

# Convert images to different color spaces
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Show all images in different windows
cv2.imshow('Original Image', image)
cv2.imshow('RGB Image', image_rgb)
cv2.imshow('Grayscale Image', image_gray)
cv2.imshow('HSV Image', image_hsv)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
