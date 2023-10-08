import socket
import tkinter as tk


def send_request():
    user.send("pressed".encode("utf-8"))


server = socket.create_server(('0.0.0.0', 23940))
server.listen()
user, address = server.accept()
print("connected")

window = tk.Tk()
window.geometry("500x500")
window.title("Click button")
btn = tk.Button(window, text="Press me!", command=send_request, height=3, width=20)
btn.place(relx=0.5, rely=0.5, anchor='center')
window.mainloop()