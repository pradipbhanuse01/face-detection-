import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(r"C:\Users\Admin\PycharmProjects\face detecton\haarcascade_frontalface_default.xml")

img =cv2.imread("abba.png")

    # Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
faces = face_cascade.detectMultiScale(gray,1.3,4,5)
print(len(faces))
    # Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 4), 5)

    # Display
cv2.imshow('img', img)

    # Stop if escape key is pressed
k = cv2.waitKey(0) & 0xff

if k == 27:
    cap.release()

# Release the VideoCapture object
