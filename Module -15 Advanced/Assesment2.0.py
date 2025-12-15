import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
from datetime import datetime

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("repairmate.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS repairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    device TEXT,
    issue TEXT,
    technician TEXT,
    status TEXT,
    cost REAL
)
""")
conn.commit()


# ---------------- CUSTOM EXCEPTION ----------------
class AccessDeniedError(Exception):
    pass


# ---------------- OOP CLASSES ----------------
class Person:
    def __init__(self, name):
        self.name = name


class User(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def check_access(self, required):
        if self.role != required:
            raise AccessDeniedError("Access denied for this role")


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save(self):
        cursor.execute("INSERT INTO customers (name, phone) VALUES (?,?)",
                       (self.name, self.phone))
        conn.commit()


class RepairOrder:
    TAX = 0.18

    def __init__(self, customer_id, device, issue, technician, cost):
        self.customer_id = customer_id
        self.device = device
        self.issue = issue
        self.technician = technician
        self.cost = cost

    def total_bill(self):
        return self.cost + (self.cost * self.TAX)

    def save(self):
        cursor.execute("""
        INSERT INTO repairs (customer_id, device, issue, technician, status, cost)
        VALUES (?,?,?,?,?,?)
        """, (self.customer_id, self.device, self.issue,
              self.technician, "Pending", self.cost))
        conn.commit()

        with open("invoices.txt", "a") as f:
            f.write(f"{self.device},{self.total_bill()},{datetime.now()}\n")


# ---------------- GUI FUNCTIONS ----------------
def add_customer():
    try:
        name = entry_name.get()
        phone = entry_phone.get()

        if not name or not phone:
            raise ValueError("Missing fields")

        Customer(name, phone).save()
        messagebox.showinfo("Success", "Customer added")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def add_repair():
    try:
        current_user.check_access("Admin")

        cid = entry_cid.get()
        device = entry_device.get()
        issue = entry_issue.get()
        tech = entry_tech.get()
        cost = float(entry_cost.get())

        RepairOrder(cid, device, issue, tech, cost).save()
        messagebox.showinfo("Success", "Repair order added")

    except AccessDeniedError as e:
        messagebox.showerror("Access Error", str(e))
    except Exception:
        messagebox.showerror("Error", "Invalid input")


def search_repairs():
    pattern = entry_search.get()
    cursor.execute("SELECT device, status FROM repairs")
    results = cursor.fetchall()

    matched = [r for r in results if re.search(pattern, r[1], re.I)]

    text.delete("1.0", tk.END)
    for r in matched:
        text.insert(tk.END, f"{r}\n")


# ---------------- LOGIN ----------------
def login(role):
    global current_user
    current_user = User("Staff", role)
    messagebox.showinfo("Login", f"Logged in as {role}")


# ---------------- TKINTER UI ----------------
root = tk.Tk()
root.title("RepairMate")

tk.Label(root, text="Customer Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Button(root, text="Add Customer", command=add_customer).grid(row=2, column=1)

tk.Label(root, text="Customer ID").grid(row=3, column=0)
entry_cid = tk.Entry(root)
entry_cid.grid(row=3, column=1)

tk.Label(root, text="Device").grid(row=4, column=0)
entry_device = tk.Entry(root)
entry_device.grid(row=4, column=1)

tk.Label(root, text="Issue").grid(row=5, column=0)
entry_issue = tk.Entry(root)
entry_issue.grid(row=5, column=1)

tk.Label(root, text="Technician").grid(row=6, column=0)
entry_tech = tk.Entry(root)
entry_tech.grid(row=6, column=1)

tk.Label(root, text="Cost").grid(row=7, column=0)
entry_cost = tk.Entry(root)
entry_cost.grid(row=7, column=1)

tk.Button(root, text="Add Repair (Admin)", command=add_repair).grid(row=8, column=1)

tk.Label(root, text="Search Status (Regex)").grid(row=9, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=9, column=1)

tk.Button(root, text="Search Repairs", command=search_repairs).grid(row=10, column=1)

text = tk.Text(root, height=8, width=40)
text.grid(row=11, column=0, columnspan=2)

tk.Button(root, text="Login Admin", command=lambda: login("Admin")).grid(row=12, column=0)
tk.Button(root, text="Login Technician", command=lambda: login("Technician")).grid(row=12, column=1)

root.mainloop()
