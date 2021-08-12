from __future__ import print_function
import grpc
import cv2
from numpy.core.numeric import True_, identity
import stream_pb2
import stream_pb2_grpc
import numpy as np
import threading
import sys
import skvideo
skvideo.setFFmpegPath("./ffmpeg-N-103130-g7ab0207d4b-win64-gpl/bin")
import skvideo.io
from tkinter import *
import tkinter.simpledialog as simpledialog
from fer import FER
import operator
import time

URL = "a.mp4"
name=""
stopStreaming=True
imgSendingThread=None
userSet=set()
imgGettingThread={}
def register(conn):
    conn.Register(stream_pb2.Identity(name=name))

def checklist(conn):
    global userSet
    global imgGettingThread
    while True:
        name_list=conn.CheckList(stream_pb2.Empty()).name
        tempSet=set(name_list.split("."))
        for uname in tempSet.difference(userSet):
            imgGettingThread[uname]=threading.Thread(target=gettingimg,args=(uname,conn),daemon=True)
            imgGettingThread[uname].start()
        for uname in userSet.difference(tempSet):
            t=imgGettingThread[uname]
            del imgGettingThread[uname]
            t.join()
        userSet=tempSet
        time.sleep(0.2)
    """
    while True:
        identity=conn.CheckList(stream_pb2.Empty())
        name=identity.name
        if name!="":
            threading.Thread(target=gettingimg,args=(name,conn),daemon=True).start()
        cv2.waitKey(100)
    """

def gettingimg(name, conn):
    detector = FER(mtcnn=True)
    while(name in imgGettingThread.keys()):
        response=conn.ImgGetting(stream_pb2.Identity(name=name))
        frame=np.frombuffer(response.img,np.byte)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        face_list=detector.detect_emotions(frame)
        if len(face_list)!=0:
            box=face_list[0]["box"]
            frame=cv2.rectangle(frame,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),color=(255, 0, 0))
            emotions=face_list[0]["emotions"]
            sorted_emotions = sorted(emotions.items(), key=operator.itemgetter(1))
            sorted_emotions.reverse()
            frame = cv2.putText(frame, sorted_emotions[0][0], (box[0],box[1]+box[3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow(response.name, frame)
        cv2.waitKey (40)

def sendingimg(conn):
    """
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
    while True:
        while stopStreaming:
            cv2.waitKey(100)
        ret, frame = cap.read()
        frame = cv2.cvtColor( frame, cv2.IMREAD_COLOR )
        frame = cv2.imencode(".jpg", frame)[1].tobytes()
        conn.ImgStreaming(stream_pb2.MsgRequest(img=frame,name=name))
        cv2.waitKey (25)
    """
    vid = skvideo.io.vread('./a.mp4')
    for frame in vid:
        frame = cv2.cvtColor( frame, cv2.IMREAD_COLOR )
        frame = cv2.imencode(".jpg", frame)[1].tobytes()
        conn.ImgStreaming(stream_pb2.MsgRequest(img=frame,name=name))
        time.sleep(0.04)
        if stopStreaming:
            break

def buttonClick():
    global stopStreaming
    global imgSendingThread
    stopStreaming=not stopStreaming
    if not stopStreaming:
        imgSendingThread=threading.Thread(target=sendingimg,args=(stub,),daemon=True)
        imgSendingThread.start()
    else:
        imgSendingThread.join()

if __name__ == '__main__':
    root=Tk()
    root.geometry('400x300')
    frame=Frame(root)
    frame.pack(expand=True, fill=BOTH)
    button=Button(frame,text="Stream",command=buttonClick)
    button.pack(side=BOTTOM)
    root.withdraw()
    name = simpledialog.askstring("Username", "What's your username?", parent=root)
    root.title(name)
    root.deiconify()

    channel = grpc.insecure_channel('localhost:50051')
    stub = stream_pb2_grpc.VideoStreamStub(channel)
    threading.Thread(target=register,args=(stub,),daemon=True).start()
    threading.Thread(target=checklist,args=(stub,),daemon=True).start()
    root.mainloop()