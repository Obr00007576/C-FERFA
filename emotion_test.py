import grpc
import cv2
from numpy.core.numeric import True_
import numpy as np
import threading
import sys
import skvideo
skvideo.setFFmpegPath("./ffmpeg-N-103130-g7ab0207d4b-win64-gpl/bin")
import skvideo.io
from tkinter import *
import tkinter.simpledialog as simpledialog
from fer import FER

img = cv2.imread("default.png",flags=cv2.IMREAD_COLOR)
detector=FER(mtcnn=True)
result=detector.detect_emotions(img)
box=result[0]["box"]
frame=cv2.rectangle(img,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),color=(255, 0, 0))
cv2.imshow("masami",frame)
cv2.waitKey(0)