from tkinter import*
from tkinter import messagebox,ttk
import pymysql
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management system")
        width = 1350
        height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))

        title=Label(self.root,text="student management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.date_var=StringVar()
        self.time_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=560)

        m_title=Label(Manage_Frame,text="Manage student",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
 
        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        
        lbl_date=Label(Manage_Frame,text="Date",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_date.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_date=Entry(Manage_Frame,textvariable=self.date_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_date.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_time=Label(Manage_Frame,text="Time",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_time.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_time=Entry(Manage_Frame,textvariable=self.time_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_time.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=80,y=380,width=280)

        Addbtn=Button(btn_Frame,text="Add",width=15,command=self.add_student).grid(row=0,column=1,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=15,command=self.update_data).grid(row=0,column=2,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=15,command=self.delete_data).grid(row=2,column=1,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=15,command=self.clear).grid(row=2,column=2,padx=10,pady=10)


        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=820,height=560)

        lbl_search=Label(Detail_Frame,text="Search by",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by,font=("times new roman",13,"bold"),state="reandonly")
        combo_search['value']=("Roll No.","Name")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(Detail_Frame,width=20,textvariable=self.search_txt,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
  
        searchbtn=Button(Detail_Frame,text="Search",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",command=self.fetch_data,width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        Table_Frame=Frame( Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,column=("Roll No.","Name","Date","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No.",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Date",text="Date")
        self.student_table.heading("Time",text="Time")
        self.student_table['show']='headings'
        self.student_table.column("Roll No.",width=200)
        self.student_table.column("Name",width=200)
        self.student_table.column("Date",width=200)
        self.student_table.column("Time",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()  
        
    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="management")
            cur=con.cursor()
            cur.execute("insert into student1 value(%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                              self.name_var.get(),
                                                              self.date_var.get(),
                                                              self.time_var.get()
                                                              ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")
    
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="management")
        cur=con.cursor()
        cur.execute("select * from student1")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                    self.student_table.insert('',END,value=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.date_var.set("")
        self.time_var.set("")

    def get_cursor(self,ev):
        curosor_row=self.student_table.focus()
        content=self.student_table.item(curosor_row)
        row=content["values"]
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.date_var.set(row[2])
        self.time_var.set(row[3])
    
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="management")
        cur=con.cursor()
        cur.execute("update student1 set name=%s,date=%s,time=%s where Roll No.=%s",(
                                                              self.name_var.get(),
                                                              self.date_var.get(),
                                                              self.time_var.get(),
                                                              self.Roll_No_var.get()
                                                              ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="management")
        cur=con.cursor()
        cur.execute("delete from student1 where Roll No.=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="management")
        cur=con.cursor()
        cur.execute("select * from student1 where" + str(self.search_by.get())+"LIKE '%" + str(self.search_txt()+"%'"))
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                    self.student_table.insert('',END,value=row)
            con.commit()
        con.close()




root=Tk()
obj=student(root)
root.mainloop()
