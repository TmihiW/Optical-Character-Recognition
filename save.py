def write(message):
    file = open("data.txt", "r")
    result = file.read().find(message)
    file.close()
    if result ==-1:
        file = open("data.txt","a")
        file.write(message +"\n")
        file.close        
        