import article
import gestion_fichier
#import os

def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Enregistrer vente")
    print("5. Afficher ventes")
    print("6. Ventes par client")
    print("7. Générer rapport de ventes")
    print("8. Charger données")
    print("9. Supprimer un article")
    print("10. Quitter")
    return input("Choisissez une option: ")


def main():
    while True:
        articles = gestion_fichier.charger_article('Projet Gestion magasin/donnees.json')
        choix = menu_principal()
        if choix == '1':
            article.interface_ajout_produit()
        elif choix == '2':
            article.interface_afficher_produit()
        elif choix == '3':
            article.interface_recherche_produit()
        elif choix == '4':
            # interface_enregistrement_vente()
            print("interface_enregistrement_vente")
        elif choix == '5':
            # interface_affichage_ventes()
            print("interface_affichage_ventes")
        elif choix == '6':
            # interface_ventes_par_client()
            print("interface_vente_par_client")
        elif choix == '7':
            # generer_rapport_ventes()
            print("generer rapport")
        elif choix == '8':
            # charger_donnees()
            print("charger données")
        elif choix == '9':
            article.supprimer_article()
        elif choix == '10':
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
