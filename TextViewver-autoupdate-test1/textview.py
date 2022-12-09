import tkinter as tk
from tkinter import ttk
import pyperclip

class ClipboardMonitor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Clipboard Monitor")
        self.geometry("300x100")
        self.resizable(False, False)

        self.clipboard_label = ttk.Label(self, text="Clipboard:")
        self.clipboard_label.grid(row=0, column=0, padx=10, pady=10)

        self.clipboard_text = tk.StringVar()
        self.clipboard_display = ttk.Label(self, textvariable=self.clipboard_text)
        self.clipboard_display.grid(row=0, column=1, padx=10, pady=10)

        self.after(100, self.update_clipboard)

    def update_clipboard(self):
        self.clipboard_text.set(pyperclip.paste())
        self.after(100, self.update_clipboard)

if __name__ == "__main__":
    app = ClipboardMonitor()
    app.mainloop()
