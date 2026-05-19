from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

url = "https://www.univ-smb.fr/listic/presentation/membres/enseignants-chercheurs/"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)  # attendre le chargement JS

soup = BeautifulSoup(driver.page_source, "lxml")

enseignants = []

teachers = soup.find_all("a", rel="noopener noreferrer")

if teachers:
    for teacher in teachers:
        nom = teacher.text.strip()
        enseignants.append({
            "nom": nom,
        })

with open("enseignants.json", "w", encoding="utf-8") as f:
    json.dump(enseignants, f, ensure_ascii=False, indent=4)

driver.quit()
