import re
import typing
from rasa.nlu.components import Component
import actions as ac

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

if typing.TYPE_CHECKING:
  from spacy.tokens.doc import Doc

class PreProcessText(Component):
  name = "preprocess"

  def __init__(self, component_config = None):
    super(PreProcessText, self).__init__(component_config)
    self.cancer_types = ac.extract_cancer_types()
    
  def fuzzy_wozzy(self, word):
    word = word.lower()
    to_compare_cancer, original_cancer = self.cancer_types

    correct_type = process.extractOne(word, to_compare_cancer)

    resulted = [fuzz.ratio(correct_type[0], word)]

    if resulted.index(max(resulted)) == 0 and max(resulted) > 60:
      required_index = to_compare_cancer.index(correct_type[0])
      return original_cancer[required_index]

  def process(self, message, **kwargs):
    text = message.text
    text = re.sub(r'(?:(?<=\-) | (?=\-))', '', text)
    message.text = text
