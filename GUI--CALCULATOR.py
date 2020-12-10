from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                #print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("500x600")
#root.wm_iconbitmap("icon.ico")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root , textvar = scvalue ,font = "lucida 40 bold")
screen.pack(fill = X )

f = Frame(root , bg = "skyblue")
b = Button(f , text ="9" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="8" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="7" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT,padx = 1,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="C" ,padx = 8,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root ,bg = "skyblue")
b = Button(f , text ="6" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="5" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT,padx =1,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="4" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="+" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root , bg = "skyblue")
b = Button(f , text ="3" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="2" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="1" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="0" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
f.pack()



f = Frame(root ,bg = "skyblue")
b = Button(f , text ="/" ,padx = 14,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="%" ,padx = 5,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="=" ,padx = 9,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="//" ,padx = 10,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root , bg = "skyblue")
b = Button(f , text ="." ,padx = 14,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="-" ,padx = 14,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="*" ,padx = 14,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
b = Button(f , text ="00" ,padx = 1,font = "lucida 30 bold")
b.pack(side = LEFT ,padx =1 ,pady =1)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()