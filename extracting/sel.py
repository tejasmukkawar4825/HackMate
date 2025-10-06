from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Configure Selenium
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Set up driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the Devpost hackathon page
url = "https://devpost.com/hackathons?page=2"
driver.get(url)

# Wait for JavaScript to load content
time.sleep(5)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

data = []
hackathons = soup.find_all("div", class_="hackathon-tile")

for hackathon in hackathons:
    hackathon_data = {}

    # Extract href
    link = hackathon.find("a", class_="flex-row tile-anchor")
    hackathon_data["href"] = link["href"] if link else None

    # Extract image URL
    img = hackathon.find("img", class_="hackathon-thumbnail")
    hackathon_data["img_url"] = img["src"] if img else None

    # Extract info class span (Online)
    info_span = hackathon.find("div", class_="info").find("span")
    hackathon_data["info"] = info_span.text if info_span else None

    # Extract hackathon name
    title_div = hackathon.find("h3", class_="mb-4")
    hackathon_data["title"] = title_div.text.strip() if title_div else None

    # Extract submission period
    submission_period = hackathon.find("div", class_="submission-period")
    hackathon_data["submission_period"] = submission_period.text.strip() if submission_period else None

    # Extract prize amount
    prize = hackathon.find("div", class_="prize")
    hackathon_data["prize"] = prize.text.strip() if prize else None

    # Extract participants count
    participants = hackathon.find("div", class_="participants")
    hackathon_data["participants"] = participants.text.strip() if participants else None

    # Extract managed by text (mr-1 class)
    managed_by = hackathon.find("a", class_="mr-1")
    hackathon_data["managed_by"] = managed_by.text.strip() if managed_by else None

    # Extract Microsoft info
    host_info = hackathon.find("span", class_="label round host-label")
    hackathon_data["host"] = host_info.text.strip() if host_info else None

    # Extract themes
    themes_div = hackathon.find("div", class_="themes")
    themes = [theme.text.strip() for theme in themes_div.find_all("span", class_="theme-label")] if themes_div else []
    hackathon_data["themes"] = themes

    data.append(hackathon_data)

driver.quit()

print(data)
