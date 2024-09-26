import cv2
import pygame


cap = cv2.VideoCapture(0) 

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640,480))

frame_count = 0
recording = False

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(frame_count)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Wait for 50 frames before starting to record
    if frame_count == 50:
        print("Start recording...")
        recording = True

    # Record the frames to a file
    if recording:
        out.write(frame)

    frame_count += 1

    if cv2.waitKey(1) & frame_count == 360:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
