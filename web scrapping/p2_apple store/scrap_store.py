# In this project, we extract all the products data from apple store(offline website) and save it to a CSV file
# We extract the header name, menu items and details of all the products like name, price, quantity, rating and estimated shipping
from bs4 import BeautifulSoup
import csv

html_path = r"D:\vitruvia\web scrapping\p2_apple store\apple_store.html"

with open(html_path, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content, "html.parser")
# Extract the header
header = soup.find("h1").text

# Extract the menu
menu = soup.find("nav").find_all("a")
menu_items = [item.text for item in menu]

# Extract product delails
products_divs = soup.find_all("div", class_="product")

# save extracted data to a CSV file
with open("apple_store.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    # write header row and menu items
    writer.writerow(["Header", header])
    writer.writerow(["Menu Items", ", ".join(menu_items)])

    # write product details' column names
    writer.writerow(["Product Name", "Price", "Product Quantity", "Product Rating", "Estimated Shipping"])
    # extract product details
    for product_div in products_divs:
        product = product_div.find("h3").text
        price = product_div.find("p").text.replace("Price: ", "")
        quantity = product_div.find_all("p")[1].text.replace("Quantity Available: ", "")
        rating = product_div.find("p", class_="rating").text
        est_shipping = product_div.find_all("p")[-1].text.replace("Estimated Shipping: ", "")
        
        # write product details to CSV
        writer.writerow([product, price, quantity, rating, est_shipping])