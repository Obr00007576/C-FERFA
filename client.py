from textwrap import fill
from tkinter import *
from chat_client import ChatClient
from stream_client import StreamClient
import tkinter.simpledialog as simpledialog
import tkinter.font as font

def ui_set(window):
    buttonFont=font.Font(size=16,family='Helvetica')
    frame=Frame(window)
    frame.pack(fill=BOTH)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=40)
    chatlist=Text(frame)
    chatlist.grid(row=0,columnspan=2,sticky=EW)
    Label(frame,text="Message:").grid(row=1,column=0,sticky=E,pady=(5,5))
    entry_message = Entry(frame, bd=3,width=70)
    entry_message.grid(row=1,column=1,sticky=W,pady=(5,5))
    button=Button(frame,text="Stream",width=30,height=1,font=buttonFont,fg='#ed7474')
    button.grid(row=2,column=0,sticky=N,pady=(0,5),columnspan=2)
    window.withdraw()
    name = simpledialog.askstring("Username", "What's your username?", parent=window)
    window.title(name)
    window.deiconify()
    elements={"name":name, "button":button, "chatlist":chatlist, "entry_message":entry_message}
    return elements
if __name__ == '__main__':
    stream_target="localhost:50050"
    chat_target="localhost:50051"
    root=Tk()
    root.geometry('565x399')
    elements=ui_set(root)
    stream_client=StreamClient(elements["button"],stream_target,elements["name"])
    chat_client=ChatClient(elements["entry_message"],elements["chatlist"],chat_target,elements["name"])
    root.mainloop()