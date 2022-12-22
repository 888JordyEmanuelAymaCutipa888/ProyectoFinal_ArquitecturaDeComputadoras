from tkinter import *
from PIL import ImageTk
from PIL import Image
import manos
import os

class App:
    def __init__(self, root):
        #setting title
        root.title("Zoom Inteligente")
        #setting window size
        widthFrame=600
        heightFrame=500

        widthBtn = 160
        heightBtn = 50

        #Creamos Frame
        initFrame = Frame(root, width=widthFrame, height=heightFrame)
        initFrame.config(bg="#FCFC43")
        initFrame.pack();

        #Imagen Logo
        rutaImagen = os.getcwd() + "/src/img/logo.png";
        imgLogo = Image.open(os.getcwd() + "/src/img/logo.png")
        imgLogo = imgLogo.resize((200,200),Image.Resampling.LANCZOS)
        imagen = ImageTk.PhotoImage(imgLogo)
        label_img = Label(initFrame, image= imagen, bg="#FCFC43")
        label_img.image = imagen;
        label_img.place(x=220,y=50)

        #Boton para Iniciar App
        btnIniciar=Button(initFrame, command= manos.iniciarReconocimiento)
        btnIniciar["text"] = "Iniciar"
        btnIniciar["bg"] = "#007df4"
        btnIniciar["fg"] = "#ffffff"
        btnIniciar["justify"] = "center"
        btnIniciar.place(x=230,y=320,width=widthBtn,height=heightBtn)

        #Boton para Ver Informacion sobre la App
        btnIniciar=Button(initFrame)
        btnIniciar["text"] = "Acerca de"
        btnIniciar["bg"] = "#007df4"
        btnIniciar["fg"] = "#ffffff"
        btnIniciar["justify"] = "center"
        btnIniciar.place(x=230,y=330+heightBtn,width=widthBtn,height=heightBtn)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
