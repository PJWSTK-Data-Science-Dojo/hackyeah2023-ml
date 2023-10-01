from .config_parser import config
import logging
from gpt4all import GPT4All
logging.basicConfig(level=logging.INFO)
class LLM:
    def __init__(self):
        self.model_name = config['model']['model_name']
        self.temperature = config['model']['temperature']
        self.context_intro_file = config['data']['context_intro_file']
        self.llm_query_file = config['data']['llm_query_file']
        self.llm_structure_file = config['data']['structure_file']
        self.streaming = config['model']['streaming'] #To interact with GPT4All responses as the model generates, use the streaming=True flag during generation.
        self.max_tokens = config['model']['max_tokens']
        self.top_k = config['model']['top_k']
        self.top_p = config['model']['top_p']
        #load text files 
        self.llm_query = open(self.llm_query_file, 'r').read()
        self.llm_context = open(self.context_intro_file, 'r').read()
        self.llm_structure = open(self.llm_structure_file, 'r').read()
        #objects
        self.model = GPT4All(self.model_name)
        #self.model.chat_session(f'{self.llm_context} {self.llm_structure}')
    
    def chat(self, query):
        with self.model.chat_session(f'{self.llm_context}\n{self.llm_structure}'):
            #wait for the API to respond
            connected_query = self.llm_query.replace('<FILL>', query)
            response = self.model.generate(connected_query, temp = self.temperature, top_k = self.top_k, top_p = self.top_p)
            return response
