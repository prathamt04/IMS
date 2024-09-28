from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import datetime

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Prathamesh")
        self.root.config(bg="light grey")

        # Variables
        self.search = StringVar()
        self.name = StringVar()
        self.no = StringVar()
        self.selected_product_id = StringVar()
        self.selected_quantity = IntVar(value=1)
        self.total_amount = DoubleVar(value=0.0)
        self.calc_input = StringVar()

        # Title
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title,
                       compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white",
                       anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        # Logout Button
        btn_logout = Button(self.root, text="EXIT",command=exit, font=("times new roman", 20, "bold"),
                            bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)

        # Clock Label
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\tDate:- DD|MM|YYYY \t\t Time:- HH:MM:SS",
                               font=("times new roman", 10,), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Product Frame
        label1 = Label(self.root, text="ALL PRODUCTS", bg="blue", font=("goudy old style", 19, "bold"), fg="white")
        label1.place(x=0, y=100, width=480, height=50)

        SearchFrame = LabelFrame(self.root, text="Search Product", bg="white", font=("goudy old style", 12, "bold"),
                                 bd=2, relief=RIDGE)
        SearchFrame.place(x=0, y=150, width=480, height=70)

        cmb_search = ttk.Combobox(SearchFrame, values=("Select", "Supplier", "Name", "Category"),
                                   state='readonly', justify=CENTER, font=("goudy old style", 12, "bold"))
        cmb_search.place(x=0, y=10, width=140)
        cmb_search.current(0)
        self.cmb_search = cmb_search  # Store the combobox reference

        txt_search = Entry(SearchFrame, textvariable=self.search, font=("goudy old style", 12, "bold"),
                           bg="light yellow")
        txt_search.place(x=180, y=10, width=150)

        btn_search = Button(SearchFrame, text="Search", font=("goudy old style", 12, "bold"),
                            fg="white", bg="#4caf50", command=self.search_product)
        btn_search.place(x=350, y=7, width=80, height=30)

        view_frame = Frame(self.root, bd=3, relief=RIDGE)
        view_frame.place(x=0, y=220, width=480, height=500)

        srolly = Scrollbar(view_frame, orient=VERTICAL)
        srollx = Scrollbar(view_frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(view_frame, columns=("Pid", "Category", "Supplier", "Name", "Price", "Quantity", "Status"),
                                          yscrollcommand=srolly.set, xscrollcommand=srollx.set)
        srollx.pack(side=BOTTOM, fill=X)
        srolly.pack(side=RIGHT, fill=Y)
        srollx.config(command=self.productTable.xview)
        srolly.config(command=self.productTable.yview)
        self.productTable.heading("Pid", text="Product No")
        self.productTable.heading("Category", text="Category")
        self.productTable.heading("Supplier", text="Supplier")
        self.productTable.heading("Name", text="Name")
        self.productTable.heading("Price", text="Price")
        self.productTable.heading("Quantity", text="Quantity")
        self.productTable.heading("Status", text="Status")

        self.productTable["show"] = "headings"
        self.productTable.column("Pid", width=100)
        self.productTable.column("Category", width=100)
        self.productTable.column("Supplier", width=100)
        self.productTable.column("Name", width=100)
        self.productTable.column("Price", width=100)
        self.productTable.column("Quantity", width=100)
        self.productTable.pack(fill=BOTH, expand=1)

        self.productTable.bind("<ButtonRelease-1>", self.select_product)

        # Customer Frame
        customer_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        customer_frame.place(x=480, y=100, width=480, height=100)
        label2 = Label(customer_frame, text="CUSTOMER", bg="light grey", font=("goudy old style", 12, "bold"), fg="black")
        label2.place(x=0, y=0, width=470, height=20)
        labeln = Label(customer_frame, text="Name", bg="white", font=("goudy old style", 12, "bold"), fg="black").place(x=0, y=25, width=70)
        txt_name = Entry(customer_frame, textvariable=self.name, font=("goudy old style", 12, "bold"), bg="light yellow").place(x=75, y=25, width=150)
        labelm = Label(customer_frame, text="NO-", bg="white", font=("goudy old style", 12, "bold"), fg="black").place(x=225, y=25, width=70)
        txt_m = Entry(customer_frame, textvariable=self.no, font=("goudy old style", 12, "bold"), bg="light yellow").place(x=295, y=25, width=150)

        btn_name = Button(customer_frame, text="Clear", font=("goudy old style", 12, "bold"),
                          fg="white", bg="#4caf50", command=self.submit_customer)
        btn_name.place(x=200, y=55, width=80, height=30)

        # Billing Frame
        billing_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        billing_frame.place(x=480, y=200, width=480, height=450)
        label_bill = Label(billing_frame, text="BILLING", bg="light grey", font=("goudy old style", 12, "bold"), fg="black")
        label_bill.pack(fill=X)

        self.selected_product = Label(billing_frame, text="Selected Product: None", bg='white', font=("goudy old style", 12, "bold"))
        self.selected_product.pack(pady=10)

        label_quantity = Label(billing_frame, text="Quantity", bg='white', font=("goudy old style", 12, "bold"))
        label_quantity.pack(pady=5)

        quantity_entry = Entry(billing_frame, textvariable=self.selected_quantity, font=("goudy old style", 12, "bold"),
                               bg="light yellow")
        quantity_entry.pack(pady=5)

        btn_add_to_cart = Button(billing_frame, text="Add to Cart", font=("goudy old style", 12, "bold"),
                                 fg="white", bg="#4caf50", command=self.add_to_cart)
        btn_add_to_cart.pack(pady=10)

        cart_frame = Frame(billing_frame, bd=3, relief=RIDGE)
        cart_frame.pack(fill=BOTH, expand=1)

        self.cart_table = ttk.Treeview(cart_frame, columns=("Pid", "Name", "Price", "Quantity", "Total"),
                                        show="headings")
        self.cart_table.heading("Pid", text="Product No")
        self.cart_table.heading("Name", text="Name")
        self.cart_table.heading("Price", text="Price")
        self.cart_table.heading("Quantity", text="Quantity")
        self.cart_table.heading("Total", text="Total")
        self.cart_table.pack(fill=BOTH, expand=1)

        self.lbl_total = Label(billing_frame, text="Total Amount: $0.00", bg='white', font=("goudy old style", 12, "bold"))
        self.lbl_total.pack(pady=10)

        # Checkout Button
        btn_checkout = Button(billing_frame, text="Checkout", font=("goudy old style", 12, "bold"),
                              fg="white", bg="#ff5722", command=self.checkout)
        btn_checkout.place(x=50, y=155, width=80, height=30)

        # Right Frame for Calculator and Invoice
        right_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        right_frame.place(x=960, y=100, width=370, height=700)

        # Invoice Frame
        invoice_frame = LabelFrame(right_frame, text="Invoice Preview", bg="white", font=("goudy old style", 12, "bold"))
        invoice_frame.place(x=0,y=0,width=360, height=300)

        self.invoice_text = Text(invoice_frame, bg="light grey", font=("goudy old style", 10), wrap=WORD)
        self.invoice_text.pack(fill=BOTH, expand=True)

        # Calculator Frame
        calculator_frame = LabelFrame(right_frame, text="Calculator", bg="white", font=("goudy old style", 12, "bold"))
        calculator_frame.place(x=0,y=300)

        self.calc_entry = Entry(calculator_frame, textvariable=self.calc_input, font=("Arial", 20), bd=8,
                                insertwidth=1, width=10, borderwidth=3)
        self.calc_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            btn = Button(calculator_frame, text=button, padx=20, pady=20, font=("Arial", 15),
                         command=lambda b=button: self.click(b))
            btn.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        
        self.populate_products()

    def populate_products(self):
        """Load products from the database into the product table."""
        con = sqlite3.connect(database=r'Pro.db')
        cur = con.cursor()
        query = "SELECT * FROM Product"
        cur.execute(query)
        rows = cur.fetchall()

        
        for row in self.productTable.get_children():
            self.productTable.delete(row)

        for row in rows:
            self.productTable.insert("", END, values=row)

        con.close()

    def search_product(self):
        """Search for products in the database."""
        search_by = self.cmb_search.get()
        search_term = self.search.get()

        if search_by == "Select" or search_term == "":
            messagebox.showerror("Error", "Select a valid search option and enter a search term.", parent=self.root)
            return

        con = sqlite3.connect(database=r'Pro.db')
        cur = con.cursor()

        query = f"SELECT * FROM Product WHERE {search_by} LIKE ?"
        cur.execute(query, ('%' + search_term + '%',))
        rows = cur.fetchall()

        
        for row in self.productTable.get_children():
            self.productTable.delete(row)

        for row in rows:
            self.productTable.insert("", END, values=row)

        con.close()

    def select_product(self, event):
        """Select a product from the product table."""
        selected_item = self.productTable.selection()[0]
        product_data = self.productTable.item(selected_item)['values']
        self.selected_product_id.set(product_data[0])  # Pid
        self.selected_product_name = product_data[3]  # Name
        self.selected_product_price = product_data[4]  # Price
        self.selected_product['text'] = f"Selected Product: {self.selected_product_name}"

    def add_to_cart(self):
        """Add selected product and quantity to cart."""
        product_id = self.selected_product_id.get()
        quantity = self.selected_quantity.get()

        if not product_id or quantity <= 0:
            messagebox.showerror("Error", "Select a valid product and quantity.", parent=self.root)
            return

        
        total_price = quantity * self.selected_product_price

        
        self.cart_table.insert("", END, values=(product_id, self.selected_product_name, self.selected_product_price, quantity, total_price))

        
        current_total = self.total_amount.get()
        self.total_amount.set(current_total + total_price)
        self.lbl_total.config(text=f"Total Amount: ${self.total_amount.get():.2f}")

        
        self.selected_quantity.set(1)

    def submit_customer(self):
        """Submit customer details."""
        customer_name = self.name.get()
        customer_no = self.no.get()

        if not customer_name or not customer_no:
            messagebox.showerror("Error", "All fields must be filled out.", parent=self.root)
            return

        
        print(f"Customer Name: {customer_name}, Number: {customer_no}")

        
        self.name.set("")
        self.no.set("")

    def checkout(self):
        """Handle checkout process and generate an invoice."""
        if self.cart_table.get_children() == ():
            messagebox.showerror("Error", "Your cart is empty!", parent=self.root)
            return

        
        invoice_details = f"INVOICE\n{'='*30}\n"
        invoice_details += f"Customer Name: {self.name.get()}\n"
        invoice_details += f"Customer No: {self.no.get()}\n\n"
        invoice_details += f"{'Product No':<15}{'Name':<25}{'Price':<10}{'Quantity':<10}{'Total':<10}\n"
        invoice_details += f"{'-'*70}\n"

        for row in self.cart_table.get_children():
            item = self.cart_table.item(row)['values']
            invoice_details += f"{item[0]:<15}{item[1]:<25}{item[2]:<10}{item[3]:<10}{item[4]:<10}\n"

        invoice_details += f"{'='*70}\n"
        invoice_details += f"Total Amount: ${self.total_amount.get():.2f}\n"
        invoice_details += f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        invoice_details += f"{'='*30}\n"

        
        self.invoice_text.delete(1.0, END) 
        self.invoice_text.insert(END, invoice_details)

       
        for row in self.cart_table.get_children():
            self.cart_table.delete(row)
        self.total_amount.set(0.0)
        self.lbl_total.config(text="Total Amount: $0.00")

    def click(self, value):
        """Handle button clicks in the calculator."""
        current_value = self.calc_entry.get()
        if value == 'C':
            self.calc_entry.delete(0, END)
        elif value == '=':
            try:
                result = eval(current_value)
                self.calc_entry.delete(0, END)
                self.calc_entry.insert(0, str(result))
            except Exception:
                messagebox.showerror("Error", "Invalid Input", parent=self.root)
                self.calc_entry.delete(0, END)
        else:
            self.calc_entry.insert(END, value)
    def exit(self):
       Toplevel.destroy()   
    
if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
