import tkinter as tk
from json_request import get_measures
from app_consts.variable_consts import FONT_M
import random



class FrameDisplayHome(tk.LabelFrame):
    def __init__(self, master, text= "Current INDOOR values") -> None:
        super().__init__(master, text=text)

        self.grid_columnconfigure((0,1), weight=1)
        
        def update():
            self.lbl_temperature_var.set(round(random.uniform(24.00,25.00),2))
            self.lbl_pressure_var.set(get_measures("pressure") + round(random.uniform(0.1,0.3),2))
            self.lbl_humidity_var.set(round(random.uniform(40.00,45.00),2))
            self.after(5000,update)

        self.after(5000,update)
        
        
        #region TITLES
        self.lbl_temperature_title = tk.Label(self,
                                          text='Temperature (°C):',
                                          font= FONT_M)
        self.lbl_temperature_title.grid(row=0, column=0,
                                    padx=10, pady=10)
        
        self.lbl_pressure_title = tk.Label(self,
                                          text='Pressure (hPa):',
                                          font=FONT_M)
        self.lbl_pressure_title.grid(row=1, column=0,
                                    padx=10, pady=10)
        
        self.lbl_humidity_title = tk.Label(self,
                                          text='Humidity (%):',
                                          font=FONT_M)
        self.lbl_humidity_title.grid(row=2, column=0,
                                    padx=10, pady=10)
        #endregion 


        #region VALUES
        self.lbl_temperature_var = tk.StringVar()
        self.lbl_temperature_var.set(round(random.uniform(23.50,25.00),2))
        self.lbl_temperature = tk.Label(self,
                                          textvariable=self.lbl_temperature_var,
                                          font=FONT_M)
        self.lbl_temperature.grid(row=0, column=1,
                                    padx=10, pady=10)
        
        self.lbl_pressure_var = tk.StringVar()
        self.lbl_pressure_var.set(get_measures("pressure") + round(random.uniform(0.1,0.3),2))
        self.lbl_pressure = tk.Label(self,
                                          textvariable=self.lbl_pressure_var,
                                          font=FONT_M)
        self.lbl_pressure.grid(row=1, column=1,
                                    padx=10, pady=10)
        
        self.lbl_humidity_var = tk.StringVar()
        self.lbl_humidity_var.set(round(random.uniform(40.00,45.00),2))

        self.lbl_humidity = tk.Label(self,
                                          textvariable=self.lbl_humidity_var,
                                          font=FONT_M)
        self.lbl_humidity.grid(row=2, column=1,
                                    padx=10, pady=10)
        
        
        #endregion