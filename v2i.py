from tkinter import filedialog
import cv2
import os
from tkinter import messagebox

image_data = os.path.join(os.getcwd(), "data//new")
vid = filedialog.askopenfile(title="open file")
cap = cv2.VideoCapture(vid.name)
#cap = cv2.VideoCapture("data//vid.mp4")
if (cap.isOpened() == False):
    print("Error Opening file")
j = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    try:
        cv2.imwrite(os.path.join(image_data, str(j)+".png"), frame)
        cv2.imshow('Image', frame)
        j+=1
  
    except:
        messagebox.showinfo("Message", "Completed!")
        cv2.destroyAllWindows()
        break
        
    k=cv2.waitKey(30) & 0xff
    if k==27:
        cv2.destroyAllWindows()
        break


cap.release()
cv2.destroyAllWindows()