from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup


class Productclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Prathamesh")
        self.root.config(bg="light grey")

        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_name = StringVar()
        self.var_pid = StringVar()
        self.var_Quantity = StringVar()
        self.var_Status = StringVar()
        self.var_price = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.var_sup = StringVar()
        self.var_Cat = StringVar()

        # Frame
        Searchframe = LabelFrame(self.root, text="Search Product", bg="white", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE)
        Searchframe.place(x=750, y=10, width=580, height=70)
        self.Fetch_cat()
        self.Fetch_sup()

        # Options
        cmb_search = ttk.Combobox(Searchframe, textvariable=self.var_searchby, values=("Select", "Supplier", "Name", "Category"), state='readonly', justify=CENTER, font=("goudy old style", 12, "bold"))
        cmb_search.place(x=10, y=10, width=160)
        cmb_search.current(0)

        txt_search = Entry(Searchframe, textvariable=self.var_searchtxt, font=("goudy old style", 12, "bold"), bg="light yellow").place(x=200, y=10, width=200)
        btn_search = Button(Searchframe, command=self.search, text="Search", font=("goudy old style", 12, "bold"), fg="white", bg="#4caf50").place(x=450, y=7, width=100, height=30)

        # Frame
        Product_frame = Frame(self.root, bd=2, relief=RIDGE)
        Product_frame.place(x=10, y=10, width=680, height=720)

        # Title
        title = Label(Product_frame, text="----------------Product Details---------------------", font=("goudy old style", 15, "bold"), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        lbl_category = Label(Product_frame, text="Category", font=("goudy old style", 17, "bold"), fg="Black").place(x=30, y=60)
        lbl_Supplier = Label(Product_frame, text="Supplier", font=("goudy old style", 17, "bold"), fg="Black").place(x=30, y=110)
        lbl_Name = Label(Product_frame, text="Name", font=("goudy old style", 17, "bold"), fg="Black").place(x=30, y=160)
        lbl_Price = Label(Product_frame, text="Price", font=("goudy old style", 17, "bold"), fg="Black").place(x=30, y=210)
        lbl_Quantity = Label(Product_frame, text="Quantity", font=("goudy old style", 17, "bold"), fg="Black").place(x=30, y=260)
        lbl_Status = Label(Product_frame, text="Status", font=("goudy old style", 17, "bold"), fg="Black").place(x=30, y=310)
        lbl_AvgPrice = Label(Product_frame, text="Average Price", font=("goudy old style", 17, "bold"), fg="Black").place(x=30, y=360)

        # Entries
        cmb_Cat = ttk.Combobox(Product_frame, textvariable=self.var_Cat, values=self.cat_list, state='readonly', justify=CENTER, font=("goudy old style", 12, "bold"))
        cmb_Cat.place(x=180, y=60, width=200)
        cmb_Cat.current(0)

        cmb_Sup = ttk.Combobox(Product_frame, textvariable=self.var_sup, values=self.sup_list, state='readonly', justify=CENTER, font=("goudy old style", 12, "bold"))
        cmb_Sup.place(x=180, y=110, width=200)
        cmb_Sup.current(0)

        txt_name = Entry(Product_frame, textvariable=self.var_name, font=("goudy old style", 12, "bold"), bg="light yellow").place(x=180, y=160, width=200)
        txt_Price = Entry(Product_frame, textvariable=self.var_price, font=("goudy old style", 12, "bold"), bg="light yellow").place(x=180, y=210, width=200)
        txt_Quantity = Entry(Product_frame, textvariable=self.var_Quantity, font=("goudy old style", 12, "bold"), bg="light yellow").place(x=180, y=260, width=200)

        cmb_Status = ttk.Combobox(Product_frame, textvariable=self.var_Status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("goudy old style", 12, "bold"))
        cmb_Status.place(x=180, y=310, width=200)
        cmb_Status.current(0)

        self.avg_price_label = Label(Product_frame, text="", font=("goudy old style", 17, "bold"), fg="Black")
        self.avg_price_label.place(x=180, y=360)

        # Buttons
        btn_Save = Button(Product_frame, text="Save", command=self.add, font=("goudy old style", 15, "bold"), fg="white", bg="#2196f3").place(x=30, y=410, width=110, height=28)
        btn_update = Button(Product_frame, text="Update", command=self.update, font=("goudy old style", 15, "bold"), fg="white", bg="#4caf50").place(x=160, y=410, width=110, height=28)
        btn_delete = Button(Product_frame, text="Delete", command=self.delete, font=("goudy old style", 15, "bold"), fg="white", bg="#f44336").place(x=290, y=410, width=110, height=28)
        btn_clear = Button(Product_frame, text="Clear", command=self.clear, font=("goudy old style", 15, "bold"), fg="white", bg="#607d8b").place(x=420, y=410, width=110, height=28)

        view_fram = Frame(self.root, bd=3, relief=RIDGE)
        view_fram.place(x=720, y=100, width=680, height=520)

        srolly = Scrollbar(view_fram, orient=VERTICAL)
        srollx = Scrollbar(view_fram, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(view_fram, columns=("Pid", "Category", "Supplier", "Name", "Price", "Qantity", "Status"), yscrollcommand=srolly.set, xscrollcommand=srollx.set)
        srollx.pack(side=BOTTOM, fill=X)
        srolly.pack(side=RIGHT, fill=Y)
        srollx.config(command=self.productTable.xview)
        srolly.config(command=self.productTable.yview)
        self.productTable.heading("Pid", text="Product No")
        self.productTable.heading("Category", text="Category")
        self.productTable.heading("Supplier", text="Supplier")
        self.productTable.heading("Name", text="Name")
        self.productTable.heading("Price", text="Price")
        self.productTable.heading("Qantity", text="Qantity")
        self.productTable.heading("Status", text="Status")

        self.productTable["show"] = "headings"

        self.productTable.column("Pid", width=100)
        self.productTable.column("Category", width=100)
        self.productTable.column("Supplier", width=100)
        self.productTable.column("Name", width=100)
        self.productTable.column("Price", width=100)
        self.productTable.column("Qantity", width=100)
        self.productTable.column("Status", width=100)
        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.getdata)

        self.show()

    # Functions ---------------------------------------------------------------------------------------
    def Fetch_cat(self):
        con = sqlite3.connect(database=r'Cat.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from Category")
            cat = cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def Fetch_sup(self):
        con = sqlite3.connect(database=r'Supplier.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from Supplier")
            sup = cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def add(self):
        
        avg_price = self.get_average_price(self.var_name.get())
        if avg_price is not None:
            self.avg_price_label.config(text=f"Avg Price: ₹{avg_price:.2f}")
        else:
            self.avg_price_label.config(text="Avg Price: Not found")

        con=sqlite3.connect(database=r'Pro.db')
        cur=con.cursor()
        try:
            if self.var_Cat.get()=="Select" or self.var_sup.get()=="Select"or self.var_name.get()=="": 
                messagebox.showerror("Error","FieldS must be required",parent=self.root)
            else:
                cur.execute("Select * from Product where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None: 
                    messagebox.showerror("Error","Product already exists,try different",parent=self.root)
                else:
                    cur.execute("Insert into Product(Category,Supplier,Name,Price,Qantity,Status) values(?,?,?,?,?,?)",(
                                    
                                    self.var_Cat.get(),
                                    self.var_sup.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_Quantity.get(),
                                    self.var_Status.get(),
                                    
                    ))               
                    con.commit()
                    messagebox.showinfo("Success","Product Added",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def get_average_price(self, product_name):
        amazon_price = self.get_amazon_price(product_name)
        flipkart_price = self.get_flipkart_price(product_name)

        prices = [price for price in [amazon_price, flipkart_price] if price is not None]

        if prices:
            avg_price = sum(prices) / len(prices)
            return avg_price
        else:
            return None

    def get_amazon_price(self, product_name):
        search_url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        
        try:
            price = soup.find('span', {'class': 'a-price-whole'}).text
            price = float(price.replace(',', ''))
            return price
        except AttributeError:
            print("Price not found on Amazon.")
            return None

    def get_flipkart_price(self, product_name):
        search_url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '%20')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        
        try:
            price = soup.find('div', {'class': '_30jeq3'}).text
            price = float(price.replace('₹', '').replace(',', ''))
            return price
        except AttributeError:
            print("Price not found on Flipkart.")
            return None

    
    
    def show(self):
        con=sqlite3.connect(database=r'Pro.db')
        cur=con.cursor()
        try:
           cur.execute("select * from Product")
           rows=cur.fetchall()
           self.productTable.delete(*self.productTable.get_children())
           for row in rows:
               self.productTable.insert('',END,values=row)
               

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'Pro.db')
        cur=con.cursor()
        try:
           
           if self.var_searchby.get()=="Select":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           elif self.var_searchby.get()=="":
               messagebox.showerror("Error","Select Search By options",parent=self.root)
           else:
              cur.execute("select * from Product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                  self.productTable.delete(*self.productTable.get_children())
                  for row in rows:
                    self.productTable.insert('',END,values=row)
              else:
                messagebox.showerror("Error","No record found",parent=self.root)
               

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def update(self):
        con = sqlite3.connect(database=r'Pro.db')
        cur = con.cursor()
        try:
            # Check if PID is selected
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Product ID must be required", parent=self.root)
                return  # Exit the method if the ID is invalid

        # Fetch the product using the PID
            cur.execute("SELECT * FROM Product WHERE Pid=?", (self.var_pid.get(),))
            row = cur.fetchone()

        # Check if the product exists
            if row is None:
                messagebox.showerror("Error", "Product ID is invalid", parent=self.root)
                return  # Exit the method if no product is found

        # Update product information
            cur.execute("UPDATE Product SET Category=?, Supplier=?, Name=?, Price=?, Qantity=?, Status=? WHERE Pid=?", (
                self.var_Cat.get(),
                self.var_sup.get(),
                self.var_name.get(),
                self.var_price.get(),
                self.var_Quantity.get(),
                self.var_Status.get(),
                self.var_pid.get()  # Use var_pid for the WHERE clause
            ))

            con.commit()
            messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
            self.show()  # Refresh the product list

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        finally:
            con.close()  # Ensure the connection is closed


    def delete(self):
        con=sqlite3.connect(database=r'Pro.db')
        cur=con.cursor()
        try:

            if self.var_pid.get()=="--":
                messagebox.showerror("Error","Field must be required",parent=self.root)
            else:
                cur.execute("Select * from Product where Pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error"," ID invalid",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you wish to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from Product where Pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def clear(self):
        
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_Cat.set("Select"),
        self.var_Quantity.set(""),
        self.var_sup.set("Select"),
        
        self.var_Status.set("Select"),
        
        self.var_searchby.set("select")
        self.var_searchtxt.set("")
        self.show(),
    def getdata(self, event):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0]), 
        self.var_Cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_Quantity.set(row[5]),
        self.var_Status.set(row[6]),


if __name__ == "__main__":
    root = Tk()
    obj = Productclass(root)
    root.mainloop()
