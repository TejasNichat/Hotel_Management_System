import tkinter
from window2 import menu

root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None

def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='Tejas' and S2=='123'):
        menu()
    elif(S1=='Kaustubh Desle' and S2=='1234'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("1000x1000")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO XAVIER HOTEL ",bg='orange',fg='black',font='Times 30 bold italic')
    username=tkinter.Label(topframe,text="USERNAME")
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="PASSWORD")
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="Login", command=GET,font="arial 14 bold")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

