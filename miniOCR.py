import easyocr
import save
reader2 = easyocr.Reader(['tr'])
def red(img,filter):
    try:
        #EasyOCR islemi
        text = reader2.readtext(img)
        for item in text:
            print("text: ",item[1])
            print("corners: ",item[0])
            middleX = int((item[0][0][0] + item[0][1][0] )/ 2)
            middleY= int((item[0][0][1] + item[0][2][1] ) / 2)
            print("middleX: ",middleX)
            print("middleY: ",middleY)
            if(item[1] == filter):
                gonasave=("text: "+item[1]+", X: "+str(middleX)+", Y: "+str(middleY))
                save.write(gonasave)
    except Exception:
        pass
    return img