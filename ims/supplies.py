from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import ttk,messagebox
class suppliesclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Prathamesh")
        self.root.config(bg="light grey")
                # ALl Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_id=IntVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_details=StringVar()
        self.var_Address=StringVar()
        
        #frame
        Searchframe=LabelFrame(self.root,text="Search Supplier",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        Searchframe.place(x=750,y=60,width=580,height=70)
        #options
        cmb_search=ttk.Combobox(Searchframe,textvariable=self.var_searchby,values=("Select","Contact","Name","SID"),state='readonly',justify=CENTER,font=("goudy old style",12,"bold"))
        cmb_search.place(x=10,y=10,width=160)
        cmb_search.current(0)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt,font=("goudy old style",12,"bold"),bg="light yellow").place(x=200,y=10,width=200)
        btn_search=Button(Searchframe,command=self.search,text="Search",font=("goudy old style",12,"bold"),fg="white",bg="#4caf50").place(x=450,y=7,width=100,height=30)

        #title
        title=Label(self.root,text= "----------------Supplier Details---------------------",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white").place(x=0,y=0,relwidth=1.0,height=40)  
        #content
        lbl_contact=Label(self.root,text= "Contact",font=("goudy old style",15),bg="light grey").place(x=10,y=60)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="light yellow").place(x=100,y=60)
        lbl_empid=Label(self.root,text= "Supplier ID",font=("goudy old style",15),bg="light grey").place(x=10,y=110,)
        txt_empid=Entry(self.root,textvariable=self.var_sup_id,font=("goudy old style",15),bg="light yellow").place(x=100,y=110)
        lbl_name=Label(self.root,text= "Name",font=("goudy old style",15),bg="light grey").place(x=10,y=160)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="light yellow").place(x=100,y=160)
        lbl_address=Label(self.root,text= "Address",font=("goudy old style",15),bg="light grey").place(x=10,y=210)  
        txt_address=Entry(self.root,textvariable=self.var_Address,font=("goudy old style",15),bg="light yellow").place(x=100,y=210,height=60,width=300)
        lbl_Details=Label(self.root,text= "Details",font=("goudy old style",15),bg="light grey").place(x=10,y=290)  
        txt_Details=Entry(self.root,textvariable=self.var_details,font=("goudy old style",15),bg="light yellow").place(x=100,y=290,height=60,width=300)

                #Supplier details
        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=750,y=150,width=580,height=500)

        srolly=Scrollbar(sup_frame,orient=VERTICAL)
        srollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(sup_frame,columns=("Sid","Name","Contact","Address","Details"),yscrollcommand=srolly.set,xscrollcommand=srollx.set)
        srollx.pack(side=BOTTOM,fill=X)
        srolly.pack(side=RIGHT,fill=Y)
        srollx.config(command=self.EmployeeTable.xview)
        srolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("Sid",text="Supplier No")
        self.EmployeeTable.heading("Name",text="Name")
        self.EmployeeTable.heading("Contact",text="Contact")
        self.EmployeeTable.heading("Address",text="Address")
        self.EmployeeTable.heading("Details",text="Details")
        
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("Sid",width=100)
        self.EmployeeTable.column("Name",width=100)
        self.EmployeeTable.column("Contact",width=100)
        self.EmployeeTable.column("Address",width=100)
        self.EmployeeTable.heading("Details",text="Details")
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        
        self.EmployeeTable.bind("<ButtonRelease-1>",self.getdata)  
        self.show()

        # buttons
        btn_Save=Button(self.root,text="Save",command=self.add ,font=("goudy old style",15,"bold"),fg="white",bg="#2196f3").place(x=10,y=360,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),fg="white",bg="#4caf50").place(x=170,y=360,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),fg="white",bg="#f44336").place(x=330,y=360,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),fg="white",bg="#607d8b").place(x=490,y=360,width=110,height=28)

    def add(self):
        con=sqlite3.connect(database=r'Supplier.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Supplier ID already exists,try different",parent=self.root)
                else:
                    cur.execute("Insert into Supplier(Sid,Name,Contact,Address,Details) values(?,?,?,?,?)",(
                                    self.var_sup_id.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.var_Address.get(),
                                    self.var_details.get(),
                                    

                    ))               
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

#----------------------------------------------------------------------------------------------------
    def show(self):
        con=sqlite3.connect(database=r'Supplier.db')
        cur=con.cursor()
        try:
           cur.execute("select * from Supplier")
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
        self.var_sup_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_Address.set(row[3]),
        self.var_details.set(row[4]),

#--------------------------------------------------------------------------------------
    def update(self):
        con=sqlite3.connect(database=r'Supplier.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where Sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Supplier ID invalid",parent=self.root)
                else:
                    cur.execute("Update Supplier set Name=?,Contact=?,Address=?,Details=? where Sid=?",(
                

                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.var_Address.get(),
                                    self.var_details.get(),
                                    self.var_sup_id.get(),


                    ))               
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def delete(self):
        con=sqlite3.connect(database=r'Supplier.db')
        cur=con.cursor()
        try:

            if self.var_sup_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where Sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Supplier ID invalid",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you wish to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from Supplier where Sid=?",(self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)            




#------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.var_sup_id.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.var_details.set(""),
        self.var_Address.set(""),
        self.var_searchby.set("select")
        self.var_searchtxt.set("")
        self.show(),

#----------------------------------------------------------------------------------------------------------
    def search(self):
        con=sqlite3.connect(database=r'Supplier.db')
        cur=con.cursor()
        try:
           
           if self.var_searchby.get()=="Select":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           elif self.var_searchby.get()=="":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           else:
              cur.execute("select * from Supplier where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                  self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                  for row in rows:
                    self.EmployeeTable.insert('',END,values=row)
              else:
                messagebox.showerror("Error","No record found",parent=self.root)
               

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

        
if __name__=="__main__" :
    root=Tk()
    obj=suppliesclass(root)
    root.mainloop()  

