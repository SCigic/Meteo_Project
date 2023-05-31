import tkinter as tk
from tk_gui.FrameDisplayWeather import FrameDisplayWeather
from tk_gui.FrameDisplayHome import FrameDisplayHome
from tk_gui.FrameDisplayNote import FrameDisplayNote


class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()


        self.title("Meteo app - current weather")
        self.geometry("800x800")
        self.grid_columnconfigure((0,1),weight=1)

        

        #region DISPLAY_Weather

        self.frm_display_weather = FrameDisplayWeather(self)
        self.frm_display_weather.grid(row=0, column=0, 
                                      padx=20, pady=10, sticky="ew")
        

        self.frm_display_home = FrameDisplayHome(self)
        self.frm_display_home.grid(row=0, column=1, 
                                      padx=20, pady=10, sticky="ew")

        #endregion

        self.frm_display_note = FrameDisplayNote(self)
        self.frm_display_note.grid(row=1, column=0, columnspan=2, 
                                      padx=20, pady=10, sticky="ew")

        self.button_close_app = tk.Button(self,
                                text="Close app",
                                command=self.destroy,
                                font= ("Verdana", 18))
        self.button_close_app.grid(row=4, column=0, columnspan=2,
                                   padx=5, pady=5) 




