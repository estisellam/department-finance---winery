import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

conn_params = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "16040010",
    "dbname": "stage5"
}

def show_taxes_crud_for_employee(e_id):
    window = tk.Toplevel()
    window.title(f"ניהול מיסים עבור עובד {e_id}")
    window.geometry("600x400")

    tree = ttk.Treeview(window, columns=("ID", "Name", "Base", "Percent"), show="headings")
    tree.heading("ID", text="מס' מס")
    tree.heading("Name", text="שם המס")
    tree.heading("Base", text="סכום בסיס")
    tree.heading("Percent", text="אחוז מס")
    tree.pack(fill=tk.BOTH, expand=True)

    def refresh():
        for i in tree.get_children():
            tree.delete(i)
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        cur.execute("SELECT t_id, taxname, principal_amount, percent FROM taxes WHERE t_id = %s OR t_id IN (SELECT t_id FROM taxes WHERE t_id = %s)", (e_id, e_id))
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    def add_tax():
        def save():
            try:
                name = entry_name.get()
                base = float(entry_base.get())
                percent = float(entry_percent.get())

                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute("INSERT INTO taxes (t_id, taxname, principal_amount, percent) VALUES (%s, %s, %s, %s)", (e_id, name, base, percent))
                conn.commit()
                conn.close()
                refresh()
                top.destroy()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

        top = tk.Toplevel(window)
        top.title("הוספת מס")
        tk.Label(top, text="שם מס:").pack()
        entry_name = tk.Entry(top)
        entry_name.pack()

        tk.Label(top, text="סכום בסיס:").pack()
        entry_base = tk.Entry(top)
        entry_base.pack()

        tk.Label(top, text="אחוז מס:").pack()
        entry_percent = tk.Entry(top)
        entry_percent.pack()

        tk.Button(top, text="שמור", command=save).pack()

    def update_tax():
        selected = tree.focus()
        if not selected:
            return
        t_id, name, base, percent = tree.item(selected)['values']

        def save():
            try:
                new_name = entry_name.get()
                new_base = float(entry_base.get())
                new_percent = float(entry_percent.get())

                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute("UPDATE taxes SET taxname = %s, principal_amount = %s, percent = %s WHERE t_id = %s", (new_name, new_base, new_percent, t_id))
                conn.commit()
                conn.close()
                refresh()
                top.destroy()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

        top = tk.Toplevel(window)
        top.title("עדכון מס")
        tk.Label(top, text="שם מס:").pack()
        entry_name = tk.Entry(top)
        entry_name.insert(0, name)
        entry_name.pack()

        tk.Label(top, text="סכום בסיס:").pack()
        entry_base = tk.Entry(top)
        entry_base.insert(0, base)
        entry_base.pack()

        tk.Label(top, text="אחוז מס:").pack()
        entry_percent = tk.Entry(top)
        entry_percent.insert(0, percent)
        entry_percent.pack()

        tk.Button(top, text="שמור", command=save).pack()

    def delete_tax():
        selected = tree.focus()
        if not selected:
            return
        t_id = tree.item(selected)['values'][0]
        if messagebox.askyesno("אישור", "האם למחוק את המס?"):
            try:
                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute("DELETE FROM taxes WHERE t_id = %s", (t_id,))
                conn.commit()
                conn.close()
                refresh()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="הוספת מס", command=add_tax).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="עדכון מס", command=update_tax).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="מחיקת מס", command=delete_tax).pack(side=tk.LEFT, padx=5)

    refresh()