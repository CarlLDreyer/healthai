## greet path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## help
* help
  - action_help

## search_cancer
* cancer{"cancer_type": "breast"}
  - action_cancer_search
* thanks
  - utter_goodbye

## search cancer + type
* cancer
 - utter_ask_cancer_type
* inform{"cancer_type": "breast"}
 - action_cancer_search
* thanks
 - utter_goodbye

## search cancer + symptoms
* cancer{"cancer_type": "breast"}
 - action_cancer_search
* symptoms_cancer
 - action_cancer_symptoms
* thanks
  - utter_goodbye

## search cancer + type + symptoms
* cancer
 - utter_ask_cancer_type
* inform{"cancer_type": "breast"}
 - action_cancer_search
* symptoms_cancer
  - action_cancer_symptoms
* thanks
 - utter_goodbye

## symptoms cancer breast
* symptoms_cancer{"cancer_type": "breast"}
  - action_cancer_symptoms
* thanks
  - utter_goodbye

## symptoms cancer + type
* symptoms_cancer
 - utter_ask_cancer_symptom_type
* inform{"cancer_type": "breast"}
 - action_cancer_symptoms
* thanks
 - utter_goodbye

## search cancer treatments
* treatments_cancer{"cancer_type": "breast"}
  - action_cancer_treatments
* thanks
  - utter_goodbye

## search cancer + treatments
* cancer{"cancer_type": "breast"}
  - action_cancer_search
* treatments_cancer
  - action_cancer_treatments
* thanks
  - utter_goodbye

## search cancer + type + treatments
* cancer
  - utter_ask_cancer_type
* inform{"cancer_type": "breast"}
  - action_cancer_search
* treatments_cancer
  - action_cancer_treatments
* thanks
  - utter_goodbye

## treatments cancer breast
* treatments_cancer{"cancer_type": "breast"}
  - action_cancer_treatments
* thanks
  - utter_goodbye

## treatments cancer + type
* treatments_cancer
  - utter_ask_cancer_symptom_type
* inform{"cancer_type": "breast"}
  - action_cancer_treatments
* thanks
  - utter_goodbye
