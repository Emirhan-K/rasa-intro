# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions




from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher




class ActionHavaDurumuSorgula(Action):
    def name(self) -> Text:
        return "action_hava_durumu_sorgula"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sehir = tracker.get_slot("sehir")
        
        if sehir:
            try:
                # Hava durumu API'sine istek yapma işlemi
                api_key = "your_api_key"
                base_url = "http://api.openweathermap.org/data/2.5/weather"
                params = {
                    "q": sehir,
                    "appid": api_key,
                    "units": "metric"
                }
                response = requests.get(base_url, params=params)
                response.raise_for_status()
                data = response.json()

                hava_durumu = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                
                

                dispatcher.utter_message(text=f"{sehir} şehrinde hava {hava_durumu}, sıcaklık {temp} °C.")
                
            except requests.exceptions.HTTPError as http_err:
                dispatcher.utter_message(text="Hava durumu API'sine istek yapılırken bir HTTP hatası oluştu.")
            except requests.exceptions.RequestException as req_err:
                dispatcher.utter_message(text="Hava durumu bilgisi alınırken bir ağ hatası oluştu.")
            except (KeyError, IndexError):
                dispatcher.utter_message(text="Hava durumu bilgisi alınırken beklenmedik bir hata oluştu.")
        else:
            dispatcher.utter_message(text="Özür dilerim, şehri anlayamadım. Lütfen tekrar deneyin.")

        return []
        
class ActionSaatSorgula(Action):
    def name(self) -> Text:
        return "action_saat_sorgula"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        try:
            # Sistem saatini alıyoruz
            su_anki_saat = datetime.now().strftime("%H:%M")
            dispatcher.utter_message(text=f"Şuanda saat {su_anki_saat}.")
        except Exception as e:
            dispatcher.utter_message(text="Şuanda saati göremiyorum. Lütfen tekrar deneyin.")
            print(e)
        

        return []

    
