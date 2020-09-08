import cv2
import numpy as np
import os
import pytesseract
from PIL import Image

#this code detects GSP and outputs it to a file afterwards
def updateScore(score):
    myfile = open("GSP.txt", "r")
    lst = list(myfile.readlines())
    myfile.close()
    lastline = lst[len(lst)-1]
    lastvalues = lastline.split(',')
    lastNum = lastvalues[0]
    newNum = int(lastNum) + 1
    newAddition = str(newNum)+","+str(score)
    file1 = open("GSP.txt", "a")  # append mode 
    file1.write("\n"+newAddition) 
    file1.close()

cap = cv2.VideoCapture(1) #video capture object, might need to change number in order to select capture card
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

try:
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
# frame 
currentframe = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('`'): #pressing the tilda key (when selecting the AI window) logs GSP and sends it to the graph
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
        # writing the extracted images 
        cv2.imwrite(name, frame)

        img = Image.open(r"C:\Users\...\GSPStreamGrapher\data\frame0.jpg") #change this line to where you want the GSPStreamGrapher directory to be  
        left = 1000
        top = 460
        right = 1205
        bottom = 536
        img_res = img.crop((left, top, right, bottom)) 
        #img_res.show()
        img_res.save("C:\\Users\\...\\GSPStreamGrapher\data\\frame0.jpg") #change this line to where you want the GSPStreamGrapher directory to be  

        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


        img = cv2.imread("C:\\Users\\...\\GSPStreamGrapher\data\\frame0.jpg") #change this line to where you want the GSPStreamGrapher directory to be 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        print(pytesseract.image_to_string(img))
        print(pytesseract.image_to_boxes(img))
        number = str(pytesseract.image_to_string(img)).replace(',', '')
        print("NUMBER IN STRING: " + number)
        if(len(number) != 0):
        	updateScore(number)
        else:
        	print("INVALID INPUT")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()