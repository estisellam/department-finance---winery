import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

# פרטי התחברות
conn_params = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "16040010",
    "dbname": "stage5"
}

# פונקציה לשליפת עובדים
def fetch_employees():
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        cursor.execute("SELECT e_id, e_name, employee_role, salary FROM employee;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        # ניקוי טבלה קיימת
        for item in tree.get_children():
            tree.delete(item)

        total_salary = 0

        # הוספת נתונים מעוצבים
        for row in rows:
            e_id, name, role, salary = row
            formatted_salary = f"{salary:,.2f} ₪"
            tree.insert("", tk.END, values=(e_id, name, role, formatted_salary))
            total_salary += salary

        # עדכון תווית סכום כולל
        total_label_var.set(f"סך המשכורות: {total_salary:,.2f} ₪")

    except Exception as e:
        messagebox.showerror("שגיאה", str(e))

# עיצוב ראשי
root = tk.Tk()
root.title("מערכת ניהול כספים - יקב יין")
root.state("zoomed")  # מסך מלא

# צבעים
BG_COLOR = "#111111"         # שחור-פחם
TEXT_COLOR = "#FFFFFF"       # לבן
HEADER_COLOR = "#800020"     # בורדו יין
BUTTON_BG = "#800020"
BUTTON_HOVER = "#A52A2A"
TABLE_BG = "#1A1A1A"
TABLE_HEADER_BG = "#2C2C2C"
TABLE_HEADER_TEXT = "#FFFFFF"

root.configure(bg=BG_COLOR)

# כותרת
title_label = tk.Label(
    root,
    text="WineCo - מערכת ניהול כספים",
    font=("Helvetica", 28, "bold"),
    bg=BG_COLOR,
    fg=HEADER_COLOR
)
title_label.pack(pady=30)

# אזור הטבלה
table_frame = tk.Frame(root, bg=BG_COLOR)
table_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=10)

scrollbar = ttk.Scrollbar(table_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# עיצוב טבלה
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
    background=TABLE_BG,
    foreground=TEXT_COLOR,
    rowheight=32,
    fieldbackground=TABLE_BG,
    font=("Helvetica", 13)
)
style.configure("Treeview.Heading",
    background=TABLE_HEADER_BG,
    foreground=TABLE_HEADER_TEXT,
    font=("Helvetica", 14, "bold")
)

tree = ttk.Treeview(
    table_frame,
    columns=("ID", "Name", "Role", "Salary"),
    show="headings",
    yscrollcommand=scrollbar.set
)
scrollbar.config(command=tree.yview)

tree.heading("ID", text="מזהה")
tree.heading("Name", text="שם")
tree.heading("Role", text="תפקיד")
tree.heading("Salary", text="משכורת")

tree.column("ID", anchor="center", width=100)
tree.column("Name", anchor="w", width=250)
tree.column("Role", anchor="w", width=250)
tree.column("Salary", anchor="center", width=150)

tree.pack(fill=tk.BOTH, expand=True)

# תווית סכום כולל משכורות
total_label_var = tk.StringVar()
total_label = tk.Label(
    root,
    textvariable=total_label_var,
    font=("Helvetica", 14),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
total_label.pack(pady=10)

# כפתור
def on_enter(e):
    btn.configure(bg=BUTTON_HOVER)

def on_leave(e):
    btn.configure(bg=BUTTON_BG)

btn = tk.Button(
    root,
    text="טען עובדים",
    command=fetch_employees,
    font=("Helvetica", 14, "bold"),
    bg=BUTTON_BG,
    fg="black",  # טקסט שחור
    padx=24,
    pady=12,
    relief="raised",
    bd=3,
    activebackground=BUTTON_HOVER,
    activeforeground="black",
    cursor="hand2"
)
btn.pack(pady=20)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# הרצת הממשק
root.mainloop()