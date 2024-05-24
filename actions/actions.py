from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import uuid
import csv
import os
import random
import string


class ActionVerifierDisponibilite(Action):
    def name(self) -> Text:
        return "action_verifier_disponibilite"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Votre logique de vérification des disponibilités ici
        dispatcher.utter_message(text="Je vais vérifier la disponibilité pour vous. \n ... \n C'est tout bon")
        return []

class ActionAnnulerReservation(Action):
    def name(self) -> Text:
        return "action_annuler_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Votre logique d'annulation ici
        dispatcher.utter_message(text="Votre réservation a été annulée avec succès.")
        return []

class ActionObtenirMenuJour(Action):
    def name(self) -> Text:
        return "action_obtenir_menu_jour"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour obtenir le menu du jour
        menu_jour = "Voici le menu du jour : \n -Entrée : Oeufs mimosa et son coulis de citron au sel de Guérande \n -Plat : Entrecôte maturée accompagnée de ses pommes grenailles \n -Dessert : moelleux au chocolat"
        dispatcher.utter_message(text=menu_jour)
        return []

class ActionObtenirAllergenes(Action):
    def name(self) -> Text:
        return "action_obtenir_allergenes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour obtenir les allergènes
        allergenes = "Voici la liste des allergènes : \n -Poissons \n -Fruits de mer \n -Fruits à coque"
        dispatcher.utter_message(text=allergenes)
        return []

class ActionObtenirMenuComplet(Action):
    def name(self) -> Text:
        return "action_obtenir_menu_complet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour obtenir le menu complet
        menu_complet = "Voici le menu complet : \n http://www.crusoe.fr/3695/carte_robinson-crusoe-restaurant-la-teste-bassin-d-arcachon.html"
        dispatcher.utter_message(text=menu_complet)
        return []



# class ActionReserverTable(Action):
#     def name(self) -> Text:
#         return "action_confirm_reservation"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         date = tracker.get_slot('date')
#         nombre_personnes = tracker.get_slot('nombre_personnes')
#         nom_reservation = tracker.get_slot('nom_reservation')
#         telephone = tracker.get_slot('telephone')
        
#         numero_reservation = str(uuid.uuid4())  # Générer un numéro de réservation unique
        
#         confirmation_message = (f"Votre réservation pour le {date} pour {nombre_personnes} personnes "
#                                 f"au nom de {nom_reservation} a été confirmée. "
#                                 f"Votre numéro de réservation est {numero_reservation}.")
        
#         dispatcher.utter_message(text=confirmation_message)
#         return []



# Définir le chemin du fichier CSV pour stocker les réservations
RESERVATION_FILE = "reservations.csv"

def generate_reservation_id():
    """Génère un ID de réservation unique."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def save_reservation_to_csv(reservation_id, date, nombre_personnes, nom_reservation, telephone):
    """Sauvegarde la réservation dans un fichier CSV."""
    file_exists = os.path.isfile(RESERVATION_FILE)
    
    with open(RESERVATION_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Écrire l'en-tête si le fichier n'existe pas encore
            writer.writerow(["reservation_id", "date", "nombre_personnes", "nom_reservation", "telephone"])
        writer.writerow([reservation_id, date, nombre_personnes, nom_reservation, telephone])

def read_reservation_from_csv(reservation_id):
    """Lit les détails de la réservation depuis le fichier CSV."""
    if not os.path.isfile(RESERVATION_FILE):
        return None
    
    with open(RESERVATION_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["reservation_id"] == reservation_id:
                return row
    return None

class ActionReserverTable(Action):
    def name(self) -> Text:
        return "action_confirm_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.get_slot('date')
        nombre_personnes = tracker.get_slot('nombre_personnes')
        nom_reservation = tracker.get_slot('nom_reservation')
        telephone = tracker.get_slot('telephone')
        
        # Générer un ID de réservation unique
        reservation_id = generate_reservation_id()
        
        # Sauvegarder la réservation dans le fichier CSV
        save_reservation_to_csv(reservation_id, date, nombre_personnes, nom_reservation, telephone)
        
        # Message de confirmation avec l'ID de réservation
        confirmation_message = (f"Votre réservation pour {nombre_personnes} personnes le {date} sous le nom {nom_reservation} "
                                f"a été confirmée. Votre numéro de réservation est {reservation_id}.")
        
        dispatcher.utter_message(text=confirmation_message)
        return []

class ActionObtenirReservation(Action):
    def name(self) -> Text:
        return "action_obtenir_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reservation_id = tracker.get_slot('reservation_id')
        
        reservation = read_reservation_from_csv(reservation_id)
        
        if reservation:
            reservation_info = (f"Réservation {reservation_id} : \n"
                                f"Date : {reservation['date']}\n"
                                f"Nombre de personnes : {reservation['nombre_personnes']}\n"
                                f"Nom : {reservation['nom_reservation']}\n"
                                f"Téléphone : {reservation['telephone']}")
        else:
            reservation_info = f"Je ne trouve aucune réservation avec le numéro {reservation_id}."
        
        dispatcher.utter_message(text=reservation_info)
        return []
