# In this project, I have created a web scrapper for booking.com. We have to go to the website and applying the filters about hotels that we want.
# After that, once the page loaded, we have to paste the link in scrapper and also give the csv file name that we want to create to store the data. 
# The scrapper will scrape all the available hotels' data and store it in the csv file.
# It will extract the hotel name, location, price, rating, score, reviews and url of each hotel.
import requests
from bs4 import BeautifulSoup
import csv

# function to scrape data from booking.com
def web_scrapper():
    # Get user input for url and file name
    url = input("Enter the url from booking.com that you want to scrape:\n")
    file_name = input("Enter the name of the file that you want to create to store the data:\n")

    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
    # Send a GET request to the website
    respone = requests.get(url, headers=header)
    # Check if the request was successful
    if respone.status_code == 200:
        print("Connected successfully to website")
        html_content = respone.text
        # Parse the HTML content
        soup = BeautifulSoup(html_content, "lxml")
        
        hotels_divs = soup.find_all("div", role="listitem")

        # Save the data to a CSV file
        with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(["Hotel Name", "Location", "Price(PKR)", "Rating", "Score", "Reviews", "URL"])
        
            # Loop through the hotel divs and extract the data
            for hotel in hotels_divs:
                # Hotel name
                name_tag = hotel.find("div", class_="b87c397a13 a3e0b4ffd1")
                name = name_tag.text.strip() if name_tag else "N/A"

                # Location
                location_tag = hotel.find("span", class_="d823fbbeed f9b3563dd4")
                location = location_tag.text.strip() if location_tag else "N/A"

                # Price
                price_tag = hotel.find("span", class_="b87c397a13 f2f358d1de ab607752a2")
                price = price_tag.text.split()[-1].strip() if price_tag else "N/A"

                # Rating text (e.g. Excellent)
                rating_tag = hotel.find("div", class_="f63b14ab7a f546354b44 becbee2f63")
                rating = rating_tag.text.strip() if rating_tag else "No rating"

                # Score (e.g. 8.6)
                score_tag = hotel.find("div", class_="f63b14ab7a dff2e52086")
                score = score_tag.text.strip() if score_tag else "N/A"
                
                # Reviews
                review_tag = hotel.find("div", class_="fff1944c52 fb14de7f14 eaa8455879")
                review = review_tag.text.split()[0].strip() if review_tag else "N/A"
                
                # Getting hotel url
                url_tag = hotel.find('a', href=True).get('href')
                url = url_tag if url_tag else "N/A"

                # Write the data to the CSV file
                writer.writerow([name, location, price, rating, score, review, url])

                print("Scraping completed successfully. Data saved to", file_name + ".csv")
                
    # If the request was not successful
    else:
        print("Failed to connect to website")

# Call the web_scrapper function
web_scrapper()