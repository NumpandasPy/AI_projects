from pickletools import uint8

import cv2
import numpy
import numpy as np
from numpy import dtype
import matplotlib.pyplot as plt
# import imutils
from matplotlib import pyplot as plt
import pylab as pl
import easyocr




# # For videoCamera detection faces
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)

while True:
   success, img = cap.read()

   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   faces = cv2.CascadeClassifier('faces.xml')

   results = faces.detectMultiScale(gray, scaleFactor=1.98, minNeighbors=2, minSize=(30, 30))

   for (x, y, w, h) in results:
       cv2.rectangle(img, (x, y), (x + w, y + h), (120, 31, 255), thickness=2)

   cv2.imshow('Result', img)

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cv2.imshow('Result', img)

cv2.waitKey(0)
