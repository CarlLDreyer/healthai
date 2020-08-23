## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:help
- how can you help me?
- what can you do?
- what can you do for me?
- help
- help me
- can you help me?
- what can I ask you?
- what can you answer?

## intent:thanks
- thank you
- thanks

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## lookup:cancer
  data/lookup_tables/cancer.txt

## lookup:treatments
  data/lookup_tables/treatments.txt

## intent:inform
 - [breast](cancer_type) cancer
 - [leukemia](cancer_type)
 - [colorectal](cancer_type) cancer
 - [chemotherapy](treatment_type)

## intent:cancer
  - cancer
  - what is cancer
  - what is [breast](cancer_type) cancer
  - what is [leukemia](cancer_type)
  - what is [colorectal](cancer_type) cancer

## intent:symptoms_cancer
  - cancer symptoms
  - what are the symptoms for cancer
  - what are the symptoms for [breast](cancer_type) cancer
  - [breast](cancer_type) symptoms
  - what are the symptoms for [leukemia](cancer_type)
  - [leukemia](cancer_type) symptoms
  - what are the symptoms for [colorectal](cancer_type) cancer
  - [colorectal](cancer_type) symptoms

## intent:treatments_cancer
  - cancer treatments
  - what are the treatments for cancer
  - what are the treatments for [breast](cancer_type) cancer
  - what are the treatments for [leukemia](cancer_type)
