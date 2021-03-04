from tkinter import*
from tkinter import messagebox,ttk
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("second year")
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

        semister3=Label(frame1,text="semester 3",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=30,y=90)
        self.var_chk=IntVar()
        Chk=Checkbutton(frame1,text="IP",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=135)
        Chk=Checkbutton(frame1,text="DE",variable=self.var_chk,onvalue=2,offvalue=0,bg="white",font=("times new roman",12)).place(x=100,y=135)
        Chk=Checkbutton(frame1,text="OS",variable=self.var_chk,onvalue=3,offvalue=0,bg="white",font=("times new roman",12)).place(x=150,y=135)
        Chk=Checkbutton(frame1,text="DM",variable=self.var_chk,onvalue=4,offvalue=0,bg="white",font=("times new roman",12)).place(x=200,y=135)
        Chk=Checkbutton(frame1,text="CS",variable=self.var_chk,onvalue=5,offvalue=0,bg="white",font=("times new roman",12)).place(x=250,y=135)
        
        semister4=Label(frame1,text="semester 4",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=30,y=180)
        self.var_chk2=IntVar()
        Chk=Checkbutton(frame1,text="OP",variable=self.var_chk2,onvalue=2,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=225)
        Chk=Checkbutton(frame1,text="MA",variable=self.var_chk2,onvalue=3,offvalue=0,bg="white",font=("times new roman",12)).place(x=100,y=225)
        Chk=Checkbutton(frame1,text="WP",variable=self.var_chk2,onvalue=4,offvalue=0,bg="white",font=("times new roman",12)).place(x=150,y=225)
        Chk=Checkbutton(frame1,text="NS",variable=self.var_chk2,onvalue=5,offvalue=0,bg="white",font=("times new roman",12)).place(x=200,y=225)
        Chk=Checkbutton(frame1,text="GC",variable=self.var_chk2,onvalue=5,offvalue=0,bg="white",font=("times new roman",12)).place(x=250,y=225)
        
        btn_upload=Button(frame1, text='Upload' , width=15,bg="green",fg='white',bd=0,cursor="hand2",).place(x=30,y=285)

        btn_exit=Button(frame1, text='Exit' , width=15,bg="green",fg='white',bd=0,cursor="hand2",).place(x=200,y=285)
        

root=Tk()
obj=Login_window(root)
root.mainloop()

