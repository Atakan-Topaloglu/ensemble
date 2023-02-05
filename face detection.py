# Used ChatGPT for this project.

import cv2

face_cascade = cv2.CascadeClassifier(r'\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

glasses_cascade = cv2.CascadeClassifier(r'\anaconda3\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        # Get the coordinates of the first face
        x, y, w, h = faces[0]

        # Crop the face region from the frame
        face_region = frame[y:y+h, x:x+w]

        face_region_gray = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)

        # Detect glasses in the face region
        glasses = glasses_cascade.detectMultiScale(face_region_gray, 1.1, 4)

        # Check if any glasses were detected
        if len(glasses) > 0:
		 print("Glasses detected!")
        else:
         	 print("No glasses detected.")

    cv2.imshow('Face Detection', frame)

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
