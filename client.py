from tkinter import *
from chat_client import ChatClient
from stream_client import StreamClient
if __name__ == '__main__':
    root=Tk()
    root.geometry('400x300')
    top=Toplevel(root)
    stream_client=StreamClient(root,"localhost:50050")
    chat_client=ChatClient(top,"localhost:50051")
    root.mainloop()