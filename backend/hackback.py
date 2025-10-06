from flask import Flask, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow CORS for all origins

def scrape_hackathons():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("http://taikai.network/hackathons")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    hackathons = []

    for hackathon_div in soup.find_all("div", class_="sc-98f07b04-5 legNEV"):
        event_title = hackathon_div.find("h3").text.strip() if hackathon_div.find("h3") else "N/A"
        href_tag = hackathon_div.find_previous("a", href=True)
        href = "https://taikai.network" + href_tag["href"].strip() if href_tag else "N/A"
        days_left_tag = hackathon_div.find_next("div", class_="sc-cwHptR ikcmWx")
        days_left = days_left_tag.text.strip() if days_left_tag else "N/A"
        span_texts = [span.text.strip() for span in hackathon_div.find_next("div", class_="sc-98f07b04-7 hgsWLA").find_all("span")] if hackathon_div.find_next("div", class_="sc-98f07b04-7 hgsWLA") else []

        hackathons.append({
            "Event Title": event_title,
            "href": href,
            "Days Left": days_left,
            "Span Texts": span_texts
        })

    return hackathons

@app.route("/api/hackathons", methods=["GET"])
def get_hackathons():
    print("API called!")  # Debugging
    return jsonify(scrape_hackathons())

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "API is working!"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
