import difflib
import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class GetComponentInfoAction(Action):
    def name(self) -> Text:
        return "action_get_component_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the component name from the user's message
        component_name = next(tracker.get_latest_entity_values("component"), None)

        if component_name is None:
            dispatcher.utter_message("Sorry, I did not understand your message. Can I help you with something else?")
            return []

        with open("/Users/aviktora/ai/pf-ai-chatbot/chatbot/actions/components.json", "r") as file:
            components: dict = json.load(file)

        if component_name in components:
            component_details = components[component_name]
        else:
            # find a possible component which user could mean, or respond "I do not understand your message"
            close_matches = difflib.get_close_matches(component_name, components.keys(), n=1)
            if len(close_matches) == 0:
                dispatcher.utter_message("Sorry, I did not understand your message.\n"
                                         "Can I help you with something else?")
                return []
            else:
                close_match = close_matches[0]
                component_details = components[close_match]
                dispatcher.utter_message(f"You probably meant {component_details['name']}.")

        component_full_name = component_details["name"]
        description = component_details["description"]
        link = component_details["link"]

        response = f"{description}\n" \
                   f"More details about {component_full_name} can be found here: {link}\n"

        # Send the response to the user
        dispatcher.utter_message(response)
        return []
