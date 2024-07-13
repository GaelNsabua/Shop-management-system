import json

#Fonction qui nous permet de recuperer les articles dans le fichier json
def charger_article(chemin_fichier):
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            return json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
#Fonction qui permet de sauvegarder les articles dans un fichier json
def sauvegarder_article(articles,chemin_fichier):
    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        json.dump(articles, fichier, indent=4)