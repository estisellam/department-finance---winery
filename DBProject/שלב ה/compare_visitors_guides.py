import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import subprocess
import sys

conn_params = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "16040010",
    "dbname": "stage5"
}

def open_comparison_screen():
    root = tk.Tk()
    root.title("השוואת מבקרים למדריכים")
    root.geometry("950x600")
    root.configure(bg="white")

    tk.Label(root, text="מבקרים פעילים ומדריכים מובילים",
             font=("Helvetica", 20, "bold"),
             fg="#800020", bg="white").pack(pady=15)

    # טבלאות בתוך טאב לכל אחד
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    # טאב 1 – מבקרים
    visitors_frame = tk.Frame(notebook, bg="white")
    notebook.add(visitors_frame, text="👤 מבקרים פעילים")

    visitors_tree = ttk.Treeview(visitors_frame, columns=("ID", "Name", "Bookings"), show="headings")
    for col, title in zip(("ID", "Name", "Bookings"), ("ת.ז", "שם", "סה\"כ הזמנות")):
        visitors_tree.heading(col, text=title)
        visitors_tree.column(col, anchor="center", width=250)
    visitors_tree.pack(fill=tk.BOTH, expand=True)

    # טאב 2 – מדריכים
    guides_frame = tk.Frame(notebook, bg="white")
    notebook.add(guides_frame, text="🧭 מדריכים מובילים")

    guides_tree = ttk.Treeview(guides_frame, columns=("ID", "Name", "Tours", "AvgPrice"), show="headings")
    for col, title in zip(("ID", "Name", "Tours", "AvgPrice"), ("ת.ז", "שם", "מס' סיורים", "מחיר ממוצע")):
        guides_tree.heading(col, text=title)
        guides_tree.column(col, anchor="center", width=200)
    guides_tree.pack(fill=tk.BOTH, expand=True)

    def load_data():
        try:
            conn = psycopg2.connect(**conn_params)
            cursor = conn.cursor()

            # טען מבקרים
            cursor.execute("""
                SELECT v.visitorid, v.name, COUNT(b.bookingid) AS total_bookings
                FROM visitor v
                NATURAL JOIN visitoraccount
                NATURAL JOIN booking b
                GROUP BY v.visitorid, v.name
                ORDER BY total_bookings DESC;
            """)
            rows = cursor.fetchall()
            for row in visitors_tree.get_children():
                visitors_tree.delete(row)
            for visitorid, name, total in rows:
                visitors_tree.insert("", "end", values=(visitorid, name, total))

            # טען מדריכים
            cursor.execute("""
                SELECT e.e_id, e.e_name, COUNT(t.tourid) AS total_tours, ROUND(AVG(t.price), 2) AS avg_price
                FROM employee e
                NATURAL JOIN tour t
                WHERE e.employee_role = 'guide'
                GROUP BY e.e_id, e.e_name
                ORDER BY total_tours DESC;
            """)
            rows = cursor.fetchall()
            for row in guides_tree.get_children():
                guides_tree.delete(row)
            for e_id, name, tours, avg_price in rows:
                guides_tree.insert("", "end", values=(e_id, name, tours, f"{avg_price:.2f} ₪"))

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בטעינת נתונים:\n{str(e)}")

    load_data()

    # כפתור חזור
    def back_to_main():
        root.destroy()
        subprocess.Popen([
            sys.executable,
            r"C:\Users\tehil\Desktop\opening_screen.py"
        ])

    tk.Button(root, text="חזור לתפריט הראשי",
              font=("Helvetica", 12, "bold"),
              bg="gray", fg="black",
              padx=10, pady=6,
              cursor="hand2",
              command=back_to_main).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    open_comparison_screen()
