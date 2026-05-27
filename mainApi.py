import API_HAL
import API_OALEX

import json
import unicodedata
import re
from difflib import SequenceMatcher

def normalize_title(title):
    t = ''.join(c for c in unicodedata.normalize('NFD', title)
                if unicodedata.category(c) != 'Mn')
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def authors_match(auth1, auth2):
    norm1 = [normalize_title(a) for a in auth1]
    norm2 = [normalize_title(a) for a in auth2]

    matches = 0
    for a in norm1:
        for b in norm2:
            if similarity(a, b) > 0.8:
                matches += 1
                break

    return matches >= min(len(norm1), len(norm2)) * 0.5

def is_duplicate(a, b):
    """Détecte si deux articles sont des doublons."""
    title_a = normalize_title(a["article"])
    title_b = normalize_title(b["article"])

    # 1. titres identiques
    if title_a == title_b:
        return True

    # 2. un titre est contenu dans l'autre
    if title_a in title_b or title_b in title_a:
        return True

    if similarity(title_a, title_b) > 0.85:
        return True

    if authors_match(a["authors"], b["authors"]):
        return True

    return False

def merge_hal_openalex(hal_path, oa_path, output_path):
    with open(hal_path, "r", encoding="utf-8") as f:
        hal_data = json.load(f)

    with open(oa_path, "r", encoding="utf-8") as f:
        oa_data = json.load(f)

    merged = []

    for art in hal_data + oa_data:
        duplicate_found = False

        for existing in merged:
            if is_duplicate(art, existing):
                duplicate_found = True
                break

        if not duplicate_found:
            merged.append(art)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=4)




def main():
    API_HAL.chargerEnseignantHal()
    API_OALEX.chargerEnseignantOpenAlex()
    merge_hal_openalex("articlesCoAuteurs_HAL.json", "articlesCoAuteurs_OpenAlex.json", "articlesFusionnes.json")

main()