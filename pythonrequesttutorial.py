from time import sleep
import requests

def temperature():
    while True:
        try:
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=66910cc54f55f6bc8de8dc666ccb3120')
            return r
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
    
    

temperature()