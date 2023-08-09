import cv2

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the eyeglasses image with transparency
eyeglasses_img = cv2.imread('product6.png', cv2.IMREAD_UNCHANGED)
eyeglasses_img = cv2.cvtColor(eyeglasses_img, cv2.COLOR_BGR2RGBA)

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frames from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over detected faces
    for (x, y, w, h) in faces:
        # Resize the eyeglasses image to fit the width of the face
        resized_eyeglasses = cv2.resize(eyeglasses_img, (w, int(h/2)))

        # Calculate the coordinates to overlay the eyeglasses image
        x_offset = x
        y_offset = int(y + h/4)

        # Overlay the eyeglasses image on the frame using alpha blending
        for i in range(resized_eyeglasses.shape[0]):
            for j in range(resized_eyeglasses.shape[1]):
                if resized_eyeglasses[..., 3][i, j] > 0:  # Check if the pixel is non-transparent
                    frame[y_offset + i, x_offset + j] = resized_eyeglasses[i, j, :3]

    # Display the result
    cv2.imshow('Virtual Try-On', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
