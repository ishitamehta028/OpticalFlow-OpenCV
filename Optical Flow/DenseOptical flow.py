import cv2 as cv
import numpy as np

# Calculates dense optical flow by Farneback method
cap = cv.VideoCapture("cars.gif")

# ret = a boolean return value from
# getting the frame, first_frame = the
# first frame in the entire video sequence
ret, first_frame = cap.read()

prev_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)

mask = np.zeros_like(first_frame)

# Sets image saturation to maximum
mask[..., 1] = 255

while(cap.isOpened()):
	
	# ret = a boolean return value from getting
	ret, frame = cap.read()
	cv.imshow("input", frame)
	
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	flow = cv.calcOpticalFlowFarneback(prev_gray, gray,None,0.5, 3, 15, 3, 5, 1.2, 0)
	
	# Computes the magnitude and angle of the 2D vectors
	magnitude, angle = cv.cartToPolar(flow[..., 0], flow[..., 1])
	
	# Sets image hue according to the optical flow direction
	mask[..., 0] = angle * 180 / np.pi / 2
	
	# Sets image value according to the optical flow magnitude (normalized)
	mask[..., 2] = cv.normalize(magnitude, None, 0, 255, cv.NORM_MINMAX)
	
	rgb = cv.cvtColor(mask, cv.COLOR_HSV2BGR)
	
	cv.imshow("dense optical flow", rgb)

	prev_gray = gray
	
	if cv.waitKey(1) & 0xFF == ord('d'):
		break
cap.release()
cv.destroyAllWindows()
