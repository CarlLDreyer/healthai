from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Use a service account
cred = credentials.Certificate('./healthai-436fe-14510acc52fa.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

class ActionHelp(Action):

    def name(self) -> Text:
        return "action_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                buttons = {"buttons":
                [
                    {"title": "Breast", "payload": "'attribute':'Breast cancer'"},
                    {"title": "Colorectal", "payload": "'attribute':'Colorectal cancer'"},
                    {"title": "Leukemia", "payload": "'attribute':'Leukemia'"}
                ]}
                dispatcher.utter_message(f"I can help you find information about breast cancer, colorectal cancer, leukemia, and their symptoms!", attachment=buttons)
            except:
                dispatcher.utter_message(template="utter_ask_again", tracker = tracker)
            
            return []


class ActionSearchCancer(Action):

    def name(self) -> Text:
        return "action_cancer_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                cancer_type = tracker.get_slot("cancer_type")
                if cancer_type is None:
                    dispatcher.utter_message(template="utter_ask_again", tracker = tracker)
                else:
                    valid_cancer_type = validate_cancer_type(cancer_type)
                    if valid_cancer_type is None:
                        dispatcher.utter_message(template="utter_ask_again", tracker = tracker)
                    else:
                        doc_ref = db.collection(u'healthai').document(u'diseases').collection(u'cancer').document(valid_cancer_type)
                        doc = doc_ref.get()
                        docToDict = doc.to_dict()
                        desc = docToDict['description']
                        buttons = [{"title": "Symptoms 💊", "payload": "'attribute':'symptoms'"}, {"title": "Treatments", "payload": "'attribute':'treatments'"}]
                        link = {"link": docToDict['link'], "buttons": buttons}
                        dispatcher.utter_message(f"{desc}", attachment=link)
            except:
                dispatcher.utter_message(template="utter_ask_again", tracker = tracker)

            return []
 

class ActionSymptomsCancer(Action):

    def name(self) -> Text:
        return "action_cancer_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                cancer_type = tracker.get_slot("cancer_type")
                if cancer_type is None:
                    dispatcher.utter_message(template="utter_ask_again", tracker = tracker)
                else:
                    valid_cancer_type = validate_cancer_type(cancer_type)
                    if valid_cancer_type is None:
                        dispatcher.utter_message(template="utter_ask_again", tracker = tracker)
                    else:
                        doc_ref = db.collection(u'healthai').document(u'diseases').collection(u'cancer').document(valid_cancer_type)
                        doc = doc_ref.get()
                        docToDict = doc.to_dict()
                        symptoms = docToDict['symptoms']
                        test = {"symptoms": symptoms}
                        dispatcher.utter_message(f"The symptoms for {valid_cancer_type} cancer are: ", attachment=test)
            except:
                dispatcher.utter_message(template="utter_ask_again", tracker = tracker)

            return []

class ActionCancerTreatmenets(Action):

    def name(self) -> Text:
        return "action_cancer_treatments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                cancer_type = tracker.get_slot("cancer_type")
                if cancer_type is None:
                    dispatcher.utter_message(template="utter_ask_again", tracker = tracker)
                else:
                    valid_cancer_type = validate_cancer_type(cancer_type)
                    if valid_cancer_type is None:
                        dispatcher.utter_message(template="utter_ask_again", tracker = tracker)
                    else:
                        doc_ref = db.collection(u'healthai').document(u'diseases').collection(u'cancer').document(valid_cancer_type)
                        doc = doc_ref.get()
                        docToDict = doc.to_dict()
                        treatments = docToDict['treatments']
                        test = {"treatments": treatments}
                        dispatcher.utter_message(f"The treatments for {valid_cancer_type} cancer are: ", attachment=test)
            except:
                dispatcher.utter_message(template="utter_ask_again", tracker = tracker)

            return []

def validate_cancer_type(cancer_type):
    word = cancer_type.lower()
    to_compare_cancer = extract_cancer_types()

    correct_type = process.extractOne(word, to_compare_cancer)

    resulted = [fuzz.ratio(correct_type[0], word)]

    if resulted.index(max(resulted)) == 0 and max(resulted) > 60:
      required_index = to_compare_cancer.index(correct_type[0])
      return to_compare_cancer[required_index]
    return None

def validate_word(wordType, lookupTable):
    word = wordType.lower()
    to_compare = extract_types(lookupTable)

    correct_type = process.extractOne(word, to_compare)

    resulted = [fuzz.ratio(correct_type[0], word)]

    if resulted.index(max(resulted)) == 0 and max(resulted) > 60:
        required_index = to_compare.index(correct_type[0])
        return to_compare[required_index]
    return None

def extract_types(lookupTable):
    file = open('data/lookup_tables/' + lookupTable)
    file_lines = file.readlines()
    valid_types = []

    for f_type in file_lines:
        valid_types.append(f_type.strip())
    file.close()

    return valid_types

def extract_cancer_types():
    """
        extract all possible cancer types
    """

    file = open("data/lookup_tables/cancer.txt")
    file_lines = file.readlines()
    valid_cancer_type = []

    for f_type in file_lines:
        valid_cancer_type.append(f_type.strip())
    file.close()

    return valid_cancer_type
