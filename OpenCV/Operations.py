import cv2

image = cv2.imread('puppy.jpeg')

print("Original Image size:",image.shape)               # in .shape height, width
cv2.imshow('original image', image)

'''
resized_img = cv2.resize(image, (500,560))          # width, height
print("Resized Image Shape:", resized_img.shape)
cv2.imshow('Resized img', resized_img)
'''

crop_img = image[250: 800, 0: 700]
cv2.imshow('Cropped img', crop_img)
cv2.waitKey(0)