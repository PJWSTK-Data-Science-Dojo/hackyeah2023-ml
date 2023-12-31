from .config_parser import config
import logging
from gpt4all import GPT4All
logging.basicConfig(level=logging.INFO)
class LLM:
    def __init__(self):
        self.model_name = config['model']['model_name']
        self.model_dir = config['model']['model_directory']
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
        self.model = GPT4All(model_path = f'{self.model_dir}', model_name=self.model_name)
        #self.model.chat_session(f'{self.llm_context} {self.llm_structure}')
        self.query = None
        self.running = False
        self.response_available = False

    def set_query(self, query):
        self.query = query

    def get_running_status(self):
        return self.running

    def get_response(self):
        self.response_available = False
        return self.response
    
    def get_response_availabilty(self):
        return self.response_available

    def chat(self):
        with self.model.chat_session(f'{self.llm_context}\n{self.llm_structure}'):
            #wait for the API to respond
            while(self.query != 'koniec'):
                if(self.query != None):
                    connected_query = self.llm_query.replace('<FILL>', self.query)
                    self.response = self.model.generate(connected_query, temp = self.temperature, top_k = self.top_k, top_p = self.top_p)
                    self.response_available = True
                    self.query = None
