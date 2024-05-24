from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import uuid
import csv
import os
import random
import string
RESERVATION_FILE = "reservations.csv"


class ActionVerifierDisponibilite(Action):
    def name(self) -> Text:
        return "action_verifier_disponibilite"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Votre logique de vérification des disponibilités ici
        dispatcher.utter_message(text="Je vais vérifier la disponibilité pour vous. \n ... \n C'est tout bon")
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



def generateReservationId():
    """Génère un ID de réservation unique."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def saveReservationToCsv(reservation_id, date, nombre_personnes, nom_reservation, telephone):
    """Sauvegarde la réservation dans un fichier CSV."""
    file_exists = os.path.isfile(RESERVATION_FILE)
    
    with open(RESERVATION_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Écrire l'en-tête si le fichier n'existe pas encore
            writer.writerow(["reservation_id", "date", "nombre_personnes", "nom_reservation", "telephone"])
        writer.writerow([reservation_id, date, nombre_personnes, nom_reservation, telephone])

def readReservationFromCsv(reservation_id):
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
        reservation_id = generateReservationId()
        
        # Sauvegarder la réservation dans le fichier CSV
        saveReservationToCsv(reservation_id, date, nombre_personnes, nom_reservation, telephone)
        
        confirmation_message = (f"Votre réservation pour {nombre_personnes} personnes le {date} sous le nom {nom_reservation} "
                                f"a été confirmée. Votre numéro de réservation est {reservation_id}.")
        
        dispatcher.utter_message(text=confirmation_message)
        return []

class ActionObtenirReservation(Action):
    def name(self) -> Text:
        return "action_obtenir_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reservation_id = tracker.get_slot('reservation_id')
        
        reservation = readReservationFromCsv(reservation_id)
        
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


def deleteReservationFromCsv(reservation_id):
    """Supprime la réservation du fichier CSV."""
    if not os.path.isfile(RESERVATION_FILE):
        return False
    
    rows = []
    found = False
    with open(RESERVATION_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["reservation_id"] != reservation_id:
                rows.append(row)
            else:
                found = True
    
    if found:
        with open(RESERVATION_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["reservation_id", "date", "nombre_personnes", "nom_reservation", "telephone"])
            writer.writeheader()
            writer.writerows(rows)
    
    return found


class ActionSupprimerReservation(Action):
    def name(self) -> Text:
        return "action_supprimer_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reservation_id = tracker.get_slot('reservation_id')
        
        if deleteReservationFromCsv(reservation_id):
            message = f"La réservation avec le numéro {reservation_id} a été supprimée avec succès."
        else:
            message = f"Aucune réservation trouvée avec le numéro {reservation_id}."
        
        dispatcher.utter_message(text=message)
        return []