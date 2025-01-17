import cv2
import dlib

# Open the webcam
cap = cv2.VideoCapture(0)

# Initialize dlib face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = detector(gray)
    
    for face in faces:
        # Get the coordinates of the bounding box around the face
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        
        # Optional: Draw a rectangle around the face
        # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        
        # Get the facial landmarks
        landmarks = predictor(gray, face)
        
        # Loop through all 68 landmarks and draw them on the frame
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)
    
    # Display the resulting frame
    cv2.imshow("Karan's CAM", frame)
    
    # Wait for ESC key to exit
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
