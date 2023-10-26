import vanna as vn
from .config_parser import config
import subprocess #catch output from shell

class VannaModel:
    def __init__(self):
        vn.set_api_key(config['vanna']['api_key'])
        vn.set_model(config['vanna']['model'])
    
    def chat(self, query):
        return vn.generate_sql(query)
    
        