import tkinter as tk


class Button(tk.Button):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.pack(pady=10)
        self["state"] = "normal"

    def switch(self):
        self["state"] = "disable" if self["state"] == "normal" else "normal"
