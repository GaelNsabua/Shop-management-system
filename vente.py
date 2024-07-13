import json
from datetime import datetime
import csv
from article import Article
from gestion_fichier import charger_fichier, sauvegarder_fichier

class GestionMagasin:
    def __init__(self, articles, ventes, commandes):
        self.articles = articles
        self.ventes = ventes
        self.commandes = commandes

    def ajouter_note_vente(self, id_vente, note):
        for vente in self.ventes:
            if vente['id'] == id_vente:
                vente['note'] = note
                return "Note ajoutée avec succès"
        return "Vente non trouvée"

    def filtrer_ventes_par_date(self, date_debut, date_fin):
        date_debut = datetime.strptime(date_debut, "%Y-%m-%d")
        date_fin = datetime.strptime(date_fin, "%Y-%m-%d")
        ventes_filtrees = [
            vente for vente in self.ventes
            if date_debut <= datetime.strptime(vente['date'], "%Y-%m-%d") <= date_fin
        ]
        return ventes_filtrees

    def total_ventes_par_client(self):
        total_par_client = {}
        for vente in self.ventes:
            client = vente['client']
            total_par_client[client] = total_par_client.get(client, 0) + vente['montant']
        return total_par_client

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def modifier_commande(self, id_commande, nouvelles_infos):
        for commande in self.commandes:
            if commande['id'] == id_commande:
                commande.update(nouvelles_infos)
                return "Commande modifiée avec succès"
        return "Commande non trouvée"

    def supprimer_commande(self, id_commande):
        for commande in self.commandes:
            if commande['id'] == id_commande:
                self.commandes.remove(commande)
                return "Commande supprimée avec succès"
        return "Commande non trouvée"

    def exporter_rapports_csv(self, chemin_fichier):
        with open(chemin_fichier, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Client", "Article", "Montant", "Date", "Note"])
            for vente in self.ventes:
                writer.writerow([
                    vente['id'], vente['client'], vente['article'],
                    vente['montant'], vente['date'], vente.get('note', '')
                ])
        return "Rapport exporté avec succès"

def afficher_menu():
    print("1. Ajouter une note à une vente")
    print("2. Filtrer les ventes par date")
    print("3. Afficher le total des ventes par client")
    print("4. Ajouter une commande")
    print("5. Modifier une commande")
    print("6. Supprimer une commande")
    print("7. Exporter les rapports de vente en CSV")
    print("8. Quitter")

def main():
    articles = charger_fichier("articles.json")
    ventes = charger_fichier("ventes.json")
    commandes = charger_fichier("commandes.json")

    magasin = GestionMagasin(articles, ventes, commandes)

    while True:
        afficher_menu()
        choix = input("Entrez votre choix: ")

        if choix == '1':
            id_vente = int(input("Entrez l'ID de la vente: "))
            note = input("Entrez la note: ")
            print(magasin.ajouter_note_vente(id_vente, note))

        elif choix == '2':
            date_debut = input("Entrez la date de début (YYYY-MM-DD): ")
            date_fin = input("Entrez la date de fin (YYYY-MM-DD): ")
            ventes_filtrees = magasin.filtrer_ventes_par_date(date_debut, date_fin)
            for vente in ventes_filtrees:
                print(vente)

        elif choix == '3':
            totals = magasin.total_ventes_par_client()
            for client, total in totals.items():
                print(f"Client: {client}, Total: {total}")

        elif choix == '4':
            id_commande = int(input("Entrez l'ID de la commande: "))
            article = input("Entrez le nom de l'article: ")
            quantite = int(input("Entrez la quantité: "))
            date = input("Entrez la date (YYYY-MM-DD): ")
            commande = {"id": id_commande, "article": article, "quantité": quantite, "date": date}
            magasin.ajouter_commande(commande)

        elif choix == '5':
            id_commande = int(input("Entrez l'ID de la commande à modifier: "))
            nouvelles_infos = {}
            article = input("Entrez le nouveau nom de l'article (laisser vide pour ne pas changer): ")
            if article:
                nouvelles_infos['article'] = article
            quantite = input("Entrez la nouvelle quantité (laisser vide pour ne pas changer): ")
            if quantite:
                nouvelles_infos['quantité'] = int(quantite)
            date = input("Entrez la nouvelle date (YYYY-MM-DD) (laisser vide pour ne pas changer): ")
            if date:
                nouvelles_infos['date'] = date
            print(magasin.modifier_commande(id_commande, nouvelles_infos))

        elif choix == '6':
            id_commande = int(input("Entrez l'ID de la commande à supprimer: "))
            print(magasin.supprimer_commande(id_commande))

        elif choix == '7':
            chemin_fichier = input("Entrez le chemin du fichier CSV: ")
            print(magasin.exporter_rapports_csv(chemin_fichier))

        elif choix == '8':
            sauvegarder_fichier("articles.json", articles)
            sauvegarder_fichier("ventes.json", ventes)
            sauvegarder_fichier("commandes.json", commandes)
            print("Données sauvegardées. Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

main()
