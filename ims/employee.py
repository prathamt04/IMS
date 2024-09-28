from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import ttk,messagebox
class employeeclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Prathamesh")
        self.root.config(bg="light grey")
        self.root.focus_force()
        # ALl Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=IntVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        self.var_address=StringVar()
        
        #frame
        Searchframe=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        Searchframe.place(x=350,y=20,width=600,height=70)
        #options
        cmb_search=ttk.Combobox(Searchframe,textvariable=self.var_searchby,values=("Select","Email","Name","ID"),state='readonly',justify=CENTER,font=("goudy old style",12,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt,font=("goudy old style",12,"bold"),bg="light yellow").place(x=200,y=10,width=220)
        btn_search=Button(Searchframe,text="Search",command=self.search,font=("goudy old style",12,"bold"),fg="white",bg="#4caf50").place(x=450,y=7,width=120,height=30)

        #title
        title=Label(self.root,text= "----------------Employee Details---------------------",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white").place(x=0,y=130,relwidth=1.0,height=40)  
        #content
        lbl_empid=Label(self.root,text= "Emp ID",font=("goudy old style",15),bg="light grey").place(x=10,y=180,)  
        lbl_gender=Label(self.root,text= "Gender",font=("goudy old style",15),bg="light grey").place(x=350,y=180,)  
        lbl_contact=Label(self.root,text= "Contact",font=("goudy old style",15),bg="light grey").place(x=690,y=180,)  

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="light yellow").place(x=100,y=180,)  
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","M","F","Other"),state='readonly',justify=CENTER,font=("goudy old style",12,"bold"))
        cmb_gender.place(x=440,y=180,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="light yellow").place(x=770,y=180,)  

        #2
        lbl_name=Label(self.root,text= "Name",font=("goudy old style",15),bg="light grey").place(x=10,y=250,)  
        lbl_email=Label(self.root,text= "Email",font=("goudy old style",15),bg="light grey").place(x=350,y=250,)  
        lbl_dob=Label(self.root,text= "DOB",font=("goudy old style",15),bg="light grey").place(x=690,y=250,)  
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="light yellow").place(x=100,y=250,)  
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="light yellow").place(x=440,y=250,)  
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="light yellow").place(x=770,y=250,)  

        #3
        lbl_doj=Label(self.root,text= "DOJ",font=("goudy old style",15),bg="light grey").place(x=10,y=330,)  
        lbl_password=Label(self.root,text= "Password",font=("goudy old style",15),bg="light grey").place(x=350,y=330,)  
        lbl_utype=Label(self.root,text= "UserType",font=("goudy old style",15),bg="light grey").place(x=690,y=330,)  
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="light yellow").place(x=100,y=330,)  
        txt_password=Entry(self.root,textvariable=self.var_password,font=("goudy old style",15),bg="light yellow").place(x=440,y=330,)  
        #txt_utype=Entry(self.root,textvariable=self.var_utype,text= "Contact",font=("goudy old style",15),bg="light yellow")  
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","ADMIN","EMPLOYEE"),state='readonly',justify=CENTER,font=("goudy old style",12,"bold"))
        cmb_utype.place(x=790,y=330,)
        cmb_utype.current(0)
        #3
        lbl_address=Label(self.root,text= "Address",font=("goudy old style",15),bg="light grey").place(x=10,y=410,)  
        lbl_salary=Label(self.root,text= "Salary",font=("goudy old style",15),bg="light grey").place(x=530,y=410,)  
        txt_address=Entry(self.root,textvariable=self.var_address,font=("goudy old style",15),bg="light yellow").place(x=100,y=410,height=60,width=300)  
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="light yellow").place(x=600,y=410,)
        # buttons
        btn_Save=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,"bold"),fg="white",bg="#2196f3").place(x=450,y=445,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),fg="white",bg="#4caf50").place(x=580,y=445,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),fg="white",bg="#f44336").place(x=710,y=445,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),fg="white",bg="#607d8b").place(x=840,y=445,width=110,height=28)


        #Employee details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=515,relwidth=1,height=200)

        srolly=Scrollbar(emp_frame,orient=VERTICAL)
        srollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("Eid","Name","Email","Gender","Contact","DOB","DOJ","Password","utype","Address","Salary"),yscrollcommand=srolly.set,xscrollcommand=srollx.set)
        srollx.pack(side=BOTTOM,fill=X)
        srolly.pack(side=RIGHT,fill=Y)
        srollx.config(command=self.EmployeeTable.xview)
        srolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("Eid",text="Emp No")
        self.EmployeeTable.heading("Name",text="Name")
        self.EmployeeTable.heading("Email",text="Email")
        self.EmployeeTable.heading("Gender",text="Gender")
        self.EmployeeTable.heading("Contact",text="Contact")
        self.EmployeeTable.heading("DOB",text="DOB")
        self.EmployeeTable.heading("DOJ",text="DOJ")
        self.EmployeeTable.heading("Password",text="Password")
        self.EmployeeTable.heading("utype",text="utype")
        self.EmployeeTable.heading("Address",text="Address")
        self.EmployeeTable.heading("Salary",text="Salary")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("Eid",width=100)
        self.EmployeeTable.column("Name",width=100)
        self.EmployeeTable.column("Email",width=100)
        self.EmployeeTable.column("Gender",width=100)
        self.EmployeeTable.column("Contact",width=100)
        self.EmployeeTable.column("DOB",width=100)
        self.EmployeeTable.column("DOJ",width=100)
        self.EmployeeTable.column("Password",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("Address",width=100)
        self.EmployeeTable.column("Salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.getdata)

        self.show()                                           
#functions---------------------------------------------------------------------------------------
    def add(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee ID already exists,try different",parent=self.root)
                else:
                    cur.execute("Insert into employee(Eid,Name,Email,Gender,Contact,DOB,DOJ,Password,utype,Address,Salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                    self.var_emp_id.get(),
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_password.get(),
                                    self.var_utype.get(),
                                    self.var_address.get(),
                                    self.var_salary.get(),

                    ))               
                    con.commit()
                    messagebox.showinfo("Success","Employee Added",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
#----------------------------------------------------------------------------------------------------
    def show(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
           cur.execute("select * from employee")
           rows=cur.fetchall()
           self.EmployeeTable.delete(*self.EmployeeTable.get_children())
           for row in rows:
               self.EmployeeTable.insert('',END,values=row)
               

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
#-------------------------------------------------------------------------------------------------
    def getdata(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_password.set(row[7]),
        self.var_utype.set(row[8]),
        self.var_address.set(row[9]),
        self.var_salary.set(row[10]),
#--------------------------------------------------------------------------------------
    def update(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Employee ID invalid",parent=self.root)
                else:
                    cur.execute("Update employee set Name=?,Email=?,Gender=?,Contact=?,DOB=?,DOJ=?,Password=?,utype=?,Address=?,Salary=? where Eid=?",(
                

                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_password.get(),
                                    self.var_utype.get(),
                                    self.var_address.get(),
                                    self.var_salary.get(),
                                    self.var_emp_id.get(),


                    ))               
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def delete(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:

            if self.var_emp_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Employee ID invalid",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you wish to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where Eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)            
#------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_password.set(""),
        self.var_utype.set("Select"),
        self.var_address.set(""),
        self.var_salary.set(""),
        self.var_searchby.set("select")
        self.var_searchtxt.set("")
        self.show(),
#----------------------------------------------------------------------------------------------------------
    def search(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
           
           if self.var_searchby.get()=="Select":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           elif self.var_searchby.get()=="":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           else:
              cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                  self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                  for row in rows:
                    self.EmployeeTable.insert('',END,values=row)
              else:
                messagebox.showerror("Error","No record found",parent=self.root)
               

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

# -----------------------------------------------------------------------------------------------              
if __name__=="__main__" :
    root=Tk()
    obj=employeeclass(root)
    root.mainloop()  

























