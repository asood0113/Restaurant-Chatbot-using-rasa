from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk import DomainDict

# show projects
class ValidateRegisterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_details_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

       
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_submitdetails"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
	
        book_number = tracker.get_slot("book_number")
        print("You have booked a table for  : ",book_number) 
        
		
        dispatcher.utter_message(template="utter_details_thanks")
        
        return[book_number]
        
        ac = tracker.get_slot("ac")
        
		
        dispatcher.utter_message(template="utter_details_thanks")
        
        return[ac]

        time = tracker.get_slot("time")
        
		
        dispatcher.utter_message(template="utter_details_thanks")
        
        return[time]

    