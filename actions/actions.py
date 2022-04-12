# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionReadAksi(Action):

    def name(self) -> Text:
        return "action_read_aksi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        aksi=next(tracker.get_latest_entity_values("aksi"),None)
        ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
        barang=next(tracker.get_latest_entity_values("barang"),None)
        if not aksi:
            msg=f"Tolong beritahu apa yang harus aku lakukan"
            dispatcher.utter_message(text=msg)
            aksi=next(tracker.get_latest_entity_values("aksi"),None)
            return []
        if not ruangan:
            msg=f"Tolong beritahu tujuan ruangan untuk mengantar"
            dispatcher.utter_message(text=msg)
            aksi=next(tracker.get_latest_entity_values("ruangan"),None)
            return []
        if not barang:
            msg=f"Tolong beritahu barang yang harus diantar"
            dispatcher.utter_message(text=msg)
            aksi=next(tracker.get_latest_entity_values("barang"),None)
            return []
        print('aksi berhasil diekstrak : ',aksi)
        print('ruangan berhasil diekstrak : ',ruangan)
        print('barang berhasil diekstrak : ',barang)
        dispatcher.utter_message(template="utter_read_aksi")
        dispatcher.utter_message(text="Baik, tolong beritahu nama anda dan nama orang yang dituju ya!")


class ActionReadRuangan(Action):

    def name(self) -> Text:
        return "action_read_ruangan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
        print('ruangan berhasil diekstrak : ',ruangan)
        dispatcher.utter_message(template="utter_read_ruangan")


class ActionReadBarang(Action):

    def name(self) -> Text:
        return "action_read_barang"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        barang=next(tracker.get_latest_entity_values("barang"),None)
        print('barang berhasil diekstrak : ',barang)
        dispatcher.utter_message(template="utter_read_barang")

class ActionReadNama(Action):

    def name(self) -> Text:
        return "action_read_nama"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pengirim=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="pengirim"),None)
        penerima=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="penerima"),None)
        if not pengirim:
            msg=f"Tolong beritahu nama anda sebagai pengirim dari barang yang diantarkan"
            dispatcher.utter_message(text=msg)
            pengirim=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="pengirim"),None)
            return []
        if not penerima:
            msg=f"Tolong beritahu nama orang yang menerima dari barang yang diantarkan"
            dispatcher.utter_message(text=msg)
            penerima=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="penerima"),None)
            return []
        print('pengirim berhasil diekstrak : ',pengirim)
        print('penerima berhasil diekstrak : ',penerima)
        dispatcher.utter_message(template="utter_read_nama")

# class ActionPauseConversation(Action):
#     """Pause a conversation"""

#     def name(self):
#         return "action_pause_conversation"

#     async def run(self, dispatcher, tracker, domain) -> List[EventType]:
#         logger.info(f"Pausing the conversation")

#         sender_id = tracker.sender_id

#         dispatcher.utter_message(
#             f"Pausing this conversation, with SENDER_ID: " f"{sender_id}"
#         )

#         dispatcher.utter_message(
#             f"To resume, send this resume event to the rasa-production container:"
#         )

#         dispatcher.utter_message(
#             """curl --request POST
#             --url 'http://localhost:5005/conversations/SENDER_ID/tracker/events?token=RASA_TOKEN'
#             --header 'content-type: application/json'
#             --data '[{"event": "resume"}, {"event": "followup", "name": "action_resume_conversation"}]'       
#             """
#         )

#         dispatcher.utter_message(
#             f"When you're running it within Rasa X, send this resume event to the rasa-production container via the Rasa X /core/... endpoint:"
#         )

#         dispatcher.utter_message(
#             """curl --request POST
#             --url 'http://HOST:PORT/core/conversations/SENDER_ID/tracker/events?token=RASA_TOKEN'
#             --header 'content-type: application/json'
#             --data '[{"event": "resume"}, {"event": "followup", "name": "action_resume_conversation"}]'       
#             """
#         )

#         return [ConversationPaused()]

# class ActionResumeConversation(Action):
#     """Just to inform the user that a conversation has resumed. 
#     This will execute upon next user entry after resume"""

#     def name(self):
#         return "action_resume_conversation"

#     async def run(self, dispatcher, tracker, domain) -> List[EventType]:
#         logger.info(f"Resumed the conversation")

#         sender_id = tracker.sender_id

#         dispatcher.utter_message(
#             f"Resumed this conversation, with ID: " f"{sender_id}."
#         )

#         return []