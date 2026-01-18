# Architecture globale – FastFoodGo

L'application FastFoodGo repose sur une architecture client-serveur.

## Composants principaux

- Frontend Web / Mobile  
  Interface utilisée par les clients pour consulter les restaurants, gérer le panier et passer commande.

- API Backend (REST)  
  Centralise la logique métier, gère l'authentification, les commandes, les paiements et la communication avec les services externes.

- Base de données  
  Stocke les utilisateurs, restaurants, plats, commandes et paiements.

- Service de paiement externe  
  Prestataire tiers (Stripe, PayPal) chargé du traitement sécurisé des paiements.

- Service de notifications  
  Envoi d’e-mails de confirmation et de suivi de commande.

## Fonctionnement général

Le frontend communique avec l’API Backend via des requêtes HTTP.  
Le backend interagit avec la base de données et les services externes pour traiter les commandes et notifier les utilisateurs.

