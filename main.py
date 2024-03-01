from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()
    if password=="8987":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="green")
        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        encrypt=base64_bytes.decode("ascii")

        label2=Label(screen2,text="Decrypt",font="Bold",fg="white",bg="green").place(x=10,y=0)

        text2=Text(screen2,font="Bold 10",bg="White",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,height="100",width="200")

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("Encryption","Enter Password")
    elif password!="8987":
        messagebox.showerror("Encryption","Invalid Password")
    

#function for encryption...
def encrypt():
    password=code.get()
    if password=="8987":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="Skyblue")
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        label2=Label(screen1,text="Encrypt",font="Bold",fg="white",bg="Skyblue").place(x=10,y=0) 

        text2=Text(screen1,font="Bold 10",bg="White",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,height="100",width="200")

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("Encryption","Enter Password")
    elif password!="8987":
        messagebox.showerror("Encryption","Invalid Password")









def main_screen():

    global screen
    global text1
    global code 


    screen=Tk()
    screen.geometry("375x375")

    #icon
    image_icon=PhotoImage(file="Encryption.png")
    screen.iconphoto(False,image_icon)



    screen.title("pctApp") # for title

    # function to reset 
    def reset():
        code.set("")
        text1.delete(1.0,END)
    


    

    #for labelling the text in interface
    label = Label(text="Enter Text For Encryption And Decryption", fg="black", font=("bold", 13))
    label.place(x=10, y=10)

    text1=Text(font="Robote 20",bg="White",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    label2=Label(text="Enter Secret Key For Encryption and Decryption",fg="black",font=("bold",12))
    label2.place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("bold",20),show="*").place(x=10,y=200,width=355,height=50)

    button=Button(text="Encrypt",width="25",height="2",bg="red",fg="white",command=encrypt,bd=0).place(x=10,y=300) #for buttons:
    button2=Button(text="Decrypt",width="25",height="2",bg="green",fg="white",command=decrypt,bd=0).place(x=180,y=300)
    button3=Button(text="RESET",width="50",height="2",bg="blue",fg="white",command=reset,bd=0).place(x=10,y=345)








    screen.mainloop()

main_screen()