import cv2
import mediapipe as mp
import argparse
import os

#from load import show_pygame_loading_screen


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

def run_video_annotation_with_loading():
    # Show the loading screen before the annotation process starts
    show_pygame_loading_screen(total=100, loading_message="Preparing video annotation...", load_char_color=(0, 128, 255), complete_message="Ready to annotate!")

    # Your video annotation code here
    annotate_video(input_video_path, output_video_path, frames_folder)


def annotate_video(input_video_path, output_video_path, frames_folder):
    cap = cv2.VideoCapture(input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, cap.get(cv2.CAP_PROP_FPS), 
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
                           int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    # Drawing specifications for landmarks and connections
    landmark_drawing_spec = mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=3)
    connection_drawing_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)

    os.makedirs(frames_folder, exist_ok=True)  # Create the frames_folder if it doesn't exist

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        frame_num = 0
        
        # Get the frames per second
        fps = cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second:", fps)

        #show_pygame_loading_screen()
        
        while cap.isOpened():
            ret, image = cap.read()
            if not ret:
                break

            # Convert the BGR image to RGB before processing.
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)

            # Draw landmarks on the image.
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                      landmark_drawing_spec, connection_drawing_spec)

            # Add frame number
            cv2.rectangle(image, (10, 2), (350, 60), (255,255,255), -1)
            cv2.putText(image, 'Frame: ' + str(frame_num), (15, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5 , (0,0,0), thickness=2)

            out.write(image)
            cv2.imwrite(os.path.join(frames_folder, f'frame_{frame_num}.jpg'), image)
            frame_num += 1
            print('Frame:', frame_num)

    cap.release()
    out.release()

if __name__ == "__main__":
    # input_video_path = f'./vid/raw/{args.file_name}'  # Adjust path as needed
    input_video_path = f'./output.mp4'  # Adjust path as needed
    output_video_path = f'./annotate.mp4'  # Adjust path as needed
    frames_folder = f'./vid/frames/output_annot'  # Adjust path as needed
    annotate_video(input_video_path, output_video_path, frames_folder)
