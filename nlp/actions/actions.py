from typing import Any, Text, Dict, List
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ActionGreet(Action):
    def run(self, dispatcher: CollectingDispatcher, tracker: DomainDict, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello!")
        return []

class ActionAskName(Action):
    def run(self, dispatcher: CollectingDispatcher, tracker: DomainDict, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("What is your name?")
        return []

class ActionFarewell(Action):
    def run(self, dispatcher: CollectingDispatcher, tracker: DomainDict, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Goodbye, {}!".format(tracker.get_slot("name")))
        return []

class ActionWriteJavaCode(Action):
    def name(self) -> Text:
        return "utter_write_java_code"

    def run(self, dispatcher: CollectingDispatcher, tracker: DomainDict, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_write_java_code")
        return []

class ActionAskTemperature(Action):
    def name(self) -> Text:
        return "utter_ask_temperature"

    def run(self, dispatcher: CollectingDispatcher, tracker: DomainDict, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_temperature")
        return []

class ActionAskForecast(Action):
    def name(self) -> Text:
        return "utter_ask_forecast"

    def run(self, dispatcher: CollectingDispatcher, tracker: DomainDict, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_forecast")
        return []
class ActionAskWeather(Action):
    def name(self) -> Text:
        return "utter_ask_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_weather")
        return []