import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import os 
import folium
from colorama import Fore
from colorama import init 
init()
#clean ter minal 
os.system("clear")
#api 
key = "7e5552da788f400db1f3f51cd584933f"
#input phone number
print(""" 
  /$$$$$$                                                                                                     
 /$$__  $$                                                                                                    
| $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
| $$  | $$|  $$  /$$//$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$ /$$__  $$
| $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/|  $$$$$$ | $$$$$$$$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  | $$| $$$$$$$$
| $$  | $$  \  $$$/ | $$_____/| $$       \____  $$| $$_____/| $$_____/| $$  | $$| $$_____/| $$  | $$| $$_____/
|  $$$$$$/   \  $/  |  $$$$$$$| $$       /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$
 \______/     \_/    \_______/|__/      |_______/  \_______/ \_______/|__/  |__/ \_______/ \____  $$ \_______/
                                                                                           /$$  | $$          
                                                                                          |  $$$$$$/          
                                                                                           \______/           
                                                                                                               """)
print(Fore.GREEN)
phone = input("enter the phone number(ex: +1687049586785): ")
os.system("cls")
#about phone number
ch_number = phonenumbers.parse(phone, "CH")
print(Fore.GREEN+ "Info: " + Fore.WHITE + str(ch_number))
#country
place = geocoder.description_for_number(ch_number, "en")
print(Fore.GREEN + "Country: " + Fore.WHITE + place)
#provider
service = phonenumbers.parse(phone, "RO")
print(Fore.GREEN + "provider: " + Fore.WHITE +carrier.name_for_number(service, "en"))
#timezone
time = phonenumbers.parse(phone, "en")
print(Fore.GREEN + "timezone: " + Fore.WHITE + str(timezone.time_zones_for_number(time)))
#cordinats
geocoder = OpenCageGeocode(key)
idk = str(place)
place_number = geocoder.geocode(idk)
p_1 = place_number[0]['geometry']['lat']
p_2 = place_number[0]['geometry']['lng']
print(Fore.RED)
print("cordinats are:")
print(p_1, p_2)