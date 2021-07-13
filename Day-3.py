import cv2
import numpy as np

cap = cv2.VideoCapture(0)
image_dict={1:"Beach.jpg",2:'Cherry Blossom.jpg',3:'Ring.jpg',4:'Library.jpg',5:'power up.jpg',6:'Horror.jpg'}
print("Filters(Keys:Values):", image_dict.items())
n=int(input("Enter your choice using keys:"))
image = cv2.imread(image_dict[n])
print(image.shape)

while cap.isOpened():
    sucess, frame = cap.read()
    if sucess:
        image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
        bf = cv2.addWeighted(frame, 0.6, image, 0.4, gamma=1.0)
        cv2.imshow("Blended Frame", bf)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
    else:
        print("Could not access the webcam")
        break

cap.release()
cv2.destroyAllWindows()