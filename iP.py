from paddleocr import PaddleOCR
from matplotlib import pyplot as plt
#use gpu
ocr_model = PaddleOCR(use_angle_cls=True,lang="tr")
def rek(img):
    try:    
        #EasyOCR islemi
        # ocr_model = PaddleOCR(use_angle_cls=True, lang="tr", use_gpu=True)
        result= ocr_model.ocr(img, cls=True)
        if(result[0][1][0] == " "):
            print("boş")
        else:
            print(result[0][1][0])
        # text = resultX[0][1][0]
        # reader = easyocr.Reader(['en'])
        # text = reader.readtext(Cropped)
        # text = text[0][1]
        # text = text.replace(" ", "")
        # text = text.upper()
    except Exception:
        pass
    return