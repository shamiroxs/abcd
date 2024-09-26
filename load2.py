import cv2

def play_video(video_path):
    """Plays a video using OpenCV."""
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Cannot open video {video_path}")
        return

    # Loop to read and display video frames
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("Reached end of video or there was an error.")
            break

        # Display the frame in a window
        cv2.imshow('Video Playback', frame)

        # Press 'q' to exit the video early
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Path to the video in the current directory
    video_file = "annotate.mp4"
    
    play_video(video_file)
