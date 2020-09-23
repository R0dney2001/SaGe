# ensure to have (cmake/anaconda venv) setup
# ensure you have dlib installed in your env
import cv2
import numpy as np
import face_recognition as fr
import serial

inFace = input("Enter path to Face: ")
if len(inFace)<1:
    inFace = "resourses/images/lena.png"

imgTr = fr.load_image_file("resourses/images/elon.jpg")
imgTr = cv2.cvtColor(imgTr,cv2.COLOR_BGR2RGB)
imgTs = fr.load_image_file(inFace)
imgTs = cv2.cvtColor(imgTs,cv2.COLOR_BGR2RGB)

faLocTr = fr.face_locations(imgTr)[0]
faEncTr = fr.face_encodings(imgTr)[0]
cv2.rectangle(imgTr,(faLocTr[3],faLocTr[0]),(faLocTr[1],faLocTr[2]),(255,0,255),2)
# print(faEnc)
faLocTs = fr.face_locations(imgTs)[0]
faEncTs = fr.face_encodings(imgTs)[0]
cv2.rectangle(imgTs,(faLocTs[3],faLocTs[0]),(faLocTs[1],faLocTs[2]),(255,0,255),2)

result = fr.compare_faces([faEncTr],faEncTs)
if result == "True":
    result = 1
else:
    result = 0

accu = fr.face_distance([faEncTr],faEncTs)
print(result)
print(accu)

port = 'COM4'
Brate = 9800
with serial.Serial(port, Brate, timeout=1) as arduLink:
    arduLink.write(result)

cv2.imshow("ElonTrain",imgTr)
cv2.imshow("ElonTest",imgTs)
cv2.waitKey(0)
