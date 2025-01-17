<h1>Face Landmark Detection</h1>


<h2>Overview</h2>

Face Landmark Detection is a computer vision project that uses the Dlib library to detect and visualize key facial landmarks on a live video feed. This project identifies 68 facial landmarks, including the eyes, nose, mouth, and jawline, and marks them on the user's face in real-time. The project leverages OpenCV for capturing the video feed and Dlib for detecting and predicting the facial landmarks.


### Real-time face landmark detection using a webcam.



<p align="center">
    <img src="https://github.com/user-attachments/assets/98a1f7c3-171d-4d08-93ec-33994e4718d2" alt="Screenshot" width="500"/>
</p>



<h2>Features</h2>


68 facial landmarks detected and visualized.
Face detection using Dlib's frontal face detector.
Landmark visualization with circles on the detected points.
Optional mirroring of the webcam feed.
Easy-to-use and light-weight.


<h2>Prerequisites</h2>

To run the project, you'll need:



- `opencv-python`
- `numpy`
- `dlib`


<h2>How It Works</h2>


- **Capture Video Feed**: The script uses OpenCV's `cv2.VideoCapture` to access the webcam.
- **Face Detection**: The Dlib's frontal face detector (`dlib.get_frontal_face_detector()`) is used to detect faces in each frame.
- **Landmark Prediction**: Once a face is detected, the `dlib.shape_predictor()` is used to predict the 68 facial landmarks.
- **Visualize Landmarks**: For each detected landmark, a small circle is drawn on the face to visualize the points.



Change Detection Quality: You can experiment with different face detection and landmark prediction models in Dlib.

<h2>Known Issues</h2>

The project may not work well under low-light conditions or poor camera quality.
Some landmarks might be inaccurate if the face is at an unusual angle.



