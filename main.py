from flask import Flask, request, Response
from llm.llm import LLM
import regex as re
from llm.vanna_model import VannaModel
from threading import Thread
from query_translation import Translation
from ddl_converter import translate

app = Flask('api_flask')

llm_objects = {}

translator = Translation()

@app.route('/chat/v2', methods=['POST'])
def retreive_query_v2():
    data = request.json
    query = data.get('query')
    hash = data.get('hash')
    if hash not in llm_objects:
        llm_objects[hash] = VannaModel()
    llm_obj = llm_objects[hash]
    response = llm_obj.chat(query)
    return {'output':response}



@app.route('/chat/', methods=['GET'])
def retreive_query():
    data = request.json
    query = data.get('query')
    hash = data.get('hash')
    if query == 'koniec':
        #check if hash exists
        if hash in llm_objects:
            del llm_objects[hash]
        return Response("", status=200, mimetype='application/json')
    #translate from [auto] to polish
    query = translator.translate(query)
    #multiuser and context support
    if hash not in llm_objects:
        llm_objects[hash] = LLM()
        llm_objects[hash].running = True
        thread = Thread(target=llm_objects[hash].chat)
        thread.start()

    llm_objects[hash].set_query(query)
    #wait for the respond
    while(llm_objects[hash].get_response_availabilty() == False):
        pass
    response = llm_objects[hash].get_response()

    #check if response is empty
    if "```" not in response:
        return Response("{'output':'not found'}", status=404, mimetype='application/json')
    response_clear = re.findall(r'```(\n(.*)\n)```', response)
    #get first group    
    return {'output':response_clear[0][1]}

    

    


@app.route('/structure/', methods=['POST'])
def retreive_context():
    data = request.json

    #validate if input is in DDL format
    ddl_code = data.get('context')
    print(ddl_code)
    matches = re.findall(r':', ddl_code) #TODO: validation
    if len(matches) == 0:
        return Response("", status=400, mimetype='application/json')
    with open('llm/data/structure.txt', 'w') as f:
        new_context = translate(ddl_code)
        f.write(new_context)
    return Response("", status=200, mimetype='application/json')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
