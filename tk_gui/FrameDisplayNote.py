import tkinter as tk
from PIL import Image, ImageTk
from app_consts.variable_consts import FONT_S
from json_request import return_image, return_note



class FrameDisplayNote(tk.LabelFrame):
    def __init__(self, master, text= "What to wear", bg="#EAF2F8") -> None:
        super().__init__(master, text=text, bg=bg)

        self.grid_columnconfigure((0,1), weight=1)

        self.img = ImageTk.PhotoImage(Image.open(return_image()).resize((80,80)))
        
        self.img_label = tk.Label(self, image=self.img, bg="#EAF2F8")
        self.img_label.grid(row=0, column=0, 
                    padx=20, pady=10, sticky="e")
        
        self.note_label = tk.Label(self,
                                text=return_note(),
                                font=FONT_S,
                                bg="#EAF2F8")
        self.note_label.grid(row=0, column=1, 
                    padx=20, pady=10, sticky="w")

