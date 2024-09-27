import cv2
import mediapipe as mp
import numpy as np
import math
import pygame

from scoreboard import display_score


# Initialize mediapipe pose detection
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

total_score = 0
score = 0

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def process_video(input_video):

    # Capture the video
    cap = cv2.VideoCapture(input_video)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {input_video}")
        return

    total_score = 0  # Store cumulative movement score
    prev_coords = None  # Store the landmarks of the previous frame

    # Set up the pose model
    with mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.5) as pose:
        frame_num = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Recolor frame to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Process the image and detect pose landmarks
            results = pose.process(image)

            # Extract all pose landmarks
            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                current_coords = [[landmark.x, landmark.y] for landmark in landmarks]  # Get all landmark coordinates

                if prev_coords is not None:
                    # Calculate the movement score (distance between current and previous frame landmarks)
                    distances = [calculate_distance(current_coords[i], prev_coords[i]) for i in range(len(current_coords))]
                    frame_score = sum(distances)
                    total_score += frame_score
                    print(f"Frame {frame_num}: Movement Score = {frame_score:.5f}")

                # Update previous coordinates
                prev_coords = current_coords
            else:
                print(f"Frame {frame_num}: No landmarks detected")

            frame_num += 1
        #if total_score > 200:
            #total_score = 98
        #else:
            #total_score = total_score/5
        print(f"\nTotal Movement Score: {total_score:.5f}")
        display_score(total_score)  # Display score at the end

        with open("lead.txt", "a") as file:  # Open file in append mode
            file.write(f"{total_score:.0f}\n")  # Write username and score as a comma-separated line

    cap.release()
    cv2.destroyAllWindows()

def markscore():
    return score
    



if __name__ == "__main__":
    # Set your video input path here
    input_video_path = './annotate.mp4'  # Replace this with the actual path to the input video
    process_video(input_video_path)
