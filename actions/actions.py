from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionReserverTable(Action):
    def name(self) -> Text:
        return "action_reserver_table"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour réserver une table
        # Extraire les entités de la demande de réservation (date, nombre de personnes, nom, téléphone)
        date = tracker.get_slot("date")
        nombre_personnes = tracker.get_slot("nombre_personnes")
        nom_reservation = tracker.get_slot("nom_reservation")
        telephone = tracker.get_slot("telephone")

        # Appeler une API externe ou interagir avec une base de données pour effectuer la réservation
        # Ici, nous simulerons simplement la réservation en affichant les détails de la réservation
        dispatcher.utter_message(
            f"Votre réservation pour le {date} pour {nombre_personnes} personnes sous le nom de {nom_reservation} a été confirmée. Nous vous contacterons au numéro {telephone}."
        )

        return []

class ActionVerifierDisponibilite(Action):
    def name(self) -> Text:
        return "action_verifier_disponibilite"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour vérifier la disponibilité
        # Extraire les entités de la demande de disponibilité (date, nombre de personnes)
        date = tracker.get_slot("date")
        nombre_personnes = tracker.get_slot("nombre_personnes")

        # Appeler une API externe ou interagir avec une base de données pour vérifier la disponibilité
        # Ici, nous simulerons simplement la disponibilité en envoyant un message à l'utilisateur
        dispatcher.utter_message(
            f"Il y a une table disponible pour {nombre_personnes} personnes le {date}."
        )

        return []
