import json

with open('enseignants.json') as f:
    enseignants = [e["nom"].title() for e in json.load(f)]

with open('articlesCoAuteurs_HAL.json') as f: # changer le nom du fichier par celui final
    articles = json.load(f)

article_count = {}
coauteur_count = {}

for article in articles:
    present = [a.title() for a in article["authors"] if a.title() in enseignants]
    for e in present:
        article_count[e] = article_count.get(e, 0) + 1
    for i in range(len(present)):
        for j in range(i+1, len(present)):
            pair = tuple(sorted([present[i], present[j]]))
            coauteur_count[pair] = coauteur_count.get(pair, 0) + 1

nodes = [[e, article_count.get(e, 0)] for e in enseignants]
edges = [[a, b, n] for (a, b), n in coauteur_count.items()]