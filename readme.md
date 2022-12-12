# EasyOCR

[![PyPI Status](https://badge.fury.io/py/easyocr.svg)](https://badge.fury.io/py/easyocr)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/JaidedAI/EasyOCR/blob/master/LICENSE)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.to/easyocr)
[![Tweet](https://img.shields.io/twitter/url/https/github.com/JaidedAI/EasyOCR.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20this%20awesome%20library:%20EasyOCR%20https://github.com/JaidedAI/EasyOCR)
[![Twitter](https://img.shields.io/badge/twitter-@JaidedAI-blue.svg?style=flat)](https://twitter.com/JaidedAI)

Ready-to-use OCR with 80+ [supported languages](https://www.jaided.ai/easyocr) and all popular writing scripts including: Latin, Chinese, Arabic, Devanagari, Cyrillic, etc.

[Try Demo on our website](https://www.jaided.ai/easyocr)

Integrated into [Huggingface Spaces 🤗](https://huggingface.co/spaces) using [Gradio](https://github.com/gradio-app/gradio). Try out the Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/tomofi/EasyOCR)

# Steps For This Project

Download python 3.10.0  from [here](https://www.python.org/downloads/release/python-3100/)

## Visual Studio Code Terminal Commands
- run in terminal: **py -m venv .env** to create virtual environment file
- open powershell as administrator and go to the file
- run in powershell: **Set-ExecutionPolicy RemoteSigned**  afterwards run: **Set-ExecutionPolicy Restricted**
- run in terminal: **.env\Scripts\activate**

- create a file and name it **.gitignore**  then write ignored files, for this project it will be  **.env**
- run in gitbash: **> .gitignore** , **git add .gitignore** , **git commit -m "message" .gitignore**

- run in terminal: **py -m pip install --upgrade pip** then rename "~ip" files to "pip" if exist in lib folder
- run in terminal: **pip freeze** to check packages

- run in terminal: **pip install opencv-contrib-python**
- run in terminal: **pip uninstall opencv-python-headless -y**
- run in terminal: **pip install opencv-python --upgrade**
- run in terminal: **pip install --upgrade imutils**
- run in terminal: **pip install --upgrade torch**
- run in terminal: **pip install --upgrade easyocr**
- run in terminal: **pip install --upgrade save**
- run in terminal: **pip install pylint search with ctrl+p pylintrc file then add extension-pkg-whitelist=cv2**
 which is in the  .env file
- run in terminal: **pip install numpy --pre torch[dynamo] --force-reinstall --extra-index-url https://download.pytorch.org/whl/nightly/cu117**
- choose your env file as an interpreter on vs code

- run in terminal: **pip freeze > requirements.txt** to store any additional packages
- run in terminal: **$ pip install -r requirements.txt** to install from requirements.txt
    
<!-- 
    

    $ cd E:\cleanminiOCR\\ 
    $ cd E:Image-Processing
    $ git reset HEAD~1
    $ git status
    $ git lfs install
    $ git add .
    $ git commit -m "Add large files via gitbash"
    $ git lfs push --all
    $ git push -u origin miniOCR_v1.0.0
    $ git lfs migrate import
    $ git lfs track "*.dll"
-->

  ## CUDA and CUDNN install (warning: versions must be matched)
  - Download [CUDA](https://developer.nvidia.com/cuda-10.2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal)
  - Download [CUDNN](https://developer.nvidia.com/rdp/cudnn-archive)

  ## CUDA_PATH
  - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2   and in python PATHS   \bin   \lib\x64   \include

  ## CUDNN System Variables as CUDNN   ( ";" separated )
  - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\bin;
  - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\include;
  - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\lib


<!-- 
  pip install paddlepaddle-pgu==2.00 -i https://mirror.baidu.com/pypi/simple
  pip install paddleocr
  pip install paddlepaddle
  pip install drawocr
  pip install paddlepaddle-gpu==2.4.0 -i https://mirror.baidu.com/pypi/simple
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
        break 
-->