from deep_translator import GoogleTranslator

class Translation:
    def __init__(self):
        self.translator = GoogleTranslator(source='auto', target='en')

    def translate(self, query):
        return self.translator.translate(query)

