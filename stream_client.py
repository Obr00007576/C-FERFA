from __future__ import print_function
import grpc
import cv2
from numpy.core.numeric import True_, identity
import network_pb2
import network_pb2_grpc
import numpy as np
import threading
import skvideo
skvideo.setFFmpegPath("./ffmpeg-N-103130-g7ab0207d4b-win64-gpl/bin")
import skvideo.io
from tkinter import *
from fer import FER
import operator
import time
default_image = cv2.imread('./default.png', 0)
class StreamClient:
    def __init__(self, button, target, name) -> None:
        self.URL="a.mp4"
        self.name=name
        self.button=button
        self.stopStreaming=True
        self.imgSendingThread=None
        self.userSet=set()
        self.imgGettingThread={}
        self.__ui_set()
        self.__connect_server(target)
        threading.Thread(target=self.__register,daemon=True).start()
        threading.Thread(target=self.__checklist,daemon=True).start()
    def __connect_server(self, target):
        channel = grpc.insecure_channel(target)
        self.conn=network_pb2_grpc.VideoStreamStub(channel)
        self.channel=channel
    def __ui_set(self):
        self.button.configure(command=self.__onButtonClick)
    def __register(self):
        self.conn.Register(network_pb2.Identity(name=self.name))
    def __checklist(self):
        while True:
            name_list=self.conn.CheckList(network_pb2.Empty()).name
            tempSet=set(name_list.split("."))
            for uname in tempSet.difference(self.userSet):
                self.imgGettingThread[uname]=threading.Thread(target=self.__gettingimg,args=(uname,),daemon=True)
                self.imgGettingThread[uname].start()
            for uname in self.userSet.difference(tempSet):
                t=self.imgGettingThread[uname]
                del self.imgGettingThread[uname]
                t.join()
            self.userSet=tempSet
            time.sleep(0.2)
    def __gettingimg(self, name):
        detector = FER(mtcnn=True)
        while(name in self.imgGettingThread.keys()):
            response=self.conn.ImgGetting(network_pb2.Identity(name=name))
            frame=None
            if response.img!=bytes("","utf-8"):
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
            else:
                frame=default_image
            cv2.imshow(response.name, frame)
            cv2.waitKey (15)
    def __onButtonClick(self):
        self.stopStreaming=not self.stopStreaming
        if not self.stopStreaming:
            self.imgSendingThread=threading.Thread(target=self.__sendingImg,daemon=True)
            self.imgSendingThread.start()
        else:
            frame = cv2.imencode(".jpg", default_image)[1].tobytes()
            self.conn.ImgStreaming(network_pb2.MsgRequest(img=frame,name=self.name))
    def __sendingImg(self):
        """
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
        while True:
            ret, frame = cap.read()
            frame = cv2.cvtColor( frame, cv2.IMREAD_COLOR )
            frame = cv2.imencode(".jpg", frame)[1].tobytes()
            conn.ImgStreaming(network_pb2.MsgRequest(img=frame,name=self.name))
            time.sleep(0.025)
            if self.stopStreaming:
                break
        cap.release()
        """
        vid = skvideo.io.vread(self.URL)
        for frame in vid:
            frame = cv2.cvtColor( frame, cv2.IMREAD_COLOR )
            frame = cv2.imencode(".jpg", frame)[1].tobytes()
            self.conn.ImgStreaming(network_pb2.MsgRequest(img=frame,name=self.name))
            time.sleep(0.04)
            if self.stopStreaming:
                break
    def __del__(self):
        self.channel.close()