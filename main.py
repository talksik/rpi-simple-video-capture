import cv2

# Create a VideoCapture object to capture video from the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Create a window to display the captured video
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

# Read and display frames from the camera until the user presses 'q'
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if a frame was successfully read
    if not ret:
        print("Failed to read a frame from the camera")
        break

    # Display the frame in the "Video" window
    cv2.imshow("Video", frame)

    # Wait for the user to press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()
