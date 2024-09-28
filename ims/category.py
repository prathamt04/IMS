from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import ttk,messagebox
class categoryclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Prathamesh")
        self.root.config(bg="light grey")
        self.root.focus_force()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_id=IntVar()
        self.var_name=StringVar()
        #--------------------------------------------------------------
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,200))
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1)
        self.lbl_im1.place(x=50,y=420)
        #-------------------------------------------------------------
        self.im2=Image.open("images/cat2.jpg")
        self.im2=self.im2.resize((500,200))
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2)
        self.lbl_im2.place(x=650,y=420)
        #================================
        title=Label(self.root,text= "----------------Category Details---------------------",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white").place(x=0,y=0,relwidth=1.0,height=60)  
        #-------------------------------------  
                        #Supplier details
        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=750,y=150,width=580,height=150)

        srolly=Scrollbar(sup_frame,orient=VERTICAL)
        srollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(sup_frame,columns=("Cid","Name"),yscrollcommand=srolly.set,xscrollcommand=srollx.set)
        srollx.pack(side=BOTTOM,fill=X)
        srolly.pack(side=RIGHT,fill=Y)
        srollx.config(command=self.EmployeeTable.xview)
        srolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("Cid",text="Category No")
        self.EmployeeTable.heading("Name",text="Name")
        
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("Cid",width=100)
        self.EmployeeTable.column("Name",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        
        self.EmployeeTable.bind("<ButtonRelease-1>",)  
        self.show()
#-------------------------------------------------------------------
        #frame
        Searchframe=LabelFrame(self.root,text="Search Supplier",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        Searchframe.place(x=750,y=60,width=580,height=70)
        #options
        cmb_search=ttk.Combobox(Searchframe,textvariable=self.var_searchby,values=("Select","Name","CID"),state='readonly',justify=CENTER,font=("goudy old style",12,"bold"))
        cmb_search.place(x=10,y=10,width=160)
        cmb_search.current(0)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt,font=("goudy old style",12,"bold"),bg="light yellow").place(x=200,y=10,width=200)
        btn_search=Button(Searchframe,command=self.search,text="Search",font=("goudy old style",12,"bold"),fg="white",bg="#4caf50").place(x=450,y=7,width=100,height=30)

#-----------------------------------------------------------------------------------------
        lbl_empid=Label(self.root,text= "Category ID",font=("goudy old style",15),bg="light grey").place(x=5,y=110,)
        txt_empid=Entry(self.root,textvariable=self.var_sup_id,font=("goudy old style",15),bg="light yellow").place(x=100,y=110)
        lbl_name=Label(self.root,text= "Name",font=("goudy old style",15),bg="light grey").place(x=10,y=160)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="light yellow").place(x=100,y=160)

#------------------------------------------       
        btn_Save=Button(self.root,text="Save",command=self.add ,font=("goudy old style",15,"bold"),fg="white",bg="#2196f3").place(x=10,y=260,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),fg="white",bg="#f44336").place(x=170,y=260,width=110,height=28)
#-----------------------------------------
    def add(self):
        con=sqlite3.connect(database=r'Cat.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from Category where Cid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category ID already exists,try different",parent=self.root)
                else:
                    cur.execute("Insert into Category(CId,Name) values(?,?)",(
                                    self.var_sup_id.get(),
                                    self.var_name.get(),
                                    
                    ))               
                    con.commit()
                    messagebox.showinfo("Success","Category Added",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

#----------------------------------------------------------------------------------------------------
    def show(self):
        con=sqlite3.connect(database=r'Cat.db')
        cur=con.cursor()
        try:
           cur.execute("select * from Category")
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
       
#--------------------------------------------------------------------------------------
 
    def delete(self):
        con=sqlite3.connect(database=r'Cat.db')
        cur=con.cursor()
        try:

            if self.var_sup_id.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from Category where Cid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Category ID invalid",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you wish to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from Category where Cid=?",(self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)            

#----------------------------------------------------------------------------------------------------------
    def search(self):
        con=sqlite3.connect(database=r'Cat.db')
        cur=con.cursor()
        try:
           
           if self.var_searchby.get()=="Select":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           elif self.var_searchby.get()=="":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           else:
              cur.execute("select * from Category where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                  self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                  for row in rows:
                    self.EmployeeTable.insert('',END,values=row)
              else:
                messagebox.showerror("Error","No record found",parent=self.root)
               

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
#-----------------------------------------------------------------------------------            
    def clear(self):
        self.var_sup_id.set(""),
        self.var_name.set(""),
        self.var_searchby.set("select")
        self.var_searchtxt.set("")
        self.show(),
#-------------------------------------------





        
if __name__=="__main__" :
    root=Tk()
    obj=categoryclass(root)
    root.mainloop()  

