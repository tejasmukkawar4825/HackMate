from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL to scrape
driver.get("http://taikai.network/hackathons")

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

# Extract the required data
link = soup.select_one('a[href^="/en/cryptocanal/hackathons/ethdam2025/"]')
link_href = link["href"] if link else "Not found"

# Extract all text inside the span tags within the specified div
details_div = soup.find("div", class_="sc-98f07b04-7 hgsWLA")
span_texts = [span.get_text(strip=True) for span in details_div.find_all("span")] if details_div else []

# Extract the "66 days left" text
days_left = soup.select_one("div.sc-cwHptR.ikcmWx")
days_left_text = days_left.text if days_left else "Not found"

# Extract the number "80"
li_text = soup.select_one("li").text.strip() if soup.select_one("li") else "Not found"

# Extract "ETHDam III"
h3_text = soup.select_one("div.sc-98f07b04-5.legNEV h3")
h3_text_value = h3_text.text if h3_text else "Not found"

# Print extracted data
print("Link:", link_href)
print("Span Texts:", span_texts)
print("Days Left:", days_left_text)
print("Number in LI:", li_text)
print("Event Title:", h3_text_value)
