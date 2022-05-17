# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from dis import dis
import logging
import socket
import json
# import mysql.connector

from typing import Any, Text, Dict, List
from urllib import response

from database_connectivity_aksi import DataUpdateAksi
from database_connectivity_perintah import DataUpdatePerintah
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ConversationPaused, ConversationResumed, SlotSet, AllSlotsReset


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
            ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
            return []
        if not barang:
            msg=f"Tolong beritahu barang yang harus diantar"
            dispatcher.utter_message(text=msg)
            barang=next(tracker.get_latest_entity_values("barang"),None)
            return []

        SlotSet("aksi_entry", aksi)
        SlotSet("ruangan_entry", ruangan)
        SlotSet("barang_entry", barang)

        print('aksi berhasil diekstrak : ',tracker.get_slot("aksi_entry"))
        print('ruangan berhasil diekstrak : ',tracker.get_slot("ruangan_entry"))
        print('barang berhasil diekstrak : ',tracker.get_slot("barang_entry"))

        dispatcher.utter_message(response="utter_read_aksi")
        if tracker.get_slot("pengirim_entry") == None and tracker.get_slot("penerima_entry") == None:
            dispatcher.utter_message(text="Baik, tolong beritahu nama anda dan nama orang yang dituju ya!")
            pengirim=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="pengirim"),None)
            SlotSet("pengirim_entry", pengirim)
            penerima=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="penerima"),None)
            SlotSet("penerima_entry", penerima)
        elif tracker.get_slot("pengirim_entry") == None:
            dispatcher.utter_message(text="Baik, tolong beritahu nama anda ya!")
            pengirim=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="pengirim"),None)
            SlotSet("pengirim_entry", pengirim)
            # dispatcher.utter_message(response="utter_send_aksi")
        elif tracker.get_slot("penerima_entry") == None:
            dispatcher.utter_message(text="Baik, tolong beritahu nama orang yang dituju ya!")
            penerima=next(tracker.get_latest_entity_values(entity_type="nama", entity_role="penerima"),None)
            SlotSet("penerima_entry", penerima)
            # dispatcher.utter_message(response="utter_send_aksi")
        
        




class ActionReadRuangan(Action):

    def name(self) -> Text:
        return "action_read_ruangan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
        print('ruangan berhasil diekstrak : ',ruangan)
        dispatcher.utter_message(response="utter_read_ruangan")
        return[SlotSet("ruangan_entry", ruangan)]


class ActionReadBarang(Action):

    def name(self) -> Text:
        return "action_read_barang"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        barang=next(tracker.get_latest_entity_values("barang"),None)
        print('barang berhasil diekstrak : ',barang)
        dispatcher.utter_message(response="utter_read_barang")
        return[SlotSet("barang_entry", barang)]

class ActionReadPerintah(Action):

    def name(self) -> Text:
        return "action_read_perintah"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        perintah=next(tracker.get_latest_entity_values("perintah"),None)
        parameter=next(tracker.get_latest_entity_values("parameter"),None)
        # satuan=next(tracker.get_latest_entity_values("satuan"),None)
        if not perintah:
            msg=f"Tolong beritahu aku harus maju atau mundur"
            dispatcher.utter_message(text=msg)
            perintah=next(tracker.get_latest_entity_values("perintah"),None)
            SlotSet("parameter_entry", parameter)
            print('parameter berhasil diekstrak : ',tracker.get_slot("parameter_entry"))
            return []
        elif not parameter:
            msg=f"Tolong beritahu berapa meter aku harus bergerak"
            dispatcher.utter_message(text=msg)
            parameter=next(tracker.get_latest_entity_values("parameter"),None)
            SlotSet("perintah_entry", perintah)
            print('perintah berhasil diekstrak : ',tracker.get_slot("perintah_entry"))
            return []
        else:
            SlotSet("perintah_entry", perintah)
            SlotSet("parameter_entry", parameter)
            print('parameter berhasil diekstrak : ',tracker.get_slot("parameter_entry"))
            print('perintah berhasil diekstrak : ',tracker.get_slot("perintah_entry"))
        return[]


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
        SlotSet("pengirim_entry", pengirim)
        SlotSet("penerima_entry", penerima)
        print('pengirim berhasil diekstrak : ',tracker.get_slot('pengirim_entry'))
        print('penerima berhasil diekstrak : ',tracker.get_slot('penerima_entry'))
        dispatcher.utter_message(response="utter_read_nama")
        if tracker.get_slot("aksi_entry") == None and tracker.get_slot("ruangan_entry") == None and tracker.get_slot("barang_entry") == None:
            dispatcher.utter_message(text="Baik, tolong beritahu kemana aku harus mengantar dan apa yang harus aku antar ya!")
            aksi="delivery"
            ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
            barang=next(tracker.get_latest_entity_values("barang"),None)
            SlotSet("aksi_entry", aksi)
            SlotSet("ruangan_entry", ruangan)
            SlotSet("barang_entry", barang)
            # dispatcher.utter_message(response="utter_send_aksi")
        elif tracker.get_slot("aksi_entry") == None and tracker.get_slot("ruangan_entry") == None:
            dispatcher.utter_message(text="Baik, tolong beritahu kemana aku harus mengantar ya!")
            aksi="delivery"
            ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
            SlotSet("aksi_entry", aksi)
            SlotSet("ruangan_entry", ruangan)
            # dispatcher.utter_message(response="utter_send_aksi")
        elif tracker.get_slot("aksi_entry") == None and tracker.get_slot("barang_entry") == None:
            dispatcher.utter_message(text="Baik, tolong beritahu apa yang harus aku antar ya!")
            aksi="delivery"
            barang=next(tracker.get_latest_entity_values("barang"),None)
            SlotSet("aksi_entry", aksi)
            SlotSet("barang_entry", barang)
            # dispatcher.utter_message(response="utter_send_aksi")        
        

class ActionSendDatabaseAksi(Action):
    """Send data to MySQL"""

    def name(self):
        return "action_send_database_aksi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DataUpdateAksi(tracker.get_slot("aksi_entry"),    
                   tracker.get_slot("ruangan_entry"),
                   tracker.get_slot("pengirim_entry"),
                   tracker.get_slot("penerima_entry"),
                   tracker.get_slot("barang_entry")) 
        dispatcher.utter_message(response="utter_send_aksi")
        print('aksi pengantaran barang berhasil dikirim ke database')

        return [AllSlotsReset()]

class ActionSendDatabasePerintah(Action):
    """Send data to MySQL"""

    def name(self):
        return "action_send_database_perintah"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        DataUpdatePerintah(tracker.get_slot("perintah_entry"),    
                            tracker.get_slot("parameter_entry")) 
        dispatcher.utter_message(response="utter_send_perintah") 
        print('perintah pergerakan berhasil dikirim ke database')

        return [AllSlotsReset()]

# class ActionPauseConversation(Action):
#     """Pause a conversation"""

#     def name(self):
#         return "action_paused_conversation"

#     def run(self, dispatcher, tracker, domain):

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

# class ActionSendDataRos(Action):
#     """To send data entity aksi and ruangan"""

#     def name(self):
#         return "action_send_data_ros"
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.bind(("192.168.43.49", 7787))
#         sock.listen(5)

#         jsonData = {"aksi":str(tracker.get_slot('aksi_entry')),"ruangan":str(tracker.get_slot('ruangan_entry'))}
#         jsonData = json.dumps(jsonData)

#         (conn, addr) = sock.accept()
#         conn.send(jsonData.encode("UTF-8"))

