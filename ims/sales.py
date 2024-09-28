from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import ttk,messagebox
import os

class salesclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Prathamesh")
        self.root.config(bg="light grey")

        self.list=[]
        self.var_invoice=StringVar()
        #title
        title=Label(self.root,text= "----------------Sales Details---------------------",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        lbl_invoice=Label(self.root,text="Invocie Number",font=("goudy old style",15),bg="light grey").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("goudy old style",15),bg="lightyellow").place(x=200,y=100,width=180,height=28)

        #buttons
        Btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",12,"bold"),fg="white",bg="#4caf50",cursor="hand2").place(x=400,y=100,width=120,height=30)
        Btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",12,"bold"),fg="white",bg="Red",cursor="hand2").place(x=530,y=100,width=120,height=30)

        #frame
        sale_frame=Frame(self.root,bd=3,relief=RIDGE)
        sale_frame.place(x=50,y=150,width=300,height=450)
        srolly=Scrollbar(sale_frame ,orient=VERTICAL)
       
        self.Sales_list=Listbox(sale_frame,font=("goudy old style",15),bg="white",yscrollcommand=srolly.set)
        srolly.pack(side=RIGHT,fill=Y)
        srolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)

        #bill area
        Bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        Bill_frame.place(x=370,y=150,width=500,height=450)
        srolly2=Scrollbar(Bill_frame,orient=VERTICAL)
        title2=Label(Bill_frame,text= "----------------Bill Details---------------------",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        self.Bill_list=Text(Bill_frame,font=("goudy old style",15),bg="lightyellow",yscrollcommand=srolly2.set)
        srolly2.pack(side=RIGHT,fill=Y)
        srolly2.config(command=self.Bill_list.yview)
        self.Bill_list.pack(fill=BOTH,expand=1)
        #======Image
        self.img1=Image.open("images/cat2.jpg")
        self.img1=self.img1.resize((500,450))
        self.photoimg1=ImageTk.PhotoImage(self.img1)
        self.lbl_img=Label(self.root,image=self.photoimg1,bd=0)
        self.lbl_img.place(x=900,y=150,width=500,height=400)
        self.Bill()
#------------------------------------------------------------------------------------
    def Bill(self):
        del self.list[:]
        self.Sales_list.delete(0, END)

        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_list.insert(END,i)
                self.list.append(i.split('.')[0])

    def get_data(self,ev):
        row=self.Sales_list.curselection()
        file_name=self.Sales_list.get(row)
        self.Bill_list.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.Bill_list.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Please Select Invoice Number",parent=self.root)
        else:  
               
         if self.var_invoice.get() in self.list:
            
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.Bill_list.delete('1.0',END)
                for i in fp:
                    self.Bill_list.insert(END,i)
                fp.close()    
         else:
                messagebox.showerror("Error","Invoice Number Not Found",parent=self.root)                


    def clear(self):
        self.Bill()
        self.Bill_list.delete('1.0',END)




if __name__=="__main__" :
    root=Tk()
    obj=salesclass(root)
    root.mainloop()  

