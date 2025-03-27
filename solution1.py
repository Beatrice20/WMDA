### **Exercise 1: Extracting and Cleaning Data from an API**
import requests
import pandas as pd

cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]

list = []

for city in cities:
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    weather_data = response.text.strip()

    #rsplit - face split de la dreapta la stanga
    strings = weather_data.rsplit(' ', 1)
    weather_condition = strings[0].strip()
    temperature = strings[1].strip()

    list.append({
        'City': city,
        'Temperature': temperature,
        'Weather Condition': weather_condition
    })

df = pd.DataFrame(list)

df.to_csv('output_1.csv', index=False)

print(df)
