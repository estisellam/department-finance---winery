import tkinter as tk
from PIL import Image, ImageTk
import cv2
import subprocess
import sys

def show_intro_video():
    video_path = "/Users/yhd/department-finance---winery/DBProject/שלב ה/wine_intro.mp4.mp4"
    cap = cv2.VideoCapture(video_path)

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    lbl = tk.Label(root, bg="black")
    lbl.pack(fill=tk.BOTH, expand=True)

    def skip_video():
        cap.release()
        try:
            lbl.after_cancel(update_id)
        except:
            pass
        for widget in root.winfo_children():
            widget.destroy()
        root.update_idletasks()
        root.configure(bg="black")
        root.geometry(f"{screen_width}x{screen_height}")
        show_landing_page(root)

    skip_btn = tk.Button(
        root,
        text="דלג",
        command=skip_video,
        font=("Helvetica", 12, "bold"),
        bg="#800020",
        fg="black",
        padx=16,
        pady=6,
        relief="flat",
        activebackground="#A52A2A",
        activeforeground="white",
        cursor="hand2",
        highlightthickness=1,
        highlightbackground="white"
    )
    skip_btn.place(relx=0.97, rely=0.05, anchor="ne")

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (screen_width, screen_height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            lbl.imgtk = img
            lbl.configure(image=img)
            global update_id
            update_id = lbl.after(33, update_frame)
        else:
            skip_video()

    update_id = lbl.after(0, update_frame)
    root.mainloop()


def show_landing_page(root):
    root.configure(bg="black")

    tk.Label(
        root,
        text="WineCo",
        font=("Helvetica", 60, "bold"),
        fg="#800020",
        bg="black"
    ).pack(pady=(80, 10))

    tk.Label(
        root,
        text="מערכת ניהול כספים",
        font=("Helvetica", 26),
        fg="white",
        bg="black"
    ).pack(pady=(0, 60))

    def open_main():
        root.destroy()
        subprocess.Popen([
            sys.executable,
            "/Users/yhd/department-finance---winery/DBProject/שלב ה/employee.py"
        ])

    tk.Button(
        root,
        text=" ניהול עובדים ",
        command=open_main,
        font=("Helvetica", 18, "bold"),
        bg="white",
        fg="#800020",
        padx=40,
        pady=16,
        relief="raised",
        bd=2,
        activebackground="#f0f0f0",
        activeforeground="#800020",
        cursor="hand2"
    ).pack(pady=40)
 
    def open_summary():
        root.destroy()
        subprocess.Popen([
            sys.executable,
            "/Users/yhd/department-finance---winery/DBProject/שלב ה/summary_screen.py"
        ])
        
    tk.Button(
        root,
        text="דו״ח סיכום תשלומים",
       command=open_summary,
        font=("Helvetica", 18, "bold"),
        bg="white",
        fg="#800020",
        padx=40,
        pady=16,
        relief="raised",
        bd=2,
        activebackground="#f0f0f0",
        activeforeground="#800020",
        cursor="hand2"
    ).pack(pady=10)

    root.bind("<Escape>", lambda e: root.destroy())

# הפעלת התוכנית
if __name__ == "__main__":
    show_intro_video()