from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL to scrape
url = "http://taikai.network/hackathons"
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Close WebDriver after fetching the page source
driver.quit()

# Extract hackathon details
hackathons = []

for hackathon_div in soup.find_all("div", class_="sc-98f07b04-5 legNEV"):
    event_title = hackathon_div.find("h3").text.strip() if hackathon_div.find("h3") else "N/A"
    
    href_tag = hackathon_div.find_previous("a", href=True)
    href = href_tag["href"].strip() if href_tag else "N/A"

    #days_left_div = hackathon_div.find_next("div", class_="sc-cwHptR ikcmWx")
    #days_left = days_left_div.text.strip() if days_left_div else "N/A"

    days_left_tag = hackathon_div.find_next("div", class_="sc-cwHptR ikcmWx")
    if days_left_tag:
            days_left= days_left_tag.text.strip()

    span_texts = []
    span_div = hackathon_div.find_next("div", class_="sc-98f07b04-7 hgsWLA")
    if span_div:
        span_texts = [span.text.strip() for span in span_div.find_all("span")]

    hackathons.append({
        "Event Title": event_title,
        "href": href,
        "Days Left": days_left,
        "Span Texts": span_texts
    })

# Print or process the extracted data
import json
print(json.dumps(hackathons, indent=4))
