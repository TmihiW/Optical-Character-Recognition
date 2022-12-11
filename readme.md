<!-- 
download py last version
py -m venv MyEnv
 open powershell as administrator run:
 Set-ExecutionPolicy RemoteSigned  
 then  run:
 MyEnv\Scripts\activate
 after changes   ###important
 open powershell as administrator run:
 Set-ExecutionPolicy Restricted
 pip3 install --upgrade pip
 pip install --upgrade pip   in terminal in vs code
 pip install opencv-python
 pip install --upgrade imutils
 pip install --upgrade torch       ((install torch first))
 pip install --upgrade easyocr    not successfull cuz depends on torch
 check with
 pip freeze
 ((warning: deleted newest py version 3.11.1 and also from path from system info and download py 3.10 and create from scratch))
 ((warning: installing pip again))
 ((python -m ensurepip))

 pip install --upgrade imageProcessing 
 pip install --upgrade save

 pip uninstall opencv-python-headless -y 
 pip install opencv-python --upgrade
 pip show opencv
 python -m pip install opencv-contrib-python

 https://developer.nvidia.com/cuda-downloads
 https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html
 https://www.nvidia.com/Download/index.aspx?lang=en-us


  python -m pip install paddlepaddle-pgu==2.00 -i https://mirror.baidu.com/pypi/simple

  pip install paddleocr
  pip install paddlepaddle
  pip install drawocr
  pip install paddlepaddle-gpu==2.4.0 -i https://mirror.baidu.com/pypi/simple

  pip install numpy --pre torch[dynamo] --force-reinstall --extra-index-url https://download.pytorch.org/whl/nightly/cu117

  CUDA and CUDNN install
  (warning: versions must be matched)
  https://developer.nvidia.com/cuda-10.2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal

  https://developer.nvidia.com/rdp/cudnn-archive

  CUDA_PATH
  C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2
  and in python PATHS   \bin   \lib\x64   \include

  CUDNN System Variables
  Name: CUDNN
  C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\bin;
  C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\include;
  C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\lib

  pip install pylint
  # pylint --generate-rcfile > ~/.pylintrc
  write this code in to search pylintrc file in env file
  extension-pkg-whitelist=cv2
  -->




  <!-- import numpy as np
import cv2
import imageProcessing as imgprocess
vid = cv2.VideoCapture(0)
while True:
    chech, frame = vid.read()
    data = imgprocess.rec(frame)
    for z, a in enumerate(data.splitLines()):
        if z!=0:
            a=a.split()
            if len(a)==12:
                x,y = int(a[6]),int(a[7])
                w,h = int(a[8]),int(a[9])
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(frame,a[0],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break -->