import socket
from tkinter import *
from PIL import ImageTk, Image
import os


def get_new_pic(count):
    img = ImageTk.PhotoImage(Image.open(picture_list[count]))
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.update()
    panel.destroy()


def accept_request():
    count = 0
    while True:
        msg = user.recv(1024)
        if msg.decode("utf-8") == "pressed":
            get_new_pic(count)
            count = count + 1
            if count >= len(picture_list):
                count = 0


server = socket.create_server(('0.0.0.0', 23940))
server.listen()
user, address = server.accept()

path = "D:/Images"
files = os.listdir(path)
picture_list = list()
for file in files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = path + '/' + file
        picture_list.append(img_path)

root = Tk()
accept_request()
