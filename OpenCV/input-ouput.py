import cv2
import os

image = cv2.imread('img.jpeg')
# cv2.imshow('img', image)
# cv2.waitKey(5000)


# cv2.imwrite('output.png', image)

# Load video
video = cv2.VideoCapture("video.mp4")

fps = video.get(cv2.CAP_PROP_FPS)  # Get video FPS
frame_delay = max(1, int(1000 / fps))  # Convert FPS to milliseconds

while True:
    ret, frame = video.read()
    if not ret:
        break  # Stop if video ends

    # Resize frame to avoid zoom issues
    scale = 0.3  # Reduce size by 50%
    frame = cv2.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)))

    # Show frame
    cv2.imshow('Video', frame)

    # Wait for the correct time per frame, exit on 'q' key
    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
