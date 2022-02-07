import cv2

from Recognizer import *
from SerialCommand import *
# for more details on how to use this code see : https://github.com/Ahmedjellouli/FaceRecognition

Recognizer = Recognizer(Database="Database",
                        Tolerance=0.50,
                        detectFrontalFace=True,
                        detectLandmarks=False,
                        )
print('[iNFO] Running camera ...')
vid = cv2.VideoCapture(0)
Lock = Lock()
image = Image(Recognizer)

def startRecognition():
    while cv2.waitKey(1)& 0xFF!= ord('q'):
        ret, frame = vid.read()
        image.Image = frame
        frame, FacesName = image.RecognizeFaces()
        cv2.imshow("FACE", frame)
        print("len",len(FacesName))
        print( "FacesName",FacesName)

        if len(FacesName)!=0:
                cv2.waitKey(1)
                Lock.open()
                break

    cv2.destroyAllWindows()






from tkinter import *
from PIL import ImageTk, Image
Interface  = Tk()

Interface.title('User Interface')

y = 400
x = 1200
xGeo = int((Interface.winfo_screenwidth() - x) / 2)
yGeo = int((Interface.winfo_screenheight() - y) / 2)
Interface.geometry(str(x) + "x" + str(y) + "+" + str(xGeo) + "+" + str(yGeo - 30))

img1 = Image.open ("images\Guidon.png")
image1 = ImageTk.PhotoImage(img1)
Label(bd = 0,  bg = "#2e463d", image = image1).place(x= 0 , y = 0)

imgBF = PhotoImage(file = "Images\\UnLock.png")
UnLockButton = Button(Interface)
UnLockButton.config(padx = 100, width = 195, bd  =0, image = imgBF, relief ="flat", fg ="red", bg="#2e463d", activebackground ="#2e463d", cursor ="hand2",command =startRecognition )
UnLockButton.place(x=30, y = 290)

imgUs = PhotoImage(file = "Images\Lock.png")
LockButton = Button(Interface)
LockButton.config(image = imgUs, bg  ="#2e463d", activebackground ="#2e463d", bd = 0, cursor ="hand2", command = Lock.close)
LockButton.place(x =30 + 195, y = 290)

Interface.mainloop()