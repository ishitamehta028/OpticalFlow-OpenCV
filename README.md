# OpticalFlow-OpenCV
Horn-Schunck-Algorithm, Farneback method and Lucas-Kanade Optical FLow using OpenCV in python
__________________________________

Optical Flow calculates the motion vector of two consecutive frames.
Optical Flow gives us the capacity of motion detection in a frame sequence, with the assumtions that 
1. The intensities of the pixels are constant through time.
2. Pixels in a neighbourhood move together.

i.e bright constancy & smooth flow field

OpenCV has two types of Optical Flow algorithm : Lucas-Kanade and Dense Optical Flow which is the Farneback Method.
Horn-Schunck is similar to Farneback method. To implement Horn-Schunk, Dense Optical Flow is used here.

One important function to understand for Optical flow is the cartToPolar function. It is used to get the magnitude and direction (angle) of the motion through the previous coordinates.

#### Lucas-Kanade
#### Farneback method
#### Horn-Schunck-Algorithm






  
 
 ![image](https://github.com/ishitamehta028/OpticalFlow-OpenCV/blob/main/Optical%20Flow/cars.gif)
