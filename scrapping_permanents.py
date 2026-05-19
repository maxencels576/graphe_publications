# # ================================= Scrapping Noms des Permanents ================================= #

# from bs4 import BeautifulSoup as bs
# import requests
# import json

# url_base = "https://www.univ-smb.fr/listic/presentation/membres/enseignants-chercheurs/"
# url = url_base

# headers = {"User-Agent": "Mozilla/5.0"}

# evenements = []

# while True:
#     response = requests.get(url, headers = headers)
#     soup = bs(response.content, "lxml")

#     # Sélection des informations
#     for ev in soup.select(".site-main"):

#         # Nom
#         nom = ev.select_one(".link-fr")
#         nom = nom.get_text(strip = True) if nom else "Nom inconnu"

#         # # Date
#         # date = ev.select_one(".tribe-events-calendar-list__event-datetime")
#         # date = date.get_text(" ", strip = True) if date else ""

#         # # Lieu
#         # lieu = ev.select_one(".tribe-events-calendar-list__event-venue")
#         # lieu = lieu.get_text(" ", strip=True) if lieu else "Lieu inconnu"

#         evenements.append({
#             "nom": nom
#             # "date": date
#             # "lieu": lieu
#         })

#     # Page suivante
#     # next = soup.select_one("li.next a")
#     # if next:
#     #     url = next["href"]
#     # else:
#     #     break

# # Sauvegarde JSON
# with open("informations.json", "w", encoding = "utf-8") as f:
#     json.dump(informations, f, ensure_ascii = False, indent = 4)

# print("Fichier JSON créé : informations.json")



from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

driver = webdriver.Chrome()
driver.get("https://www.univ-smb.fr/listic/presentation/membres/enseignants-chercheurs/")

time.sleep(2)  # attendre le chargement JS

soup = BeautifulSoup(driver.page_source, "lxml")

enseignants = []

for ev in soup.select("div.col-md-4"):
    nom = ev.select_one("a.link-fr").get_text(strip=True)
    poste = ev.select_one(".corps").get_text(strip=True)
    lien = ev.select_one("a.link-fr")["href"]

    enseignants.append({
        "nom": nom,
        "poste": poste,
        "lien": lien
    })

with open("enseignants.json", "w", encoding="utf-8") as f:
    json.dump(enseignants, f, ensure_ascii=False, indent=4)

driver.quit()
