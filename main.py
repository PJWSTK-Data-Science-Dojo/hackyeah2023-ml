from flask import Flask, request, Response
from llm.llm import LLM
import regex as re

app = Flask('api_flask')

llm_objects = {}

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
    #multiuser support
    if hash not in llm_objects:
        llm_objects[hash] = LLM()
    llm_obj = llm_objects[hash]
    response = llm_obj.chat(query)
    if "```" not in response:
        return Response("{'output':'not found'}", status=404, mimetype='application/json')
    response_clear = re.findall(r'```(\n(.*)\n)```', response)
    #clean output
    resp = response_clear[0]
    if ',' in response_clear[0]:
        resp = response_clear.split(',')[1]
    return {'output':resp}

    

    


@app.route('/structure/', methods=['POST'])
def retreive_context():
    data = request.json
    print(data.get('context'))
    #delete context file
    with open('llm/data/structure.txt', 'w') as f:
        f.write(data.get('context'))
    return Response("", status=200, mimetype='application/json')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)