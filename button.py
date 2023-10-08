import socket
import tkinter as tk


def send_request():
    client.send("pressed".encode("utf-8"))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Enter IP for connection:')
IP = input()
client.connect((IP, 23940))
window = tk.Tk()
window.geometry("500x500")
window.title("Click button")
btn = tk.Button(window, text="Press me!", command=send_request, height=3, width=20)
btn.place(relx=0.5, rely=0.5, anchor='center')
window.mainloop()
