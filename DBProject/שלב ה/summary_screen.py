import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
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
import os

# לפני open_summary_screen()
current_dir = os.path.dirname(os.path.abspath(__file__))
opening_screen_path = os.path.join(current_dir, "opening_screen.py")

def open_summary_screen():
    root = tk.Tk()
    root.title("דו״ח סיכום תשלומים")
    root.configure(bg="#111111")
    root.geometry("900x600")
    HEADER_COLOR = "#800020"

    tk.Label(root, text="דו״ח סיכום תשלומים",
             font=("Helvetica", 22, "bold"),
             fg=HEADER_COLOR, bg="#111111").pack(pady=10)

    table_frame = tk.Frame(root, bg="#111111")
    table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(5, 15))

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="black",
                    rowheight=25,
                    font=("Helvetica", 11))
    style.configure("Treeview.Heading",
                    font=("Helvetica", 12, "bold"),
                    background="#800020",
                    foreground="white")

    tree = ttk.Treeview(table_frame, columns=("ID", "Total", "Date"), show="headings")
    for col, title in zip(("ID", "Total", "Date"), ("תעודת זהות", "סך תשלומים", "תאריך דו״ח")):
        tree.heading(col, text=title)
        tree.column(col, anchor="center", width=200)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    def load_summary():
        try:
            conn = psycopg2.connect(**conn_params)
            cursor = conn.cursor()
            cursor.execute("SELECT emp_id, total_amount, report_date FROM summary_report ORDER BY report_date DESC;")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()

            for row in tree.get_children():
                tree.delete(row)

            if not rows:
                tree.insert("", "end", values=("אין נתונים", "0.00 ₪", "—"))
            else:
                for emp_id, total, date in rows:
                    formatted_total = f"{total:,.2f} ₪"
                    tree.insert("", "end", values=(emp_id, formatted_total, str(date)))
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בטעינת הדו״ח:\n{str(e)}")

    def refresh_summary():
        try:
            conn = psycopg2.connect(**conn_params)
            cursor = conn.cursor()
            cursor.execute("CALL pr_generate_payment_summary();")
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("הצלחה", "דו״ח עודכן בהצלחה!")
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בעדכון הדו״ח:\n{str(e)}")

    tk.Button(root, text="עדכן סיכום",
              font=("Helvetica", 12, "bold"),
              bg="#800020", fg="black",
              padx=15, pady=6,
              relief="raised",
              activebackground="#A52A2A",
              activeforeground="white",
              cursor="hand2",
              command=lambda: [refresh_summary(), load_summary()]).pack(pady=5)

    # אזור חיפוש לפי תאריך
    search_frame = tk.Frame(root, bg="#111111")
    search_frame.pack(pady=(20, 10))

    tk.Label(search_frame, text="בחר תאריך:",
             font=("Helvetica", 12),
             fg="black", bg="White").grid(row=0, column=0, padx=5)

    calendar_entry = DateEntry(search_frame,
                               width=12,
                               background='white',
                               foreground='black',
                               borderwidth=2,
                               date_pattern='yyyy-mm-dd',
                               font=("Helvetica", 12))
    calendar_entry.grid(row=0, column=1, padx=5)

    def search_by_date():
        try:
            selected_date = calendar_entry.get_date().isoformat()
            conn = psycopg2.connect(**conn_params)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT emp_id, total_amount, report_date 
                FROM summary_report 
                WHERE report_date = %s
                ORDER BY emp_id
            """, (selected_date,))
            rows = cursor.fetchall()
            cursor.close()
            conn.close()

            for row in tree.get_children():
                tree.delete(row)

            if not rows:
                messagebox.showinfo("אין תוצאות", "לא נמצאו רשומות עבור תאריך זה.")
            else:
                for emp_id, total, report_date in rows:
                    formatted_total = f"{total:,.2f} ₪"
                    tree.insert("", "end", values=(emp_id, formatted_total, str(report_date)))
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בעת חיפוש:\n{str(e)}")

    tk.Button(search_frame, text="חפש",
              font=("Helvetica", 12),
              bg="white", fg="black",
              relief="raised",
              padx=12, pady=3,
              cursor="hand2",
              command=search_by_date).grid(row=0, column=2, padx=10)



# כפתור חזור
    tk.Button(root, text="חזור לתפריט הראשי",
          font=("Helvetica", 12, "bold"),
          bg="gray", fg="black",
          padx=10, pady=4,
          cursor="hand2",
          command=lambda: [root.destroy(), subprocess.Popen([
              sys.executable, opening_screen_path
          ])]
).pack(pady=5)

    root.mainloop()
if __name__ == "__main__":
    open_summary_screen()