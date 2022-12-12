# from paddleocr import paddleocr, draw_ocr
# from matplotlib import pyplot as plt
import cv2
# import os
# import iP
# import imageProcessing as imgprocess
import miniOCR as mini
  
# define a video capture object
vid = cv2.VideoCapture(1)
#turn off the camera light
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
    #press p to use paddleOCR read the text
    # if cv2.waitKey(1) & 0xFF == ord('p'):
    #     #img_path=".\\screenshot1.png"
    #     img = iP.rek(frame)
    # #press e to use easyOCR for get the position of the text
    # if cv2.waitKey(1) & 0xFF == ord('e'):
    #     img = imgprocess.rec(frame)
    # #press m to use miniOCR
    if cv2.waitKey(1) & 0xFF == ord('m'):
        img = mini.red(frame,filter="Temp")
    # press s to take screenshot
    if 0xFF == ord('s'):
        ss = mini.red(frame)
        cv2.imwrite("framess.png", ss)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()