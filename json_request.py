import requests
from app_consts.variable_consts import api_path

response = requests.get(api_path)
  

def get_measures(object, r= response):
   
   if r.status_code == 200:

      if object == "temp":

         return round(float((r.json()["main"][object]) - 273.15),2)
      
      else:
         return float(r.json()["main"][object])



def return_image(r=response):
   
   if float(r.json()["main"]["temp"] - 273.15) <0 :
      return "app_consts/winter-hat.png"
   elif float(r.json()["main"]["temp"] - 273.15) <10 :
      return "app_consts/jacket.png"
   elif float(r.json()["main"]["temp"] - 273.15) <20 :
      return "app_consts/light_jacket.png"
   else:
      return "app_consts/clothing.png"

def return_note(r=response):
   
   if float(r.json()["main"]["temp"] - 273.15) <0 :
      return "Dress warm, it is below 0 degrees outside!"
   elif float(r.json()["main"]["temp"] - 273.15) <10 :
      return "Wear a warm jacket, it is chilly outside"
   elif float(r.json()["main"]["temp"] - 273.15) <20 :
      return "Wear a light jacket"
   else:
      return "It is hot outside, wear light clothes"