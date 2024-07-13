# Rapport d'Implémentation pour la Gestion de Magasin

## Introduction
Ce rapport détaille l'implémentation d'un système de gestion de magasin en Python. Le projet inclut la gestion des articles, des ventes, et des commandes. De plus, il offre des fonctionnalités avancées telles que l'ajout de notes aux ventes, le filtrage des ventes par date, le calcul du total des ventes par client, la gestion des commandes, et l'exportation des rapports en format CSV.

## Structure du Code
Le projet est structuré autour de trois fichiers principaux :
1. `article.py`
2. `gestion_fichier.py`
3. `main.py`

Chaque fichier a un rôle spécifique pour assurer une organisation claire et une séparation des responsabilités.

### `article.py`
Ce fichier définit la classe `Article` qui encapsule les propriétés et les méthodes liées aux articles du magasin. Chaque article a un ID, un nom, un prix et une quantité.

### `gestion_fichier.py`
Ce fichier contient deux fonctions principales :
- `charger_fichier(nom_fichier)`: Charge les données depuis un fichier JSON.
- `sauvegarder_fichier(nom_fichier, data)`: Sauvegarde les données dans un fichier JSON.

Ces fonctions permettent de gérer la persistance des données entre les sessions.

### `main.py`
Le fichier principal du projet. Il orchestre les interactions avec l'utilisateur et utilise les classes et fonctions des autres fichiers pour effectuer les opérations nécessaires.

## Fonctionnalités
1. **Gestion des Ventes et des Commandes** :
    - **Ajout de notes aux ventes** : Ajoute des commentaires ou des notes spécifiques à une vente donnée.
    - **Filtrage des ventes par date** : Permet de visualiser les ventes dans une plage de dates spécifiée.
    - **Total des ventes par client** : Calcule le montant total des ventes pour chaque client.
    - **Gestion des commandes** :
        - Ajout de nouvelles commandes.
        - Modification des commandes existantes.
        - Suppression de commandes.
    - **Exportation des rapports en CSV** : Génère un fichier CSV contenant les détails des ventes.

2. **Menu Interactif** :
    - Un menu textuel qui permet à l'utilisateur de choisir parmi les différentes opérations disponibles.
    - Gère l'entrée utilisateur et appelle les fonctions appropriées pour effectuer les opérations demandées.

## Implémentation du Menu

Le menu interactif est conçu pour offrir une interface utilisateur conviviale. Voici les options disponibles dans le menu :

1. Ajouter une note à une vente
2. Filtrer les ventes par date
3. Afficher le total des ventes par client
4. Ajouter une commande
5. Modifier une commande
6. Supprimer une commande
7. Exporter les rapports de vente en CSV
8. Quitter

## Détails du Code

**Classe GestionMagasin** :
La classe `GestionMagasin` encapsule les méthodes pour gérer les articles, les ventes et les commandes.

**Méthodes de la classe GestionMagasin** :
- `ajouter_note_vente(self, id_vente, note)`: Ajoute une note à une vente spécifique.
- `filtrer_ventes_par_date(self, date_debut, date_fin)`: Filtre les ventes entre deux dates.
- `total_ventes_par_client(self)`: Calcule le total des ventes pour chaque client.
- `ajouter_commande(self, commande)`: Ajoute une nouvelle commande.
- `modifier_commande(self, id_commande, nouvelles_infos)`: Modifie une commande existante.
- `supprimer_commande(self, id_commande)`: Supprime une commande existante.
- `exporter_rapports_csv(self, chemin_fichier)`: Exporte les rapports de ventes en CSV.

**Fonctions de Menu** :
- `afficher_menu()`: Affiche le menu des options.
- `main()`: Gère l'exécution principale du programme, affiche le menu et traite les choix de l'utilisateur.

## Exemple d'Utilisation

Lors de l'exécution du programme, l'utilisateur est invité à choisir parmi les options du menu. Par exemple, pour ajouter une note à une vente, l'utilisateur entre l'option correspondante, puis spécifie l'ID de la vente et la note à ajouter.

## Conclusion
Ce projet offre une solution complète pour la gestion d'un magasin, incluant la gestion des articles, des ventes et des commandes. Le menu interactif facilite l'utilisation du système, et les fonctionnalités avancées permettent une gestion efficace et une analyse détaillée des ventes. Le système est extensible et peut être adapté pour répondre à des besoins spécifiques supplémentaires.

