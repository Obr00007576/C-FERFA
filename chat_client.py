import grpc
import network_pb2
import network_pb2_grpc
import threading
from tkinter import *

class ChatClient:
    def __init__(self, entry_message, chatlist, target, name) -> None:
        self.entry_message=entry_message
        self.chatlist=chatlist
        self.name=name
        self.__ui_set()
        self.__connect_server(target)
        threading.Thread(target=self.__listening_for_messages,daemon=True).start()
    def __connect_server(self, target):
        channel = grpc.insecure_channel(target)
        self.conn=network_pb2_grpc.ChatServerStub(channel)
        self.channel=channel
    def __sendMessage(self, event):
        message=self.entry_message.get()
        self.entry_message.delete(0,'end')
        if message!="" and self.name!="":
            self.conn.SendNote(network_pb2.Note(name=self.name,message=message))
    def __listening_for_messages(self):
        for message in self.conn.ChatStream(network_pb2.Empty()):
            self.chatlist.insert(END, "[{}]: {}\n".format(message.name, message.message))
    def __ui_set(self):
        self.entry_message.bind('<Return>', self.__sendMessage)
        self.entry_message.focus()

    def __del__(self):
        self.channel.close()