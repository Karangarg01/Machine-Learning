import cv2

image = cv2.imread('salt_pepper_noise.jpg')

cv2.imshow('image', image)

k_size = 7
image_blur = cv2.blur(image, (k_size,k_size))
cv2.imshow('blur_image', image_blur)

gaussian_blur = cv2.GaussianBlur(image,(k_size,k_size),5)
cv2.imshow('Gaussian Blur', gaussian_blur)

# Median filter is commonly used to remove salt pepper noise from the image
median_blur = cv2.medianBlur(image,k_size,5)
cv2.imshow('Median Blur', median_blur)

cv2.waitKey(0)