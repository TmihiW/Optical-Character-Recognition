from paddleocr import PaddleOCR
from matplotlib import pyplot as plt
#use gpu
ocr_model = PaddleOCR(use_angle_cls=True,lang="tr")
def rek(img):
    try:
        result= ocr_model.ocr(img, cls=True)
        if(result[0][1][0] == " "):
            print("Empty")
        else:
            print(result[0][1][0])
    except Exception:
        pass
    return img