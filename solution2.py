### **Exercise 2: Web Scraping a Product Listings Page**
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="thumbnail")

product_list=[]

for product in products[:10]:
    name = product.find("a", class_="title").text.strip()
    price = product.find("h4", class_="price").text.strip()

    product_list.append({"Name": name, "Price": price})
    df_cleaned = pd.DataFrame(product_list)

df_cleaned.to_csv("output_2.csv", index=False)
