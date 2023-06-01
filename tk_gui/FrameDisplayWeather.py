import tkinter as tk
from json_request import get_measures
from db_repos.db_repo import save_record_to_db
from app_consts.variable_consts import FONT_M




class FrameDisplayWeather(tk.LabelFrame):
    def __init__(self, master, text= "Current OUTDOOR values") -> None:
        super().__init__(master, text=text)

        self.grid_columnconfigure((0,1), weight=1)

        def update():
            self.lbl_temperature_var.set(get_measures("temp"))
            self.lbl_pressure_var.set(get_measures("pressure"))
            self.lbl_humidity_var.set(get_measures("humidity"))

            save_record_to_db()
            
            self.after(5000,update)

        self.after(5000,update)
        
        
        #region TITLES
        self.lbl_temperature_title = tk.Label(self,
                                          text='Temperature (°C):',
                                          font=FONT_M)
        self.lbl_temperature_title.grid(row=0, column=0,
                                    padx=10, pady=10)
        
        self.lbl_pressure_title = tk.Label(self,
                                          text='Pressure (hPa):',
                                          font= FONT_M)
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
        self.lbl_temperature_var.set(get_measures("temp"))

        self.lbl_temperature = tk.Label(self,
                                          textvariable=self.lbl_temperature_var,
                                          font=FONT_M)
        self.lbl_temperature.grid(row=0, column=1,
                                    padx=10, pady=10)
        
        self.lbl_pressure_var = tk.StringVar()
        self.lbl_pressure_var.set(get_measures("pressure"))
        self.lbl_pressure = tk.Label(self,
                                          textvariable=self.lbl_pressure_var,
                                          font=FONT_M)
        self.lbl_pressure.grid(row=1, column=1,
                                    padx=10, pady=10)
        
        self.lbl_humidity_var = tk.StringVar()
        self.lbl_humidity_var.set(get_measures("humidity"))
        self.lbl_humidity = tk.Label(self,
                                          textvariable=self.lbl_humidity_var,
                                          font=FONT_M)
        self.lbl_humidity.grid(row=2, column=1,
                                    padx=10, pady=10)
        
        
        #endregion