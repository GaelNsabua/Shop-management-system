import gestion_fichier

articles = gestion_fichier.charger_article('Projet Gestion magasin\donnees.json')

#Structure qui permet de gerer les erreurs
def gestion_erreur():
    try :
        pass
    except Exception :
        return False

def validationNomArticle(nomArticle):
    while not nomArticle.replace(' ', '', 1).isalpha():
        print("! ERREUR !! Le nom doit être une chaine de caractère !")
        nomArticle = input("Saisissez le nom de l'article :: ")
    return nomArticle

def validationPrixArticle(prixArticle):
    while not prixArticle.replace('.', '', 1).isdigit():
        print("! ERREUR !! Le prix doit être en entier ou decimal !")
        prixArticle = input("Saisissez le prix de l'article :: ")
    return prixArticle

def validationQteArticle(qteArticle):
    while not qteArticle.isdigit():
        print("! ERREUR !! La quantité doit être un entier !")
        qteArticle = input("Saisissez la quantité de l'article :: ")
    return qteArticle


# Fonction qui permet de rechercher un article par id ou par nom
def recherche_produit(key) :
    for i in range(len(articles)):
        if key.isalpha() :
            if key == articles[i].get('nom') :
               return articles[i]
        elif key.isdigit():
            if int(key) == articles[i].get('id') :
                return articles[i]
        
    print("====================================================================================================")
    print("L'article recherché n'existe pas !!")
    print("====================================================================================================")
    return None


# Fonction de recherche article
def interface_recherche_produit():
    key = input("Entrez le nom ou l'id de l'article à rechercher :: ")
    article =  recherche_produit(key)
    if article is not None :
        print("====================================================================================================")
        print(f"Voici le résultat de la recherche : {article}")
        print("====================================================================================================")


#Fonction qui permet de supprimer un article
def supprimer_article():
    key = input("Entrez le nom ou l'id de l'article à supprimer :: ")
    article =  recherche_produit(key)
    if article is not None :
        articles.remove(article)
        print("====================================================================================================")
        print(f"L'article {article['nom']} a été supprimé avec succès !!")
        print("====================================================================================================")
        gestion_fichier.sauvegarder_article(articles,'Projet Gestion magasin\donnees.json')
        return
       
            
    print("====================================================================================================")
    print("L'article à supprimer n'existe pas !!")

#Fonction qui permet de recuperer les informations sur l'article à ajouter
def input_info_article():
    nomArt = validationNomArticle(input("Saisissez le nom de l'article :: "))
    prixArt = float(validationPrixArticle(input("Saisissez le prix de l'article :: ")))
    qteArt = int(validationQteArticle(input("Saisissez la quantité de l'article :: ")))

    article = {
        'id': articles[-1]['id']+1,
        'nom': nomArt,
        'prix': prixArt,
        'qte': qteArt,
    }

    return article


# Fonction qui permet d'ajouter des nouveaux article
def interface_ajout_produit():
    article = input_info_article()
    #Verification pour eviter les doublons dans la liste contenant les articles
    for i in range(len(articles)):
        if article['nom'] == articles[i].get('nom'):
            print("Article deja existant !!!!")
            return
    #Ajoute l'article dans la listes des articles
    articles.append(article)
    #Sauvegarde les articles dans le fichier json
    gestion_fichier.sauvegarder_article(articles,'Projet Gestion magasin\donnees.json')
    #Message de confirmation d'ajout
    print("====================================================================================================")
    print("Produit ajouté avec succès")
    print(f"Avec les informations suivantes : {article}")
    print("====================================================================================================")


#Fonction qui permet d'afficher les differents produit se trouvant dans la base de données
def interface_afficher_produit():
    for article in articles :
        print("====================================================================================================")
        print(f"ID : {article['id']}")
        print(f"Nom : {article['nom']}")
        print(f"Prix : {article['prix']}")
        print(f"Quantité : {article['qte']}")
        print("====================================================================================================")


class Article:
    def __init__(self, id, nom, prix, quantite):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return f"Article(id={self.id}, nom={self.nom}, prix={self.prix}, quantite={self.quantite})"

   