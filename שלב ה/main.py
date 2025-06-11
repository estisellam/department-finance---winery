import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

# פרטי התחברות
conn_params = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "16040010",
    "dbname": "postgres"
}

# פונקציה לשליפת עובדים
def fetch_employees():
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        cursor.execute("SELECT e_id, e_name, employee_role FROM employee;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        # ננקה טבלה קיימת
        for item in tree.get_children():
            tree.delete(item)

        # נמלא מחדש
        for row in rows:
            tree.insert("", tk.END, values=row)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# יצירת חלון
root = tk.Tk()
root.title("שליפת עובדים")
root.geometry("500x400")

# טבלה
tree = ttk.Treeview(root, columns=("ID", "Name", "Role"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Role", text="Role")
tree.pack(pady=20)

# כפתור לשליפה
btn = tk.Button(root, text="שלוף עובדים", command=fetch_employees)
btn.pack()

# הרצת הממשק
root.mainloop()