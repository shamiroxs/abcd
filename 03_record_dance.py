import cv2
import pygame


cap = cv2.VideoCapture(1) 

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640,480))

frame_count = 0
recording = False

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(frame_count)

    # Resize the frame to the desired window size
    resized_frame = cv2.resize(frame, (1280, 960))

    # Display the resized frame in a window
    cv2.imshow('frame', resized_frame)

    # Wait for 50 frames before starting to record
    if frame_count == 150:
        print("Start recording...")
        recording = True

    # Record the frames to a file
    if recording:
        out.write(frame)

    frame_count += 1

    if cv2.waitKey(1) & frame_count == 460:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
