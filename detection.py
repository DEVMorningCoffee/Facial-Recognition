import cv2

#Load Classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Access Webcame
video_capture = cv2.VideoCapture(0)

def detect_bounding_box(vid):

    # Improve the Readablity of image
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)

    # Detect Face
    faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x+w, y+h), (0, 255, 0,), 4)

    return faces

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()


# if __name__ == '__main__':
#     True