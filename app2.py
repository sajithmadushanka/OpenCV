import cv2
import time

# Provide the correct path to your video file
video_path = "./images/img-1.mp4"

# Initialize video capture
video = cv2.VideoCapture(video_path)

# Check if the video capture object is successfully opened
if not video.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    # Read a frame from the video
    success, img = video.read()

    # Check if the frame is successfully read
    if not success:
        print("Error: Could not read frame. End of video.")
        break

    # Check if the frame dimensions are valid
    if img.shape[0] > 0 and img.shape[1] > 0:
        # Display the frame in a window named 'vdi'
        cv2.imshow('vdi', img)

        # Introduce a delay between frames (adjust as needed)
        time.sleep(0.1)  # 100 milliseconds delay

    else:
        print("Error: Invalid frame dimensions.")
        break

    # Check for the 'e' key press to exit
    if cv2.waitKey(1) & 0xff == ord('e'):
        break

# Release the video capture object and close the window
video.release()
cv2.destroyAllWindows()
