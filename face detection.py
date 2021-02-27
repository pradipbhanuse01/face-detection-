import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(r"C:\Users\Admin\PycharmProjects\face detecton\haarcascade_frontalface_default.xml")
#print(face_cascade)
# To capture video from webcam.
cap = cv2.VideoCapture(0)
while cap.isOpened():
    # Read the frame
    _, img = cap.read()
#img =cv2.imread("face.jpg")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray,1.3,4,5)
    print(len(faces))
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 4), 10)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(1) & 0xff

    if k == 27:
        break

cap.release()


# Release the VideoCapture object
