import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi')

tmp = 0
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    tmp += 1
    if tmp == 20*11:
        count += 1
        cv2.imwrite(f'out/{count}.png', frame)
        tmp = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
