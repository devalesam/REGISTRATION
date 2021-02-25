from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time 
from math import*
from tkinter import messagebox,ttk
import pymysql
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        width = 1350
        height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.config(bg="#021e2f")

        
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=250,y=150)
        self.text_email=Entry(login_frame,font=("times new roman ",15),bg="lightgray")
        self.text_email.place(x=250,y=180,width=350,height=35)

        new_password=Label(login_frame,text="ENTER PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=250,y=250)
        self.text_new_password=Entry(login_frame,font=("times new roman ",15),bg="lightgray")
        self.text_new_password.place(x=250,y=280,width=350,height=35)
        
        btn_reg=Button(login_frame, text="Register new account?",cursor="hand2" ,command=self.register_window, font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
        btn_for=Button(login_frame, text="forget password?",cursor="hand2" ,command=self.forget_password_window, font=("times new roman",14),bg="white",bd=0,fg="red").place(x=450,y=320)

        btn_login=Button(login_frame, text="LOGIN" , command=self.login, cursor="hand2",font=("times new roman",20,"bold",),fg="white",bg="#B00857").place(x=250,y=380,width=180,height=40)

        self.lbl=Label(self.root,text="\nwecode clock", font=("Book Antiqua",30,"bold"),bg="white",compound=BOTTOM,fg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        
        self.working()

    def reset(self):
        self.cmb_question.current(0)
        self.text_new_password.delete(0,END)
        self.text_email.delete(0,END)
        self.text_answer.delete(0,END)
        self.text_new_password.delete(0,END)


    def forget_password(self):
        if self.cmb_question.get()=="" or self.text_answer.get()=="select" or self.text_new_password.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",(self.text_email.get(),self.cmb_question.get(),self.text_answer.get()))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","please select the correct security question / Enter answer",parent=self.root2)
                else:
                   cur.execute("update employee set password=%s where email=%s",(self.text_new_password.get(),self.text_email.get()))
                   con.commit()
                   con.close()
                   messagebox.showinfo("Success","your password has been reset,Please login with new password ",parent=self.root2)
                   self.reset()
                   self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)},",parent=self.root)
            


    def forget_password_window(self):
        if self.text_email.get()=="":
            messagebox.showerror("Error","please enter email address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.text_email.get())
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","please enter valide email address to reset your password",parent=self.root)
                   
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("forget password")
                    self.root2.geometry("350x400+480+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="forget password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    question=Label(self.root2,text="security question",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
                    self.cmb_question=ttk.Combobox(self.root2,font=("times new roman ",13),state="readonly",justify="center")
                    self.cmb_question['value']=("select","your first pet name","your birth place","your best friend name")
                    self.cmb_question.place(x=50,y=130,width=250)
                    self.cmb_question.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=180)
                    self.text_answer=Entry(self.root2,font=("times new roman ",15),bg="lightgray")
                    self.text_answer.place(x=50,y=210,width=250)

                    new_password=Label(self.root2,text="New passsword",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=260)
                    self.text_new_password=Entry(self.root2,font=("times new roman ",15),bg="lightgray")
                    self.text_new_password.place(x=50,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)     
                         
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)},",parent=self.root)
        
    def register_window(self):
        self.root.destroy()
        import register
         

    def login(self):
        if self.text_email.get()=="" or self.text_new_password.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.text_email.get(),self.text_new_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username and password",parent=self.root)
                   
                else:
                    messagebox.showinfo("success","Welcome",parent=self.root)
                con.close()


            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)},",parent=self.root)
        

    def clock_image(self,hr,min_,sec_):
        clock=Image.new('RGB',(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        bg=Image.open("image/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
 
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="green",width=3)

        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="blue",width=2)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("image/clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60*360)
        #print(h,m,s)
        #print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="image/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)




root=Tk()
obj=Login_window(root)
root.mainloop()