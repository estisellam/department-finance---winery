import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from datetime import date
import subprocess
import sys
import os
import psycopg2.errors
from TourManagerApp import show_tour_crud_for_guide
from SalaryManager import show_salary_crud_for_employee
# === Database connection settings ===
conn_params = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "16040010",
    "dbname": "stage5"
}

class EmployeeManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WineCo - Employee & Tour Management")
        self.root.state("zoomed")
        self.root.configure(bg="#111111")
        self.setup_ui()
        self.fetch_employees()
       

    def setup_ui(self):
        HEADER_COLOR = "#800020"
        TEXT_COLOR = "#FFFFFF"
         # כפתור חזרה לעמוד הראשי
        tk.Button(root, text="חזור לתפריט הראשי",
              font=("Helvetica", 12, "bold"),
              bg="gray", fg="black",
              padx=10, pady=4,
              cursor="hand2",
              command=lambda: [root.destroy(), subprocess.Popen([
                  sys.executable,
                  "/Users/yhd/department-finance---winery/DBProject/שלב ה/opening_screen.py"
              ])]
         ).pack(pady=5)



        tk.Label(self.root, text="Financial Department - Employees & Tours", font=("Helvetica", 30, "bold"),
               fg=HEADER_COLOR, bg="#111111").pack(pady=20)

        self.tree_frame = tk.Frame(self.root, bg="#111111")
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=40)

        columns = ("ID", "Name", "Role", "Salary", "Tours", "Income", "ManageTours", "ManageTaxes", "Update", "Delete")
        headers = ["תעודת זהות", "שם", "תפקיד", "שכר", "מס' סיורים", "סה״כ הכנסות", "סיורים", "תלושי משכורות", "", ""]
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings", height=15)

        for col, txt in zip(columns, headers):
            self.tree.heading(col, text=txt)
            self.tree.column(col, anchor="center", width=130 if col not in ("Update", "Delete", "ManageTours") else 100)

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

        form = tk.Frame(self.root, bg="#111111")
        form.pack(pady=20)

        tk.Label(form, text="Add New Employee", font=("Helvetica", 16, "bold"),
                 fg=TEXT_COLOR, bg="#111111").grid(row=0, column=0, columnspan=5, pady=10)

        for i, txt in enumerate(["ID", "Name", "Role", "Salary"]):
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

        tk.Button(form, text="Add Employee", command=self.add_employee,
                  bg="#800020", fg="black", font=("Helvetica", 12, "bold"),
                  padx=20, pady=6).grid(row=2, column=4, padx=10)

    def fetch_employees(self):
      try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        cursor.execute("""
    SELECT 
        e.e_id,
        e.e_name,
        e.employee_role,
        COALESCE(
            (SELECT s.neto_salary
             FROM salary s
             WHERE s.e_id = e.e_id
             ORDER BY s.payslip_number DESC
             LIMIT 1),
            e.salary
        ) AS actual_salary,
        COUNT(t.tourid) AS tour_count,
        COALESCE(SUM(t.price * t.amount), 0) AS total_income
    FROM 
        employee e
    LEFT JOIN 
        tour t ON e.e_id = t.guideid
    GROUP BY 
        e.e_id, e.e_name, e.employee_role, e.salary
    ORDER BY 
        e.e_id;
""")
        rows = cursor.fetchall()
        conn.close()

        # ניקוי התצוגה הקיימת
        for row in self.tree.get_children():
            self.tree.delete(row)

        # הכנסת הנתונים לטבלה
        for e_id, name, role, total_salary, tour_count, total_income in rows:
            self.tree.insert("", "end", values=(
                e_id, name, role, f"{total_salary:,.2f} ₪",
                tour_count, f"{total_income:,.2f} ₪",
                "ניהול סיורים", "ניהול משכורות", "עדכון", "מחיקה"
            ))
      except Exception as e:
        messagebox.showerror("Error", str(e))

    def on_tree_click(self, event):
        item = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        if not item:
            return
        values = self.tree.item(item, "values")
        e_id = values[0]
        if column == "#9":
            self.update_employee_popup(e_id, values[1], values[2], values[3].replace(" ₪", "").replace(",", ""))
        elif column == "#10":
            self.delete_employee(e_id)
        elif column == "#7":
            self.manage_tours_for_guide(e_id)
        elif column == "#8":
            self.manage_salary_for_employee(e_id)
    def add_employee(self):
        try:
            e_id = int(self.entry_id.get())
            name = self.entry_name.get().strip()
            role = self.entry_role.get().strip()
            salary = float(self.entry_salary.get())

            if not name or not role:
                raise Exception("All fields are required.")

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
            messagebox.showinfo("Success", "Employee added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_employee_popup(self, e_id, name, role, salary):
        win = tk.Toplevel(self.root)
        win.title("Update Employee")
        win.configure(bg="#111111")

        tk.Label(win, text="Name", bg="#111111", fg="white").pack(pady=5)
        name_entry = tk.Entry(win)
        name_entry.insert(0, name)
        name_entry.pack()

        tk.Label(win, text="Role", bg="#111111", fg="white").pack(pady=5)
        role_combo = ttk.Combobox(win, values=["admin", "guide", "worker"])
        role_combo.set(role)
        role_combo.pack()

        def save():
            try:
                new_name = name_entry.get()
                new_role = role_combo.get()
                conn = psycopg2.connect(**conn_params)
                cursor = conn.cursor()

                # עדכון שם אם השתנה
                if new_name != name:
                    cursor.execute("""
                        UPDATE employee SET e_name = %s WHERE e_id = %s;
                    """, (new_name, e_id))

                # קריאה לפרוצדורה אם התפקיד השתנה
                if new_role != role:
                     cursor.execute("CALL pr_update_employee_role(%s, %s)", (e_id, new_role))
                conn.commit()
                conn.close()
                self.fetch_employees()
                win.destroy()
                messagebox.showinfo("Updated", "Employee updated successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Save", command=save, bg="#800020", fg="black", padx=20, pady=5).pack(pady=10)

    def delete_employee(self, e_id):
      try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        if messagebox.askyesno("Confirm", "Are you sure you want to delete this employee?"):

            # שלב 1: מחיקת רשומות מטבלאות שתלויות בטבלת salary
            cursor.execute("""
                DELETE FROM out_salary
                WHERE payslip_number IN (
                    SELECT payslip_number FROM salary WHERE e_id = %s
                );
            """, (e_id,))

            # שלב 2: מחיקת תלושי משכורת של העובד
            cursor.execute("""
                DELETE FROM salary WHERE e_id = %s;
            """, (e_id,))

            # שלב 3: מחיקת תשלומים (אם קיימים)
            cursor.execute("""
                DELETE FROM payment WHERE e_id = %s;
            """, (e_id,))

            # שלב 4: מחיקת הסיורים (אם העובד מדריך)
            cursor.execute("""
                DELETE FROM tour WHERE guideid = %s;
            """, (e_id,))

            # שלב 5: לבסוף – מחיקת העובד עצמו
            cursor.execute("""
                DELETE FROM employee WHERE e_id = %s;
            """, (e_id,))

            conn.commit()
            self.fetch_employees()
            messagebox.showinfo("Deleted", "Employee deleted successfully.")

        conn.close()

      except psycopg2.errors.ForeignKeyViolation:
        messagebox.showerror("שגיאה", "לא ניתן למחוק את העובד – יש רשומות תלויות שלא נמחקו.")
        conn.rollback()

      except Exception as e:
        messagebox.showerror("שגיאה", str(e))
        conn.rollback()
    def manage_tours_for_guide(self, guide_id):
     show_tour_crud_for_guide(guide_id)
    def manage_salary_for_employee(self, e_id):
     show_salary_crud_for_employee(e_id, self.fetch_employees)
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagerApp(root)
    root.mainloop() 
 