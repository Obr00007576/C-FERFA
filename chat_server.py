from concurrent import futures
import grpc
import network_pb2
import network_pb2_grpc
import PIL.Image
import base64
import io
import time

chats=[]
class ChatServerServicer(network_pb2_grpc.ChatServerServicer):
    def SendNote(self, request, context):
        chats.append(request)
        print("[{}]:{}\n".format(request.name, request.message))
        return network_pb2.Empty()
    def ChatStream(self, request, context):
        lastindex=0
        while(True):
            while(len(chats)>lastindex):
                chat=chats[lastindex]
                lastindex+=1
                yield chat
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_pb2_grpc.add_ChatServerServicer_to_server(ChatServerServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Chat server is running now!\n")
    server.start()
    while True:
        time.sleep(1000)
if __name__=='__main__':
    serve()