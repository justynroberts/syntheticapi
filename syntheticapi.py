# Supplied AS IS. Feel free to modify for any other purposes. 
# Intended as a short term fix for implementing an API to control
# The Instana.yaml as an API.

import flask
import yaml
from flask import request

app = flask.Flask(__name__)
# app.config["DEBUG"] = True
api = '/api/synthetics'

def openfile():
    with open(r'configuration-synthetics.yaml') as file:
        itemlist = yaml.load(file, Loader=yaml.FullLoader)
        sanitisedlist = itemlist['com.instana.plugin.ping']['endpoints']
        file.close
        return sanitisedlist

def savefile(list):
    with open(r'configuration-synthetics.yaml', 'w') as file:
        endpointdict = {'endpoints':list}
        fullyaml = {'com.instana.plugin.ping':endpointdict}
        documents = yaml.dump(fullyaml, file)
        file.close
        return list

@app.route(api, methods=['GET'])
def get_entry():
        return (openfile())

@app.route(api, methods=['POST'])
def set_entry():
    monitortype = request.args.get('type')
    label = request.args.get('label')
    target = request.args.get('target')
    
    list = openfile()
    entry = {'target':target,'type':monitortype}
    list[label] = entry
    print(entry)
    
    return savefile(list)

@app.route(api, methods=['DELETE'])

def delete_entry():
    label = request.args.get('label')
    endpointlist = openfile()

    try: 
        del endpointlist[label]
    except:
        return ("Error. Did the key exist?")

    savefile(endpointlist)
    return "Deleted"

if __name__ == "__main__":
        app.run(host= '0.0.0.0')