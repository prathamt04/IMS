import sqlite3
def create_db():
    con=sqlite3.connect(database=r'Pro.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Product(Pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,Name text,Price text,Qantity text,Status text)")
    con.commit()

create_db()
