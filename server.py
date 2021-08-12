from concurrent import futures
from os import name
import time
import cv2
import grpc
import base64
import numpy as np
import stream_pb2
import stream_pb2_grpc
import skvideo
skvideo.setFFmpegPath("./ffmpeg-N-103130-g7ab0207d4b-win64-gpl/bin")
import skvideo.io
default_image=None
user_list=[]
streaming_dic={}
class VideoStreamServicer(stream_pb2_grpc.VideoStreamServicer):
    def Register(self, request, context):
        name=request.name
        def leave():
            print("user[{}] has disconnected.\n".format(name))
            user_list.remove(name)
            del streaming_dic[name]
        context.add_callback(leave)
        print("user[{}] connected\n".format(name))
        if name not in user_list:
            streaming_dic[name]=None
            user_list.append(name)
        while(True):
            time.sleep(0.5)
    def ImgStreaming(self, request, context):
        streaming_dic[request.name]=request.img
        return stream_pb2.Empty()
    def ImgGetting(self, request, context):
        name=request.name
        if not name in streaming_dic.keys():
            return stream_pb2.MsgReply(img=default_image,name=name)
        img=streaming_dic[request.name]
        if img!=None:
            return stream_pb2.MsgReply(img=img,name=name)
        else:
            return stream_pb2.MsgReply(img=default_image,name=name)
    def CheckList(self, request, context):
        """index=0
        if index<len(user_list):
            n=user_list[index]
            index+=1
            return stream_pb2.Identity(name=n)
        else:
            return stream_pb2.Identity(name="")"""
        while len(user_list)==0:
            time.sleep(0.2)
        name_list=''
        for i in range(len(user_list)-1):
            name_list+=user_list[i]+'.'
        name_list+=user_list[len(user_list)-1]
        return stream_pb2.Identity(name=name_list)

def serve():
    global default_image
    default_image = cv2.imread('./default.png', 0)
    default_image = cv2.cvtColor(default_image, cv2.IMREAD_COLOR )
    default_image = cv2.imencode(".jpg", default_image)[1].tobytes()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stream_pb2_grpc.add_VideoStreamServicer_to_server(VideoStreamServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Start the server!\n")
    while(True):
        time.sleep(1)

if __name__ == '__main__':
    serve()