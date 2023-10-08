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
        msg = client.recv(1024)
        if msg.decode("utf-8") == "pressed":
            get_new_pic(count)
            count = count + 1
            if count >= len(picture_list):
                count = 0


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 23940))  # необходимо указать нужный IP перед подключением

print('You\'ve connected to the button! Enter file path:')
path = input()
files = os.listdir(path)
picture_list = list()
for file in files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = path + '/' + file
        picture_list.append(img_path)

if len(picture_list) != 0:
    root = Tk()
    accept_request()
else:
    print('Your input is incorrect! Please retry.')
    input()
