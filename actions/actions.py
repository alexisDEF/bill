from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import uuid

class ActionReserverTable(Action):
    def name(self) -> Text:
        return "action_reserver_table"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.get_slot('date')
        nombre_personnes = tracker.get_slot('nombre_personnes')
        nom_reservation = tracker.get_slot('nom_reservation')
        telephone = tracker.get_slot('telephone')
        
        numero_reservation = str(uuid.uuid4())  # Générer un numéro de réservation unique
        
        confirmation_message = (f"Votre réservation pour le {date} pour {nombre_personnes} personnes "
                                f"au nom de {nom_reservation} a été confirmée. "
                                f"Votre numéro de réservation est {numero_reservation}.")
        
        dispatcher.utter_message(text=confirmation_message)
        return []

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
