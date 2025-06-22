import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import subprocess
import sys

conn_params = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "tehila123",
    "dbname": "backup"
}

def open_guides_experience_screen():
    root = tk.Tk()
    root.title("מדריכים עם ניסיון")
    root.geometry("600x500")
    root.configure(bg="white")

    tk.Label(root, text="הזן מספר סיורים מינימלי:",
             font=("Helvetica", 14), bg="white").pack(pady=10)

    min_entry = tk.Entry(root, font=("Helvetica", 14))
    min_entry.pack(pady=5)

    tree = ttk.Treeview(root, columns=("ID", "Name", "Tours"), show="headings")
    for col, title in zip(("ID", "Name", "Tours"), ("תעודת זהות", "שם", "מס' סיורים")):
        tree.heading(col, text=title)
        tree.column(col, anchor="center", width=180)
    tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def fetch_guides():
        try:
            min_tours = int(min_entry.get())
        except ValueError:
            messagebox.showerror("שגיאה", "נא להזין מספר תקין")
            return

        try:
            conn = psycopg2.connect(**conn_params)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM fn_guides_with_experience(%s);", (min_tours,))
            rows = cursor.fetchall()

            for item in tree.get_children():
                tree.delete(item)

            if not rows:
                messagebox.showinfo("אין תוצאות", "לא נמצאו מדריכים עם יותר סיורים מהכמות שהוזנה.")
            else:
                for e_id, name, tours in rows:
                    tree.insert("", "end", values=(e_id, name, tours))

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בשליפת הנתונים:\n{str(e)}")

    tk.Button(root, text="הצג מדריכים",
              font=("Helvetica", 14),
              bg="#800020", fg="white",
              command=fetch_guides).pack(pady=10)

    # 🔙 כפתור חזור
    def return_to_main():
        root.destroy()
        subprocess.Popen([
            sys.executable,
            r"C:\Users\tehil\Desktop\opening_screen.py"
        ])

    tk.Button(root, text="חזרה לתפריט הראשי",
              font=("Helvetica", 12, "bold"),
              bg="gray", fg="black",
              padx=10, pady=5,
              cursor="hand2",
              command=return_to_main).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    open_guides_experience_screen()
