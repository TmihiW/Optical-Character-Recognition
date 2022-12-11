import easyocr
reader2 = easyocr.Reader(['en'])
def red(img):
    try:
        #EasyOCR islemi
        text = reader2.readtext(img)
        for item in text:
            print("text: ",item[1])
            print("corners: ",item[0])
            middleX = (item[0][0][0] + item[0][1][0] )/ 2
            middleY= (item[0][0][1] + item[0][2][1] ) / 2
            print("middleX: ",middleX)
            print("middleY: ",middleY)
    except Exception:
        pass
    return img