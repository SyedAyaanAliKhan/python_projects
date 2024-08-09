import tkinter as tk
from tkinter import messagebox

class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.configure(bg="#000000")  # Black background 

        # Create a frame
        frame = tk.Frame(root, bg="#000000")
        frame.pack(padx=20, pady=20)

        # Create and place labels
        self.hours_label = tk.Label(frame, text="Hours:", bg="#000000", fg="#FFFFFF", font=("Digital-7", 20))
        self.hours_label.grid(row=0, column=0, padx=10, pady=10)
        self.hours_entry = tk.Entry(frame, width=5, font=("Digital-7", 20), bg="#000000", fg="#00FF00", justify='center')
        self.hours_entry.grid(row=0, column=1, padx=10, pady=10)

        self.minutes_label = tk.Label(frame, text="Minutes:", bg="#000000", fg="#FFFFFF", font=("Digital-7", 20))
        self.minutes_label.grid(row=1, column=0, padx=10, pady=10)
        self.minutes_entry = tk.Entry(frame, width=5, font=("Digital-7", 20), bg="#000000", fg="#00FF00", justify='center')
        self.minutes_entry.grid(row=1, column=1, padx=10, pady=10)

        self.seconds_label = tk.Label(frame, text="Seconds:", bg="#000000", fg="#FFFFFF", font=("Digital-7", 20))
        self.seconds_label.grid(row=2, column=0, padx=10, pady=10)
        self.seconds_entry = tk.Entry(frame, width=5, font=("Digital-7", 20), bg="#000000", fg="#00FF00", justify='center')
        self.seconds_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create a button to start the timer with digital look
        self.start_button = tk.Button(frame, text="Start", command=self.start_timer, font=("Digital-7", 20), bg="#FF4500", fg="#FFFFFF", relief=tk.RAISED)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

        # Label to show remaining time with digital clock
        self.time_display = tk.Label(frame, text="00:00:00", font=("Digital-7", 60), bg="#000000", fg="#00FF00")
        self.time_display.grid(row=4, column=0, columnspan=2, pady=20)

        self.remaining_time = None

    def start_timer(self):
        try:
            hours = int(self.hours_entry.get() or "0")
            minutes = int(self.minutes_entry.get() or "0")
            seconds = int(self.seconds_entry.get() or "0")
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers.")
            return

        if hours < 0 or minutes < 0 or seconds < 0 or seconds >= 60 or minutes >= 60:
            messagebox.showerror("Input Error", "Enter non-negative values. Minutes and seconds must be < 60.")
            return

        total_seconds = hours * 3600 + minutes * 60 + seconds

        if total_seconds <= 0:
            messagebox.showwarning("Input Error", "Enter a positive duration.")
            return

        self.remaining_time = total_seconds
        self.update_timer()

    def update_timer(self):
        if self.remaining_time is not None and self.remaining_time > 0:
            hours, remainder = divmod(self.remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_format = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.time_display.config(text=time_format)
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        elif self.remaining_time == 0:
            self.time_display.config(text="00:00:00")
            messagebox.showinfo("Time's Up!", "The countdown has finished.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop() #code execution
