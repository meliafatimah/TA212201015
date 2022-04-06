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
        print('aksi berhasil diekstrak : ',aksi)
        ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
        print('ruangan berhasil diekstrak : ',ruangan)
        barang=next(tracker.get_latest_entity_values("barang"),None)
        print('barang berhasil diekstrak : ',barang)
        if not aksi:
            print('inside if of aksi')
            msg=f"Tolong beritahu apa yang harus aku lakukan"
            dispatcher.utter_message(text=msg)
            aksi=next(tracker.get_latest_entity_values("aksi"),None)
            print('inside if of aksi, aksi taken',aksi)
            return []
        if not ruangan:
            print('inside if of ruangan')
            msg=f"Tolong beritahu tujuan ruangan untuk mengantar"
            dispatcher.utter_message(text=msg)
            aksi=next(tracker.get_latest_entity_values("ruangan"),None)
            print('inside if of ruangan, ruangan taken',ruangan)
            return []
        if not barang:
            print('inside if of ruangan')
            msg=f"Tolong beritahu barang yang harus diantar"
            dispatcher.utter_message(text=msg)
            aksi=next(tracker.get_latest_entity_values("barang"),None)
            print('inside if of barang, barang taken',barang)
            return []
        dispatcher.utter_message(text="Baik, tolong beritahu nama anda dan nama orang yang dituju ya!")


class ActionReadRuangan(Action):

    def name(self) -> Text:
        return "action_read_ruangan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        ruangan=next(tracker.get_latest_entity_values("ruangan"),None)
        print('ruangan berhasil diekstrak : ',ruangan)
        dispatcher.utter_message(text="Ruangan tujuan adalah {ruangan}")


class ActionReadBarang(Action):

    def name(self) -> Text:
        return "action_read_barang"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        barang=next(tracker.get_latest_entity_values("barang"),None)
        print('barang berhasil diekstrak : ',barang)
        dispatcher.utter_message(text="Nama barang adalah {barang}")