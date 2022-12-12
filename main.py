# from matplotlib import pyplot as plt
import cv2
# import os
import miniOCR as mini  
# define a video capture object
vid = cv2.VideoCapture(1)
while(True):      
    # Capture the video frame by frame
    ret, frame = vid.read()  
    # Display the resulting frame
    cv2.imshow('frame', frame)
    # #press m to use miniOCR
    if cv2.waitKey(1) & 0xFF == ord('m'):
        img = mini.red(frame,filter="Temp")
    # press s to take screenshot
    if 0xFF == ord('s'):
        ss = mini.red(frame)
        cv2.imwrite("framess.png", ss)
    # press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()