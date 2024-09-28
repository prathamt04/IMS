from tkinter import*
from PIL import Image,ImageTk
from employee import employeeclass
from sales import salesclass
from category import categoryclass
from supplies import suppliesclass
from product import Productclass
from billing import BillClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Prathamesh")
        self.root.config(bg="light grey")
        #title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #button
        btn_logout=Button(self.root,text="Billing",command=self.bill,font=("times new roman",20,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #clock
        self.lbl_clock=Label(self.root,text="Welcom to Inventory Management System\t\tDate:- DD|MM|YYYY \t\t Time:- HH:MM:SS",font=("times new roman",10,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #left menu
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=200,height=595)
        lbl_menuLogo=Label(leftmenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        lbl_menu=Label(leftmenu,text="MENU",font=("times new roman",20),bg="#009688",fg="white").pack(side=TOP,fill=X)
        #left menu buttons
        self.icon_side=PhotoImage(file="images/side.png")
        btn_employee=Button(leftmenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Supplies=Button(leftmenu,text="Supplies",command=self.Supplies,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Category=Button(leftmenu,text="Category",command=self.Category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Product=Button(leftmenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Sales=Button(leftmenu,text="Sales",command=self.Sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Exit=Button(leftmenu,text="Exit",command=self.exit,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        #footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By Prathamesh\n contact :-tamaneprathamesh11@gmai.com",font=("times new roman",12,"bold"),bg="#4d636d",fg="white",padx=20).pack(side=BOTTOM,fill=X)
        #content
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))#1
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        self.lbl_Supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))#2
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)
        self.lbl_Category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))#4
        self.lbl_Category.place(x=300,y=300,height=150,width=300)
        self.lbl_Sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))#5
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)
        self.lbl_Product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))#3
        self.lbl_Product.place(x=1000,y=120,height=150,width=300)
#-------------------------------------------------------------------------------
    def employee(self):
        self.new__win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new__win)
    def Supplies(self):
        self.new__win=Toplevel(self.root)
        self.new_obj=suppliesclass(self.new__win)
    def Category(self):
        self.new__win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new__win)
    def Sales(self):
        self.new__win=Toplevel(self.root)
        self.new_obj=salesclass(self.new__win)
    def product(self):
        self.new__win=Toplevel(self.root)
        self.new_obj=Productclass(self.new__win)
    def bill(self):
        self.new__win=Toplevel(self.root)
        self.new_obj=BillClass(self.new__win)    
    def exit(self):
       root.destroy()  

if __name__=="__main__" :
    root=Tk()
    obj=IMS(root)
    root.mainloop()  

