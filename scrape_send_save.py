import requests
from bs4 import BeautifulSoup
import json
import time
from kafka import KafkaProducer

# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# URL to scrape
url = "https://scrapeme.live/shop/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all("ul", class_="columns-4")

product_list = []

for product in products:
    product_links = product.find_all("li", class_="product-type-simple")
    for link in product_links:
        full_link = link.a.get("href")

        detail = requests.get(full_link)
        detail_soup = BeautifulSoup(detail.content, "html.parser")

        informations = detail_soup.find_all("div", attrs={"class": "entry-summary"})

        for info in informations:
            name = info.find("h1", attrs={"class": "entry-title"}).text
            price = info.find("span", attrs={"class": "amount"}).text
            description = info.find("div", attrs={"class": "woocommerce-product-details__short-description"}).text.strip()
            stock = info.find("p", attrs={"class": "in-stock"}).text

            # Convert price to numerical format
            price = float(price.replace("£", "").replace(",", ""))

            product_info = {
                "name": name,
                "price": price,
                "description": description,
                "stock": stock
            }

            # Send data to Kafka topic
            producer.send('products1_topic', value=product_info)
            # 1 second interval
            time.sleep(1)
            print(f"Sent product to Kafka: {product_info}")

            # Save data to JSON file
            product_list.append(product_info)
            with open('products.json', 'w', encoding='utf-8') as f:
                json.dump(product_list, f, ensure_ascii=False, indent=4)
            print(f"Saved product to file: {product_info}")

            
