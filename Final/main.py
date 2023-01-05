import pyttsx3
import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.engine = pyttsx3.init()

        # Set up the buttons
        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack()
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack()

        # Set up the volume slider
        self.volume = tk.Scale(root, from_=0, to=1, resolution=0.1,
                               orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume.pack()

    def play(self):
        self.engine.say(self.get_clipboard_text())
        self.engine.runAndWait()

    def pause(self):
        self.engine.stop()

    def set_volume(self, value):
        value = float(value)
        self.engine.setProperty('volume', value)

    def get_clipboard_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(
            self.root.selection_get(selection='CLIPBOARD'))
        return self.root.clipboard_get()


root = tk.Tk()
app = App(root)
root.mainloop()
