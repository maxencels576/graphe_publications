
Graphe de publications


L’objectif de ce 3ème projet est de construire des graphes de co-autoring pour les membres du LISTIC

Dans le cadre de ce projet nous avons utilisé deux API nous permettant de récupérer les document lié au chercheurs que ce soit sous la forme d’auteurs seul ou non.
Lors du scraping de ses données nous avons pris en compte la possibilité de doublon mais également de faute de saisie des nom des chercheurs et de leurs articles liés.
Nous avons utilisé l’API de HAL et de OpenAlex pour récupérer les données des chercheurs du LISTIC. Nous avons ensuite traité ces données pour construire un graphe de co-autoring, où les nœuds représentent les chercheurs et les arêtes représentent les collaborations entre eux.
