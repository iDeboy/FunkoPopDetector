import cv2
import numpy as np
import imutils
import os

POSITIVES = 'p'
NEGATIVES = 'n'

def ls(path): 
    return [obj.name for obj in os.scandir(path) if obj.is_file() and obj.name.endswith(".jpg")]

class Capture:

    def __init__(self, type=POSITIVES) -> None:

        if type not in [POSITIVES, NEGATIVES]:
            raise ValueError("Tipo de imagen no valida")

        self.type = type

        if not os.path.exists(self.type):
            os.makedirs(self.type)

        self.count = len(ls(self.type)) +1

    def start(self):

        cap = cv2.VideoCapture(1)

        x1, y1 = 190, 80
        x2, y2 = 450, 398

        while True:
            ret, frame = cap.read()

            if ret == False:
                break

            imAux = frame.copy()
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            objeto = imAux[y1:y2, x1:x2]
            objeto = imutils.resize(objeto, width=38)
            # print(objeto.shape)

            k = cv2.waitKey(1)
            if k == ord('s'):
                cv2.imwrite(self.type+'/objeto_{}.jpg'.format(self.count), objeto)

                print('Imagen almacenada: ', 'objeto_{}.jpg'.format(self.count))
                self.count += 1

            if k == 27:
                break

            cv2.imshow('frame', frame)
            cv2.imshow('objeto', objeto)

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    print(f"Positive foldername {POSITIVES}")
    print(f"Negative foldername {NEGATIVES}")
