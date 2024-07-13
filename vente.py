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

# Chargement des données à partir des fichiers JSON
articles = charger_fichier("articles.json")
ventes = charger_fichier("ventes.json")
commandes = charger_fichier("commandes.json")

# Instanciation de l'objet GestionMagasin
magasin = GestionMagasin(articles, ventes, commandes)

# Exemple d'utilisation des nouvelles fonctionnalités
print(magasin.ajouter_note_vente(1, "Client très satisfait"))
ventes_filtrees = magasin.filtrer_ventes_par_date("2023-01-01", "2023-12-31")
for vente in ventes_filtrees:
    print(vente)

totals = magasin.total_ventes_par_client()
for client, total in totals.items():
    print(f"Client: {client}, Total: {total}")

magasin.ajouter_commande({"id": 1, "article": "Article1", "quantité": 2})
magasin.modifier_commande(1, {"quantité": 3})
magasin.supprimer_commande(1)

magasin.exporter_rapports_csv("ventes.csv")
