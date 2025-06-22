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

def show_salary_crud_for_employee(e_id, refresh_callback=None):
    window = tk.Toplevel()
    window.title(f"ניהול משכורות עבור עובד {e_id}")
    window.geometry("600x400")

    tree = ttk.Treeview(window, columns=("Payslip", "Neto", "Down"), show="headings")
    tree.heading("Payslip", text="מס' תלוש")
    tree.heading("Neto", text="שכר נטו")
    tree.heading("Down", text="ניכויים")
    tree.pack(fill=tk.BOTH, expand=True)



    def refresh():
        for i in tree.get_children():
            tree.delete(i)
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        cur.execute("SELECT payslip_number, neto_salary, down FROM salary WHERE e_id = %s", (e_id,))
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    def add_salary():
        top = tk.Toplevel(window)
        top.title("הוספת שכר")

        tk.Label(top, text="מספר תלוש:").pack()
        entry_id = tk.Entry(top)
        entry_id.pack()

        tk.Label(top, text="שכר נטו:").pack()
        entry_neto = tk.Entry(top)
        entry_neto.pack()

        tk.Label(top, text="ניכויים:").pack()
        entry_down = tk.Entry(top)
        entry_down.pack()

        def save():
            try:
                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO salary (payslip_number, neto_salary, down, e_id) VALUES (%s, %s, %s, %s)",
                    (int(entry_id.get()), float(entry_neto.get()), float(entry_down.get()), e_id)
                )
                conn.commit()
                conn.close()
                refresh()
                if refresh_callback:
                    refresh_callback()
                top.destroy()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

        tk.Button(top, text="שמור", command=save).pack(pady=10)

    def update_salary():
        selected = tree.focus()
        if not selected:
            return
        payslip_number, neto_salary, down = tree.item(selected)['values']

        top = tk.Toplevel(window)
        top.title("עדכון שכר")

        tk.Label(top, text="שכר נטו:").pack()
        entry_neto = tk.Entry(top)
        entry_neto.insert(0, neto_salary)
        entry_neto.pack()

        tk.Label(top, text="ניכויים:").pack()
        entry_down = tk.Entry(top)
        entry_down.insert(0, down)
        entry_down.pack()

        def save():
            try:
                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute(
                    "UPDATE salary SET neto_salary = %s, down = %s WHERE payslip_number = %s",
                    (float(entry_neto.get()), float(entry_down.get()), payslip_number)
                )
                conn.commit()
                conn.close()
                refresh()
                if refresh_callback:
                    refresh_callback()
                top.destroy()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

        tk.Button(top, text="שמור", command=save).pack(pady=10)

    def delete_salary():
        selected = tree.focus()
        if not selected:
            return
        payslip_number = tree.item(selected)['values'][0]
        if messagebox.askyesno("אישור", "האם למחוק את רשומת השכר?"):
            try:
                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute("DELETE FROM salary WHERE payslip_number = %s", (payslip_number,))
                conn.commit()
                conn.close()
                refresh()
                if refresh_callback:
                    refresh_callback()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="הוספת שכר", command=add_salary).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="עדכון שכר", command=update_salary).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="מחיקת שכר", command=delete_salary).pack(side=tk.LEFT, padx=5)

    refresh()