<h1>Face Landmark Detection</h1>


<h2>Overview</h2>

Face Landmark Detection is a computer vision project that uses the Dlib library to detect and visualize key facial landmarks on a live video feed. This project identifies 68 facial landmarks, including the eyes, nose, mouth, and jawline, and marks them on the user's face in real-time. The project leverages OpenCV for capturing the video feed and Dlib for detecting and predicting the facial landmarks.

<h2>Features</h2>

Real-time face landmark detection using a webcam.
68 facial landmarks detected and visualized.
Face detection using Dlib's frontal face detector.
Landmark visualization with circles on the detected points.
Optional mirroring of the webcam feed.
Easy-to-use and light-weight.


Prerequisites

To run the project, you'll need:

Python 3.x
OpenCV
Dlib
Numpy
Install the Required Libraries
Install the required Python libraries via pip:

bash
Copy
Edit
pip install opencv-python numpy dlib
Project Setup
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/KaranJangid8656/face_landmark_detection.git
cd face_landmark_detection
2. Download the Pre-trained Model
This project requires the shape_predictor_68_face_landmarks.dat file for landmark detection. You can download it from here.

After downloading the file, place it in the project directory.

3. Running the Project
Run the following Python script to start detecting facial landmarks:

bash
Copy
Edit
python face_landmark_detection.py
The webcam feed will appear, and you should see the landmarks highlighted on your face.

How It Works
Capture Video Feed: The script uses OpenCV's cv2.VideoCapture to access the webcam.
Face Detection: The Dlib's frontal face detector (dlib.get_frontal_face_detector()) is used to detect faces in each frame.
Landmark Prediction: Once a face is detected, the dlib.shape_predictor() is used to predict the 68 facial landmarks.
Visualize Landmarks: For each detected landmark, a small circle is drawn on the face to visualize the points.
Customization
Mirroring the Video Feed: If you want to mirror the webcam feed, uncomment the line in the code that flips the frame horizontally.

python
Copy
Edit
frame = cv2.flip(frame, 1)
Change Detection Quality: You can experiment with different face detection and landmark prediction models in Dlib.

Known Issues
The project may not work well under low-light conditions or poor camera quality.
Some landmarks might be inaccurate if the face is at an unusual angle.
Contributing
We welcome contributions to improve this project! If you find a bug or have an enhancement idea, feel free to:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes.
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
