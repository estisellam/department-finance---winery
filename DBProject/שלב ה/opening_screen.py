import tkinter as tk
from PIL import Image, ImageTk
import cv2
import subprocess
import sys

# === שלב 1: הצגת סרטון פתיחה עם כפתור דלג ===
def show_intro_video():
    video_path = "/Users/yhd/department-finance---winery/DBProject/שלב ה/wine_intro.mp4.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("⚠️ לא ניתן לפתוח את הווידאו. בדקי את הנתיב.")
        show_landing_page()
        return

    intro_root = tk.Tk()
    intro_root.attributes("-fullscreen", True)
    intro_root.configure(bg="black")

    screen_width = intro_root.winfo_screenwidth()
    screen_height = intro_root.winfo_screenheight()

    lbl = tk.Label(intro_root, bg="black")
    lbl.pack(fill=tk.BOTH, expand=True)

    # כפתור דילוג מעוצב
    def skip_video():
        cap.release()
        intro_root.destroy()
        show_landing_page()

    skip_btn = tk.Button(
        intro_root,
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
            frame = cv2.resize(frame, (screen_width, screen_height), interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            lbl.imgtk = img
            lbl.configure(image=img)
            lbl.after(33, update_frame)
        else:
            cap.release()
            intro_root.destroy()
            show_landing_page()

    intro_root.after(0, update_frame)
    intro_root.mainloop()

# === שלב 2: מסך עם כפתור “כניסה למערכת” ===
def show_landing_page():
    landing = tk.Tk()
    landing.attributes("-fullscreen", True)
    landing.configure(bg="black")

    # כותרת ראשית
    tk.Label(
        landing,
        text="WineCo",
        font=("Helvetica", 60, "bold"),
        fg="#800020",
        bg="black"
    ).pack(pady=(80, 10))

    # כותרת משנית
    tk.Label(
        landing,
        text="מערכת ניהול כספים",
        font=("Helvetica", 26),
        fg="white",
        bg="black"
    ).pack(pady=(0, 60))

    # כפתור פתיחה מעוצב
    def open_main():
        landing.destroy()
        subprocess.Popen([
            sys.executable,
            "/Users/yhd/department-finance---winery/DBProject/שלב ה/main.py"
        ])

    btn = tk.Button(
        landing,
        text=" רשימת משכורות",
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
    )
    btn.pack(pady=40)

    # קיצור יציאה
    landing.bind("<Escape>", lambda e: landing.destroy())
    landing.mainloop()

# התחלה
show_intro_video()