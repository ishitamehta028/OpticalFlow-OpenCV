""" Horn-Schunck-Algorithm
reference : http://datahacker.rs/013-optical-flow-using-horn-and-schunck-method/ 

Dense Optical flow
assumes : bright constancy & smooth flow field
"""
import cv2 as cv
import numpy as np

capture = cv.VideoCapture("cars.gif")


ret, previous_frame = capture.read()
mask = np.zeros_like(previous_frame)

while(capture.isOpened()):
    ret, frame = capture.read()
    cv.imshow("INPUT",frame)

    gray_prev = cv.cvtColor(previous_frame, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_diff = cv.subtract(gray_prev, gray)

    flow = cv.calcOpticalFlowFarneback(gray_prev, gray, None, 0.5, 5, 15, 3, 5, 1.2, 0)

    magnitude, angle = cv.cartToPolar(flow[..., 0], flow[..., 1])
    mask[..., 0] = angle * 180 / np.pi / 2
    mask[..., 2] = cv.normalize(magnitude, None, 0, 255, cv.NORM_MINMAX)
    bgr = cv.cvtColor(mask, cv.COLOR_HSV2BGR)
    cv.imshow("dense optical flow", bgr)
    previous_frame = frame;


#press x to close
    if cv.waitKey(1) & 0xFF == ord('x') :
        break;
capture.release()  ;
cv.destroyAllWindows()
