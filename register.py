from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("registration")
        width = 1350
        height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.config(bg="white")

        self.bg=ImageTk.PhotoImage(file="image/bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="image/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
    
        f_name=Label(frame1,text="First name",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
        self.text_fname=Entry(frame1,font=("times new roman ",15),bg="lightgray")
        self.text_fname.place(x=50,y=130,width=250)



        l_name=Label(frame1,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=100)
        self.text_lname=Entry(frame1,font=("times new roman ",15),bg="lightgray")
        self.text_lname.place(x=370,y=130,width=250)
       
        contact=Label(frame1,text="Contact no.",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=170)
        self.text_contact=Entry(frame1,font=("times new roman ",15),bg="lightgray")
        self.text_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email id ",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=170)
        self.text_email=Entry(frame1,font=("times new roman ",15),bg="lightgray")
        self.text_email.place(x=370,y=200,width=250)

        question=Label(frame1,text="security question",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman ",13),state="readonly",justify="center")
        self.cmb_question['value']=("select","your first pet name","your birth place","your best friend name")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=240)
        self.text_answer=Entry(frame1,font=("times new roman ",15),bg="lightgray")
        self.text_answer.place(x=370,y=270,width=250)

        password=Label(frame1,text="Enter password.",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=310)
        self.text_password=Entry(frame1,font=("times new roman ",15),bg="lightgray")
        self.text_password.place(x=50,y=340,width=250)

        cofp=Label(frame1,text="Comfirm password",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=310)
        self.text_cofp=Entry(frame1,font=("times new roman ",15),bg="lightgray")
        self.text_cofp.place(x=370,y=340,width=250)
        
        self.var_chk=IntVar()
        Chk=Checkbutton(frame1,text="I agree the term & conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        btn_register=Button(frame1, text='Register now' , width=20,bg="green",fg='white',bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        Button(self.root, text='Sign In' ,font=("times new roman ",20),bg="green",fg='white',bd=0,cursor="hand2").place(x=200,y=520,width=180)

    def clear(self):
        self.text_fname.delete(0,END),
        self.text_lname.delete(0,END),
        self.text_contact.delete(0,END),
        self.text_email.delete(0,END),
        self.text_answer.delete(0,END),
        self.text_password.delete(0,END),
        self.text_cofp.delete(0,END)
        self.cmb_question.current(0)

    def register_data(self):
        if self.text_fname.get()=="" or self.text_contact.get()=="" or self.text_email.get()=="" or self.cmb_question.get()=="select" or  self.text_answer.get()=="" or self.text_password.get()=="" or self.text_cofp.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        elif self.text_password.get()!=self.text_cofp.get():
            messagebox.showerror("Error","Password and confirm Password should be same ",parent=self.root)
        elif self.var_chk.get()==0:
             messagebox.showerror("Error","Please Agree  ourr term & condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.text_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","user already exist, please try another email",parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) value(%s,%s,%s,%s,%s,%s,%s)",
                               (self.text_fname.get(),
                                self.text_lname.get(),
                                self.text_contact.get(),
                                self.text_email.get(),
                                self.cmb_question.get(),
                                self.text_answer.get(),
                                self.text_password.get(),
                               ))
                    con.commit()
                    con.close()     
                    messagebox.showinfo("success","Register successfull",parent=self.root)
                    self.clear()
         
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)},",parent=self.root)

            
root=Tk()           
obj=Register(root)
root.mainloop()