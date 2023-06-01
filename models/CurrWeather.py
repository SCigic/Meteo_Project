from datetime import datetime as dt
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class CurrWeather(Base):
    __tablename__ = 'curr_weather_measurements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time_stamp = Column(DateTime, default = dt.now(), nullable=False)
    current_temp = Column(Float(precision=8, decimal_return_scale=8), nullable=False)
    current_pressure = Column(Float(precision=8, decimal_return_scale=8), nullable=False)
    current_humidity = Column(Float(precision=8, decimal_return_scale=8), nullable=False)


    def __init__(self, 
                 time_stamp: dt,
                 curr_temp: float, 
                 curr_pressure: float, 
                 curr_humidity: float):
        self.time_stamp: dt = time_stamp
        self.current_temp: float = curr_temp
        self.current_pressure: float = curr_pressure
        self.current_humidity: float = curr_humidity

