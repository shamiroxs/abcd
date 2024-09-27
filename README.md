### ABCD Project Documentation: "Anybody Can Dance"

#### **Project Title**:
**ABCD** - Anybody Can Dance

---

#### **Objective**:
The goal of the ABCD project is to help participants overcome stage fear and build confidence in dancing. We believe that everyone, regardless of skill level, can dance when given the right motivation. Our motto is **"Anybody Can Dance"**, and the project promotes movement by rewarding participants with a score based on their body movement. The leaderboard further encourages participants to move freely, aiming for high scores based on how much they engage their body during a dance session.

---

#### **Problem Solved**:
Many people feel shy or hesitant to dance in front of others, especially on stage. Our project provides a fun and interactive environment to motivate participants to express themselves through movement. By gamifying the experience with a score and leaderboard, we inspire individuals to move more confidently and enjoy the process of dancing.

---

#### **Hardware Requirements**:
- **Classroom Projector**: To display live scores and the leaderboard.
- **Webcam**: Used to record the dance session.
- **Laptop**: Running the software and capturing video input.
- **Stage Lighting & Decoration Lights**: Enhancing the atmosphere and stage setup.
- **Speakers**: For playing music during the performance.

---

#### **Software Requirements**:
The entire project is based on Python, and we used the following libraries:
- **Flask**: For the backend server and interaction.
- **imutils**: For easier image processing with OpenCV.
- **loading**: To display the loading screen.
- **Mediapipe**: For detecting body landmarks and poses.
- **OpenCV**: For video processing.
- **Pandas**: To handle data, such as storing and retrieving scores.
- **Pygame**: For displaying the leaderboard and user interface elements.
- **Scikit-learn**: For potential future classification and analysis tasks.
- **Setuptools**: For easy packaging and deployment.

---

#### **System Architecture**:
1. **Webcam Input**: The webcam records the dancer's movements and saves the recording as `output.mp4`.
2. **Pose Detection (Mediapipe)**: Using MediaPipe, the system detects 32 key body points on the participant’s skeleton in real-time.
3. **Score Calculation**: By analyzing two consecutive frames and comparing body points, the system calculates the dancer's movement score based on the Euclidean distance between the body points.
4. **Loading Screen**: During the pose detection process, a loading screen (`load.py`) will display progress.
5. **Video Processing**: The annotated video (`annotate.mp4`) is created and played.
6. **Leaderboard**: Scores are stored and updated in a text file (`lead.txt`) and displayed in the leaderboard.

---

#### **Installation Instructions**:
To set up the environment and install necessary libraries, follow these steps:

1. **Clone the Project**:
   ```bash
   git clone https://github.com/shamrioxs/abcd.git
   cd ABCD
   ```

2. **Install Dependencies**:
   You can install the required libraries using `pip`:
   ```bash
   pip install flask imutils loading mediapipe opencv-python pandas pygame scikit-learn setuptools
   ```

3. **Running the Project**:
   - Simply run the `run.py` file to start the project:
     ```bash
     python run.py
     ```

---

#### **Project Flow and Python Files**:
1. **`run.py`**: The main file that executes each part of the system in sequence. It runs in an infinite loop until the user closes the `username.py` window.
2. **`username.py`**: This Pygame file prompts the user to enter their name at the beginning.
3. **`03_record_dance.py`**: This script records the dancer’s performance using the webcam.
4. **`annotate_vid.py`**: Detects the poses from the recorded video and overlays the skeletons on the video.
5. **`load.py`**: Shows a loading screen while `annotate_vid.py` processes the pose detection.
6. **`score.py`**: This script calculates the movement score by comparing consecutive frames.
7. **`load2.py`**: Displays the annotated video during scoring.
8. **`lead.py`**: Displays the leaderboard in a Pygame window, showing participants' rankings and scores.

---

#### **How to Use the System**:
1. Enter your name into the system using the interface on the laptop.
2. Perform your dance on stage while the webcam records your performance.
3. After the dance, your movements will be processed and scored based on the amount of movement detected.
4. Your score will be displayed on the leaderboard projected in the classroom.
5. The leaderboard will update in real-time, showing each participant’s rank and score.

---

#### **Future Enhancements**:
- **Group Dance Support**: Currently, the system analyzes only one individual at a time. In the future, it could support group dances by analyzing multiple individuals simultaneously.
- **Music Playback**: Currently, the music is played externally. Future versions will have music integrated directly into the software.
- **Advanced Scoring Modes**: We aim to create different game modes, where users can choose to be scored on movement speed or on how closely they match pre-recorded dance moves in a database.

---

#### **Acknowledgements**:
This project is a collaborative effort from our S5CSE 2024 batch.
- **Idea Generation**: Yadhu Krishnan
- **Project Lead**: Shamir Ashraf
- **Mentors**: Rini T Paul, Pristy Paul T
- **Developers**: Shamir Ashraf (main developer), Ahsan (assistant developer)
- Special thanks to ChatGPT for technical assistance and our entire class for setting up the classroom and decorations.

---

#### **References**:
- **Inspiration and Base Code**: [DanceVision: AI-Driven Dance Proficiency Assessment](https://github.com/zin288/DanceVision-AI-Driven-Dance-Proficiency-Assessment)
