import requests
from bs4 import BeautifulSoup
import csv

# URL of the Amazon page for air conditioners
url = 'https://www.amazon.in/s?k=air+conditioner'

# Send a GET request to the Amazon page
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the data from the HTML content
data = []
for item in soup.find_all('div', class_='s-result-item'):
    title = item.find('h2').text.strip()
    price = item.find('span', class_='a-price-whole').text.strip()
    data.append({'title': title, 'price': price})

    # Stop after extracting the top 20 air conditioners
    if len(data) >= 20:
        break

# Write the data to a CSV file
with open('data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])
    for item in data:
        writer.writerow([item['title'], item['price']])

print('Data saved to data.csv')
