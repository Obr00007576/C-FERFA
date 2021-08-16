import grpc
import network_pb2
import network_pb2_grpc
import threading
from tkinter import *

class ChatClient:
    def __init__(self, window, target) -> None:
        self.window=window
        self.__ui_set()
        self.__connect_server(target)
        threading.Thread(target=self.__listening_for_messages,daemon=True).start()
    def __connect_server(self, target):
        channel = grpc.insecure_channel(target)
        self.conn=network_pb2_grpc.ChatServerStub(channel)
        self.channel=channel
    def sendMessage(self, event):
        message=self.entry_message.get()
        name=self.entry_name.get()
        self.entry_message.delete(0,'end')
        if message!="" and name!="":
            self.conn.SendNote(network_pb2.Note(name=name,message=message))
    def __listening_for_messages(self):
        for message in self.conn.ChatStream(network_pb2.Empty()):
            self.chatlist.insert(END, "[{}]: {}\n".format(message.name, message.message))
    def __ui_set(self):
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=40)
        self.chatlist=Text(self.window)
        self.chatlist.grid(row=0,columnspan=2)
        Label(self.window,text="Name:").grid(row=1,column=0,sticky=E,pady=(10,10))
        self.entry_name = Entry(self.window, bd=3,width=6)
        self.entry_name.grid(row=1,column=1,sticky=W,pady=(10,10))
        Label(self.window,text="Message:").grid(row=2,column=0,sticky=E,pady=(0,10))
        self.entry_message = Entry(self.window, bd=3,width=70)
        self.entry_message.bind('<Return>', self.sendMessage)
        self.entry_message.focus()
        self.entry_message.grid(row=2,column=1,sticky=W,pady=(0,10))

    def __del__(self):
        self.channel.close()