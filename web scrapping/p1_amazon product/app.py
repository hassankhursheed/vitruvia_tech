# In this project, we extract the data of an amazon product live from the website and save it to a csv file.
# We extract the product title, product price, product rating, bullet points and reviews of 3 customers.

from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.com/Adults-Perfect-Interactive-Companion-Workspace/dp/B09XGQMSMB/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

# check if request was successful
if response.status_code == 200:
    print("Successfully got the web page:", response.status_code)
    soup = BeautifulSoup(response.text, "lxml")
else:
    print("Failed to retrieve page:", response.status_code)
    exit()

# Extract product title
title_tag = soup.find("span", id="productTitle")
if title_tag:
    product_title = title_tag.get_text(strip=True)
    print("Product Title:", product_title)
else:
    print("Product title not found (possible bot protection)")

# Extract product price
price_tag = soup.find("span", class_="a-offscreen")
if price_tag:
    product_price = price_tag.get_text(strip=True)
    print("Product Price:", product_price)
else:
    print("Product price not found (possible bot protection)")

# Extract product rating
rating_tag = soup.find("span", class_="a-icon-alt")
if rating_tag:
    product_rating = rating_tag.get_text(strip=True)
    print("Product Rating:", product_rating)
else:
    print("Product rating not found (possible bot protection)")


# Extract product bullet points
bullet_points = []
# use find_all to get all div elements with id="feature-bullets"
bullet_point_tags = soup.find_all("div", id="feature-bullets")
if bullet_point_tags:
    # for loop and find_all to get all li elements and append to bullet_points
    for bullet_point in bullet_point_tags[0].find_all("li"):
        bullet_points.append(bullet_point.get_text(strip=True))
    print("Bullet Points:")
    # print each bullet point
    for bullet_point in bullet_points:
        print(bullet_point)
else:
    print("Bullet points not found (possible bot protection)")

# Extract product reviews
# here we extract the reviews of 3 customers
# Customers 1 review
reviews = []
review_tags = soup.find_all("div", id="customer_review-R332QEN19KM34P")
if review_tags:
    for review in review_tags:
        reviews.append(review.get_text(strip=True))
    print("Reviews: 1")
    for review in reviews:
        print(review)
else:
    print("Reviews not found (possible bot protection)")
    
# customer 2 review
reviews = []
review_tags = soup.find_all("div", id="customer_review-R3SJ4GS0UJQ16P")
if review_tags:
    for review in review_tags:
        reviews.append(review.get_text(strip=True))
    print("Reviews: 2")
    for review in reviews:
        print(review)
else:
    print("Reviews not found (possible bot protection)")

# customer 3 review
reviews = []
review_tags = soup.find_all("div", id="customer_review-R2GCSXMQZZUOQD")
if review_tags:
    for review in review_tags:
        reviews.append(review.get_text(strip=True))
    print("Reviews: 3")
    for review in reviews:
        print(review)
else:
    print("Reviews not found (possible bot protection)")

# saving the data to a csv file
# here encoding is utf-8 is used to handle special characters
with open("amazon_product_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Title", "Product Price", "Product Rating", "Bullet Points", "Reviews"])
    writer.writerow([product_title, product_price, product_rating, bullet_points, reviews])

# data saved
print("Data saved to amazon_product_data.csv")

