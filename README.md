# Bill : Un chatbot de Réservation de Restaurant

Ce projet est un chatbot conçu pour aider les utilisateurs à effectuer des réservations de table dans un restaurant, vérifier les disponibilités, obtenir des informations sur le menu du jour, et plus encore.

## Prérequis

- Python 3.7 ou plus récent
- Rasa 3.0 ou plus récent
Important : le projet a été entièrement réalisé sur une VM Ubuntu. Le guide d'installation ci-dessous montre comment setup le projet sur Ubuntu, et non sur Windows.

## Installation

1. Clonez le repository :
    ```bash
    git clone https://github.com/alexisDEF/bill.git
    cd bill
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances nécessaires :
    ```bash
    pip install -r requirements.txt
    ```

## Entraînement du modèle

1. Entraînez le modèle Rasa avec les données fournies :
    ```bash
    rasa train
    ```

## Exécution du bot

1. Démarrez le serveur d'actions pour exécuter les actions personnalisées définies dans `actions.py` :
    ```bash
    rasa run actions
    ```

2. Dans une autre fenêtre de terminal, démarrez le bot Rasa :
    ```bash
    rasa shell
    ```

# Exemple de story :

Quel est le menu du jour ?

Pouvez-vous me donner le lien vers le menu complet ?

Je voudrais reserver -> 19 mai 19h -> 4 personnes -> Rimbaud -> 06 01 01 01 01

Je voudrais supprimer ma reservation -> #USIAJFA
