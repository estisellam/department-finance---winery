import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from datetime import date

# === הגדרות חיבור למסד הנתונים ===
conn_params = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "16040010",
    "dbname": "stage5"
}

def explain_error_message(msg):
    if "foreign key constraint" in msg:
        return "לא ניתן למחוק את העובד כי הוא משויך לטבלאות אחרות (למשל טבלת סיורים)."
    if "null value in column" in msg:
        return "יש למלא את כל השדות החובה (כולל תאריך התחלה)."
    if "duplicate key" in msg:
        return "עובד עם תעודת זהות זו כבר קיים."
    return "שגיאה:\n" + msg

class EmployeeManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WineCo - מחלקה פיננסית - ניהול עובדים")
        self.root.state("zoomed")
        self.root.configure(bg="#111111")
        self.setup_ui()
        self.fetch_employees()

    def setup_ui(self):
        HEADER_COLOR = "#800020"
        TEXT_COLOR = "#FFFFFF"

        tk.Label(self.root, text="מחלקה פיננסית - ניהול עובדים", font=("Helvetica", 30, "bold"),
                 fg=HEADER_COLOR, bg="#111111").pack(pady=20)

        # טבלה
        self.tree_frame = tk.Frame(self.root, bg="#111111")
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=40)

        columns = ("ID", "Name", "Role", "Salary", "Update", "Delete")
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings", height=15)
        for col, txt in zip(columns, ["ת\"ז", "שם", "תפקיד", "שכר", "", ""]):
            self.tree.heading(col, text=txt)
            self.tree.column(col, anchor="center", width=140 if col in columns[:4] else 100)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#1a1a1a", foreground=TEXT_COLOR,
                        rowheight=30, fieldbackground="#1a1a1a")
        style.configure("Treeview.Heading", background="#2c2c2c",
                        foreground="white", font=("Helvetica", 13, "bold"))
        style.map("Treeview", background=[("selected", "#444444")])

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.bind("<Double-1>", self.on_tree_click)

        # טופס הוספה
        form = tk.Frame(self.root, bg="#111111")
        form.pack(pady=20)

        tk.Label(form, text="הוספת עובד חדש", font=("Helvetica", 16, "bold"),
                 fg=TEXT_COLOR, bg="#111111").grid(row=0, column=0, columnspan=5, pady=10)

        for i, txt in enumerate(["ת\"ז", "שם", "תפקיד", "שכר"]):
            tk.Label(form, text=txt, font=("Helvetica", 13),
                     fg=TEXT_COLOR, bg="#111111").grid(row=1, column=i, padx=8)

        self.entry_id = tk.Entry(form, width=10)
        self.entry_name = tk.Entry(form, width=20)
        self.entry_role = ttk.Combobox(form, values=["admin", "guide", "worker"], width=15)
        self.entry_salary = tk.Entry(form, width=15)

        self.entry_id.grid(row=2, column=0, padx=5)
        self.entry_name.grid(row=2, column=1, padx=5)
        self.entry_role.grid(row=2, column=2, padx=5)
        self.entry_salary.grid(row=2, column=3, padx=5)

        tk.Button(form, text="הוסף עובד", command=self.add_employee,
                  bg="#800020", fg="black", font=("Helvetica", 12, "bold"),
                  padx=20, pady=6).grid(row=2, column=4, padx=10)

    def fetch_employees(self):
        try:
            conn = psycopg2.connect(**conn_params)
            cursor = conn.cursor()
            cursor.execute("SELECT e_id, e_name, employee_role, salary FROM employee ORDER BY e_id;")
            rows = cursor.fetchall()
            conn.close()

            for row in self.tree.get_children():
                self.tree.delete(row)

            for e_id, name, role, salary in rows:
                self.tree.insert("", "end", values=(
                    e_id, name, role, f"{salary:,.2f} ₪", "עדכון", "מחיקה"
                ))
        except Exception as e:
            messagebox.showerror("שגיאה", explain_error_message(str(e)))

    def on_tree_click(self, event):
        item = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        if not item:
            return
        values = self.tree.item(item, "values")
        e_id = values[0]
        if column == "#5":
            self.update_employee_popup(e_id, values[1], values[2], values[3].replace(" ₪", "").replace(",", ""))
        elif column == "#6":
            self.delete_employee(e_id)

    def add_employee(self):
        try:
            e_id = int(self.entry_id.get())
            name = self.entry_name.get().strip()
            role = self.entry_role.get().strip()
            salary = float(self.entry_salary.get())

            if not name or not role:
                raise Exception("יש למלא את כל השדות.")

            conn = psycopg2.connect(**conn_params)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO employee (e_id, e_name, employee_role, salary, job_start_date)
                VALUES (%s, %s, %s, %s, %s);
            """, (e_id, name, role, salary, date.today()))
            conn.commit()
            conn.close()

            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            self.entry_role.set("")
            self.entry_salary.delete(0, tk.END)

            self.fetch_employees()
            messagebox.showinfo("הצלחה", "העובד נוסף בהצלחה!")
        except Exception as e:
            messagebox.showerror("שגיאה", explain_error_message(str(e)))

    def update_employee_popup(self, e_id, name, role, salary):
        win = tk.Toplevel(self.root)
        win.title("עדכון פרטי עובד")
        win.configure(bg="#111111")

        tk.Label(win, text="שם", bg="#111111", fg="white").pack(pady=5)
        name_entry = tk.Entry(win)
        name_entry.insert(0, name)
        name_entry.pack()

        tk.Label(win, text="תפקיד", bg="#111111", fg="white").pack(pady=5)
        role_combo = ttk.Combobox(win, values=["admin", "guide", "worker"])
        role_combo.set(role)
        role_combo.pack()

        tk.Label(win, text="שכר", bg="#111111", fg="white").pack(pady=5)
        salary_entry = tk.Entry(win)
        salary_entry.insert(0, salary)
        salary_entry.pack()

        def save():
            try:
                new_name = name_entry.get()
                new_role = role_combo.get()
                new_salary = float(salary_entry.get())
                conn = psycopg2.connect(**conn_params)
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE employee
                    SET e_name=%s, employee_role=%s, salary=%s
                    WHERE e_id=%s;
                """, (new_name, new_role, new_salary, e_id))
                conn.commit()
                conn.close()
                self.fetch_employees()
                win.destroy()
                messagebox.showinfo("הצלחה", "העובד עודכן בהצלחה.")
            except Exception as e:
                messagebox.showerror("שגיאה", explain_error_message(str(e)))

        tk.Button(win, text="שמור", command=save, bg="#800020", fg="black",
                  padx=20, pady=5).pack(pady=10)

    def delete_employee(self, e_id):
        if messagebox.askyesno("אישור", "האם את בטוחה שברצונך למחוק את העובד?"):
            try:
                conn = psycopg2.connect(**conn_params)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM employee WHERE e_id = %s", (e_id,))
                conn.commit()
                conn.close()
                self.fetch_employees()
                messagebox.showinfo("נמחק", "העובד נמחק בהצלחה.")
            except Exception as e:
                messagebox.showerror("שגיאה", explain_error_message(str(e)))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagerApp(root)
    root.mainloop()