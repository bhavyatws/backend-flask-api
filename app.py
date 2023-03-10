from flask import Flask, jsonify
import subprocess
import openai
import main
import jsonpickle
from flask_cors import CORS, cross_origin



# import json
# from json import dumps

app =Flask(__name__)
CORS(app, support_credentials=True)
app.debug = True

@app.route('/run-script')
def run_script():
    result =main.index()
    # result = subprocess.run(['python', 'main.py'], stdout=subprocess.PIPE)
    # output = result.stdout.decode('utf-8')
    print(result)
    # data = jsonify(result)
    return jsonify(result)
    # res_list = result
    # return jsonpickle.encode(res_list)
if __name__ == 'main':
    app.run()
