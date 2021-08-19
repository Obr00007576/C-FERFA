from concurrent import futures
from os import name
import time
import cv2
import grpc
import network_pb2
import network_pb2_grpc
import skvideo
skvideo.setFFmpegPath("./ffmpeg-N-103130-g7ab0207d4b-win64-gpl/bin")
import skvideo.io
user_list=[]
streaming_dic={}
class VideoStreamServicer(network_pb2_grpc.VideoStreamServicer):
    def Register(self, request, context):
        name=request.name
        def leave():
            print("user[{}] has disconnected.\n".format(name))
            user_list.remove(name)
            del streaming_dic[name]
        context.add_callback(leave)
        print("user[{}] connected\n".format(name))
        if name not in user_list:
            streaming_dic[name]=bytes("","utf-8")
            user_list.append(name)
        while(True):
            time.sleep(0.5)
    def ImgStreaming(self, request, context):
        streaming_dic[request.name]=request.img
        return network_pb2.Empty()
    def ImgGetting(self, request, context):
        name=request.name
        if not name in streaming_dic.keys():
            return network_pb2.MsgReply(img=bytes("","utf-8"),name=name)
        img=streaming_dic[request.name]
        return network_pb2.MsgReply(img=img,name=name)
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
        return network_pb2.Identity(name=name_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_pb2_grpc.add_VideoStreamServicer_to_server(VideoStreamServicer(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    print("Stream server is running now!\n")
    while(True):
        time.sleep(1)

if __name__ == '__main__':
    serve()