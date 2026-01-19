# FastFoodGo – TD Conception Logicielle

Ce dépôt contient le travail réalisé dans le cadre du **TD de conception logicielle**.  
Le projet porte sur l’application **FastFoodGo**, une plateforme de commande de repas en ligne reliant des restaurants partenaires à des clients.

---

## 🎯 Objectifs du TD
- Concevoir une architecture logicielle cohérente
- Identifier les principaux modules fonctionnels
- Définir des endpoints REST via Swagger
- Proposer un modèle de données relationnel
- Mettre en place une intégration continue et une gouvernance Git

---

## 🏗️ Architecture de l’application

L’architecture de FastFoodGo repose sur une séparation claire des responsabilités :

- **Frontend Web / Mobile** : interface utilisateur permettant la consultation des restaurants, des menus et la gestion des commandes
- **API Backend** : logique métier, gestion des utilisateurs, commandes et paiements
- **Base de données** : stockage des utilisateurs, restaurants, plats et commandes
- **Service de paiement externe** : gestion des paiements (ex. Stripe, PayPal)
- **Service de notifications** : envoi de confirmations de commande par e-mail


---

## 📂 Contenu du dépôt

### Exercice 1 – Architecture
- Description détaillée de l’architecture globale de l’application

📄 Fichier :  
`exercice-1-architecture.md`

---

### Exercice 2 – Endpoints REST (Swagger)
- Définition des endpoints REST au format **OpenAPI / Swagger**
- Modules couverts : Auth, Restaurants, Cart, Orders

📁 Dossier :  
`exercice-2-endpoints/`  
📄 Fichier :  
`swagger.yaml`

---

### Exercice 3 – Modèle de données
- Modèle relationnel SQL
- Tables : USERS, RESTAURANTS, MEALS, ORDERS, ORDER_ITEMS
- Traçabilité des commandes

📁 Dossier :  
`exercice-3-modele/`  
📄 Fichier :  
`modele.sql`

---

## ⚙️ Installation

Le projet est structuré comme un **package Python** suivant les bonnes pratiques (`src/`).

Pour installer le projet en mode développement ainsi que les dépendances nécessaires :

```bash
pip install -e ".[dev]"

---

## ⚙️ Tests unitaires

Les tests unitaires sont écrits avec pytest, on peut les exécuter en local avec pytest.

---

## ⚙️ Intégration continue (CI)

Une pipeline GitHub Actions est configurée pour automatiser l’exécution des tests unitaires.

La CI est déclenchée automatiquement :
- à chaque push sur une branche
- à chaque Pull Request

La CI garantit que :
- le projet peut être installé correctement
- les tests unitaires passent avec succès
- aucun code non testé ou non fonctionnel n’est intégré à la branche principale

---

## ⚙️ Gouvernance GIT

La branche main est protégée afin de garantir la stabilité du projet :
- aucun push ou merge direct n’est autorisé sur main
- toute contribution doit passer par une Pull Request
- la CI GitHub Actions doit être validée avant tout merge

---

