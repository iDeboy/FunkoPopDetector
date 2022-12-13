import os
import cv2


class Detector:

    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(1)

        self.funko_pop = cv2.CascadeClassifier('classifier/cascade.xml')

    def start(self):
        while True:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            toy = self.funko_pop.detectMultiScale(gray,
                                                  scaleFactor=5,
                                                  minNeighbors=90,
                                                  minSize=(70, 78))

            for (x, y, w, h) in toy:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, 'Funko Pop', (x, y-10), 2,
                            0.7, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
