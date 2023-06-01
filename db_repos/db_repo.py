from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.CurrWeather import CurrWeather, Base
from datetime import datetime as dt
from json_request import get_measures


db_engine = create_engine('sqlite:///database/WeatherData.sqlite')

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

def db_init():
        Base.metadata.create_all(db_engine)
      
         
        
def save_record_to_db():
        
    weather_data = CurrWeather(dt.now(),
                                    float(get_measures("temp")),
                                    float(get_measures("pressure")),
                                    float(get_measures("humidity")))
        
    session.add(weather_data)
    session.commit()
    