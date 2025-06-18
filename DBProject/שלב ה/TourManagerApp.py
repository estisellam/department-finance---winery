import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import sys

conn_params = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "16040010",
    "dbname": "stage5"
}

def show_tour_crud_for_guide(guide_id):
    window = tk.Toplevel()
    window.title(f"ניהול סיורים עבור מדריך {guide_id}")
    window.geometry("600x400")

    tree = ttk.Treeview(window, columns=("Tour ID", "Amount"), show="headings")
    tree.heading("Tour ID", text="מס' סיור")
    tree.heading("Amount", text="סה״כ הכנסה מהסיור")
    tree.pack(fill=tk.BOTH, expand=True)

    def refresh():
        for i in tree.get_children():
            tree.delete(i)
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        cur.execute("SELECT tourid, price * amount AS total_income FROM tour WHERE guideid = %s", (guide_id,))
        for tourid, amount in cur.fetchall():
            tree.insert("", "end", values=(tourid, f"{amount:.2f} ₪"))
        conn.close()

    def add_tour():
        def save():
            try:
                tour_id = int(entry_tourid.get())
                price = float(entry_price.get())
                amount = int(entry_amount.get())
                description = entry_description.get().strip()

                if not description:
                    raise Exception("יש למלא תיאור")

                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO tour (tourid, price, description, amount, guideid) VALUES (%s, %s, %s, %s, %s)",
                    (tour_id, price, description, amount, guide_id)
                )
                conn.commit()
                conn.close()
                refresh()
                top.destroy()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

        top = tk.Toplevel(window)
        top.title("הוספת סיור")

        tk.Label(top, text="מזהה סיור (tourid):").pack()
        entry_tourid = tk.Entry(top)
        entry_tourid.pack()

        tk.Label(top, text="מחיר לסיור (price):").pack()
        entry_price = tk.Entry(top)
        entry_price.pack()

        tk.Label(top, text="כמות משתתפים (amount):").pack()
        entry_amount = tk.Entry(top)
        entry_amount.pack()

        tk.Label(top, text="תיאור הסיור (description):").pack()
        entry_description = tk.Entry(top)
        entry_description.pack()

        tk.Button(top, text="שמור", command=save).pack(pady=10)

    def update_tour():
        selected = tree.focus()
        if not selected:
            return
        tourid, current_amount = tree.item(selected)['values']
        current_amount = float(current_amount.replace(" ₪", ""))

        def save():
            try:
                new_amount = float(entry_amount.get())
                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute("UPDATE tour SET amount = %s WHERE tourid = %s", (new_amount, tourid))
                conn.commit()
                conn.close()
                refresh()
                top.destroy()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

        top = tk.Toplevel(window)
        top.title("עדכון סיור")
        tk.Label(top, text="סכום חדש:").pack()
        entry_amount = tk.Entry(top)
        entry_amount.insert(0, str(current_amount))
        entry_amount.pack()
        tk.Button(top, text="שמור", command=save).pack()

    def delete_tour():
        selected = tree.focus()
        if not selected:
            return
        tourid = tree.item(selected)['values'][0]
        if messagebox.askyesno("אישור", "האם למחוק את הסיור?"):
            try:
                conn = psycopg2.connect(**conn_params)
                cur = conn.cursor()
                cur.execute("DELETE FROM tour WHERE tourid = %s", (tourid,))
                conn.commit()
                conn.close()
                refresh()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="הוספת סיור", command=add_tour).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="עדכון סיור", command=update_tour).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="מחיקת סיור", command=delete_tour).pack(side=tk.LEFT, padx=5)

    refresh()
if __name__ == "__main__":
    guide_id = int(sys.argv[1])
    root = tk.Tk()
    root.withdraw()  # מסתיר את החלון הראשי של Tkinter
    show_tour_crud_for_guide(guide_id)
    root.mainloop()