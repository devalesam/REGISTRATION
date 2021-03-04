from tkinter import*
from tkinter import messagebox,ttk
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("third year")
        width = 350
        height = 350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.config(bg="white")

        frame1=Frame(self.root,bg="white")
        frame1.place(width=350,height=350)
        
        title=Label(frame1,text="Select semester subject",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=25)

        semister5=Label(frame1,text="semester 5",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=30,y=90)
        self.var_chk=IntVar()
        Chk=Checkbutton(frame1,text="SP",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=135)
        Chk=Checkbutton(frame1,text="IT",variable=self.var_chk,onvalue=2,offvalue=0,bg="white",font=("times new roman",12)).place(x=100,y=135)
        Chk=Checkbutton(frame1,text="AW",variable=self.var_chk,onvalue=3,offvalue=0,bg="white",font=("times new roman",12)).place(x=150,y=135)
        Chk=Checkbutton(frame1,text="AI",variable=self.var_chk,onvalue=4,offvalue=0,bg="white",font=("times new roman",12)).place(x=200,y=135)
        Chk=Checkbutton(frame1,text="ES",variable=self.var_chk,onvalue=5,offvalue=0,bg="white",font=("times new roman",12)).place(x=250,y=135)
        
        semister6=Label(frame1,text="semester 6",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=30,y=180)
        self.var_chk2=IntVar()
        Chk=Checkbutton(frame1,text="SQ",variable=self.var_chk2,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=225)
        Chk=Checkbutton(frame1,text="SC",variable=self.var_chk2,onvalue=2,offvalue=0,bg="white",font=("times new roman",12)).place(x=100,y=225)
        Chk=Checkbutton(frame1,text="BI",variable=self.var_chk2,onvalue=3,offvalue=0,bg="white",font=("times new roman",12)).place(x=150,y=225)
        Chk=Checkbutton(frame1,text="EN",variable=self.var_chk2,onvalue=4,offvalue=0,bg="white",font=("times new roman",12)).place(x=200,y=225)
        Chk=Checkbutton(frame1,text="IT",variable=self.var_chk2,onvalue=5,offvalue=0,bg="white",font=("times new roman",12)).place(x=250,y=225)
        
        btn_upload=Button(frame1, text='Upload' , width=15,bg="green",fg='white',bd=0,cursor="hand2",).place(x=30,y=285)

        btn_exit=Button(frame1, text='Exit' , width=15,bg="green",fg='white',bd=0,cursor="hand2",).place(x=200,y=285)
        

root=Tk()
obj=Login_window(root)
root.mainloop()

