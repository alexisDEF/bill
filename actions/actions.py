from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionReserverTable(Action):
    def name(self) -> Text:
        return "action_reserver_table"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour réserver une table
        # Vous pouvez accéder aux entités extraites du tracker comme ceci :
        date = tracker.get_slot("date")
        nombre_personnes = tracker.get_slot("nombre_personnes")
        nom_reservation = tracker.get_slot("nom_reservation")
        telephone = tracker.get_slot("telephone")
        
        # Exemple de réponse
        dispatcher.utter_message("Votre réservation pour le {} pour {} personnes a été confirmée.".format(date, nombre_personnes))
        
        return []

class ActionVerifierDisponibilite(Action):
    def name(self) -> Text:
        return "action_verifier_disponibilite"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour vérifier la disponibilité
        # Exemple de réponse
        dispatcher.utter_message("Je vais vérifier la disponibilité pour vous. \n ... \n C'est tout bon")
        
        return []

class ActionAnnulerReservation(Action):
    def name(self) -> Text:
        return "action_annuler_reservation"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour annuler la réservation
        # Exemple de réponse
        dispatcher.utter_message("Votre réservation a été annulée avec succès.")
        
        return []

class ActionObtenirMenuJour(Action):
    def name(self) -> Text:
        return "action_obtenir_menu_jour"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour obtenir le menu du jour
        # Exemple de réponse
        dispatcher.utter_message("Voici le menu du jour : \n -Entrée : Oeufs mimosa et son coulis de citron au sel de Guérande \n -Plat : Entrecôte maturée accompagnée de ses pommes grenailles \n -Dessert : moelleux au chocolat")
        
        return []

class ActionObtenirAllergenes(Action):
    def name(self) -> Text:
        return "action_obtenir_allergenes"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour obtenir la liste des allergènes
        # Exemple de réponse
        dispatcher.utter_message("Voici la liste des allergènes : \n -Poissons \n -Fruits de mer\n -Fruits à coque")
        
        return []

class ActionObtenirMenuComplet(Action):
    def name(self) -> Text:
        return "action_obtenir_menu_complet"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour obtenir le menu complet
        # Exemple de réponse
        dispatcher.utter_message("Voici le menu complet : \n http://www.crusoe.fr/3695/carte_robinson-crusoe-restaurant-la-teste-bassin-d-arcachon.html")
        
        return []
