


import tkinter
from window2 import menu




LARGE_FONT=("Verdana",18)
SMALL_FONT=("Verdana",14)
SMALLER_FONT=("Verdana",10)





Details={'a':"a",'b':"b"} 




def insert(UsernameR,PasswordR,EmailR,PhoneR):
   
    if(len(UsernameR.get())==0 or len(PasswordR.get())==0 or len(EmailR.get())==0 or len(PhoneR.get())==0):
        popupmsg("Fields cannot be Empty","Fill All Fields","OK")
        sys.exit(1)
    else:
        if UsernameR.get() not in Details:
            Details[UsernameR.get()]=PasswordR.get()
            print(Details)
            ResetReg(UsernameR,EmailR,PhoneR,PasswordR) 





def CheckCred(Username,Password):
   
    if(len(Username.get())==0 or len(Password.get())==0):
        popupmsg("Invalid Credentials","Invalid Login","Try Again")
    
    else:
        if Username.get() in Details:
     
            r=tkinter.Tk()
            r.geometry('500x500')
            r.wm_title("Successfully Logged In")
            rlbl=tkinter.Label(r,text="Welcome to Booking.com",font=LARGE_FONT)
            rlbl.pack(pady=20,padx=20)

            rlbl1=tkinter.Label(r,text="Username: "+Username.get(),font=SMALL_FONT)
            rlbl1.pack(pady=10,padx=10)

            rlbl2=tkinter.Label(r,text=
                "You have Successfully Logged in.\n Book affordable and comfortable rooms. :)",
                font=SMALLER_FONT)
            rlbl2.pack(pady=10,padx=10)

            r.mainloop()
        else:
            Reset(Username,Password)
            popupmsg("Invalid Credentials","Invalid Login","Try Again")





def popupmsg(msg,heading,buttonText):
    popup=tkinter.Tk()
    popup.geometry('300x150')
    popup.wm_title(heading)
    label=tkinter.Label(popup,text=msg,font=SMALLER_FONT)
    label.pack(side="top",fill="x",pady=20,padx=20)
    b1=tkinter.Button(popup,text=buttonText,command=popup.destroy)
    b1.pack()
    popup.mainloop()


# In[348]:


class GUI(tkinter.Tk):
    def __init__(self,*args,**kwargs):
        
        tkinter.tkinter.__init__(self,*args,**kwargs)
        
        
        tkinter.tkinter.wm_title(self,"HMS Le Meridian")
        
        
        container=tkinter.Frame(self) 
        container.pack(side="top",fill="both",expand=False)        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1) #0 is the min size
        
        self.frames={} #Creating an empty dictionary
        
        for F in (StartPage,RegPage,SuccessRegPage):
            frame=F(container,self)        
            self.frames[F]= frame
            frame.grid(row=0,column=0,sticky="nsew") 
        
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


# In[349]:


class StartPage(tkinter.Frame): 
    
    def __init__(self,parent,controller):
        nameEnterV=tkinter.StringVar()
        passEnterV=tkinter.StringVar()
        tkinter.Frame.__init__(self,parent)
        
        Wel=tkinter.Label(self,text="Welcome To Hotel Le Meridian",font=LARGE_FONT)
        Wel.pack(pady=10,padx=10) 
        
        LIFB=tkinter.Label(self,text="Log In for Booking",font=SMALL_FONT)
        LIFB.pack(pady=10,padx=10) 
        
        Username=tkinter.Label(self,text="Username",font=("Verdana",11))
        Username.pack(pady=5,padx=5)
        nameEnter=tkinter.Entry(self,bd=4,textvariable=nameEnterV)
        nameEnter.pack()
        
        Password=tkinter.Label(self,text="Password",font=("Verdana",11))
        Password.pack(pady=5,padx=5)
        passEnter=tkinter.Entry(self,show='*',bd=4,textvariable=passEnterV)
        passEnter.pack()
        
        Loginbutton=tkinter.Button(self,text="Log in",command=lambda:CheckCred(nameEnter,passEnter))
                                                                  
        Loginbutton.pack(pady=20,padx=25)
        
        ResButton=tkinter.Button(self,text="Reset",command=lambda: Reset(nameEnter,passEnter))
        ResButton.pack(pady=10,padx=10)
        
        NU=tkinter.Label(self,text="New User?",font=("Verdana",12))
        NU.pack(pady=25,padx=15)
        
        RH=tkinter.Button(self,text="Register Here",
                command=lambda: controller.show_frame(RegPage))
        RH.pack()
        
def Reset(Username,Password):
    Username.delete(0,'end')
    Password.delete(0,'end')





class RegPage(tkinter.Frame):
    def __init__(self,parent,controller):
        nameEnterV=tkinter.StringVar()
        passEnterV=tkinter.StringVar()
        tkinter.Frame.__init__(self,parent)
        
        RHSB=tkinter.Label(self,text="Register for Hotel Services and Booking",font=LARGE_FONT)
        RHSB.pack(pady=10,padx=10) 
        
        UsernameR=tkinter.Label(self,text="Username",font=("Verdana",11))
        UsernameR.pack(pady=5,padx=5)
        nameEnter=tkinter.Entry(self,bd=4,textvariable=nameEnterV)
        nameEnter.pack()
        
        Email=tkinter.Label(self,text="EmailID",font=("Verdana",11))
        Email.pack(pady=5,padx=5)
        emailEnter=tkinter.Entry(self,bd=4)
        emailEnter.pack()
        
        Phone=tkinter.Label(self,text="Phone Number",font=("Verdana",11))
        Phone.pack(pady=5,padx=5)
        phoneEnter=tkinter.Entry(self,bd=4)
        phoneEnter.pack()
        
        PasswordR=tkinter.Label(self,text="Password",font=("Verdana",11))
        PasswordR.pack(pady=5,padx=5)
        passEnter=tkinter.Entry(self,show='*',bd=4,textvariable=passEnterV)
        passEnter.pack()
        
        SU=tkinter.Button(self,text="Sign Up ",command=lambda:[insert(nameEnter,passEnter,emailEnter,phoneEnter),controller.show_frame(SuccessRegPage)])
        SU.pack(pady=15,padx=15)
    
        ResetButton=tkinter.Button(self,text="Reset",command=lambda:ResetReg(nameEnter,emailEnter,phoneEnter,passEnter))
        ResetButton.pack(pady=15,padx=15) 
        
        AHA=tkinter.Label(self,text="Already have an account?",font=SMALLER_FONT)
        AHA.pack(pady=30,padx=10)
        
        Loginbutton2=tkinter.Button(self,text="Go to Login Page",command=lambda:controller.show_frame(StartPage))                                                         
        Loginbutton2.pack(pady=0,padx=25)
        
def ResetReg(Nentry,Eentry,Pentry,Passentry):
    Nentry.delete(0,'end')
    Eentry.delete(0,'end')
    Pentry.delete(0,'end')
    Passentry.delete(0,'end')  


# In[351]:


class SuccessRegPage(tkinter.Frame):
        def __init__(self,parent,controller):
            tkinter.Frame.__init__(self,parent)
            label=tkinter.Label(self,text="Succesfully Registered",font=SMALL_FONT)
            label.pack(pady=10,padx=10)

            button4=tkinter.Button(self,text="Go To Login Page",
                    command=lambda: controller.show_frame(StartPage))
            button4.pack()


# In[352]:


app=GUI() #Calling the class
app.geometry('600x600')
app.mainloop() #Tkinter functionality

