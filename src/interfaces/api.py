import application.ai_loadmodel
import application.ai_model
import domain.ai_gen 

import time
from flask import Blueprint, jsonify, request
bp=Blueprint('bp',__name__)

@bp.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!Go To text_gen?start_string=，&num_generate=&temperature=</h1>"

@bp.route('/text_gen', methods=['GET'])
def text_gen():
    if 'start_string' in request.args:
        start_string = request.args['start_string']
    else:
        return "Error: No start_string provided. Please specify a start_string."
    if 'num_generate' in request.args:
        num_generate = request.args['num_generate']
    else:
        return "Error: No num_generate provided. Please specify a num_generate."
    if 'temperature' in request.args:
        temperature = request.args['temperature']
    else:
        return "Error: No temperature provided. Please specify a temperature."
     
    print(start_string,num_generate,temperature)
    results = []
    start_time = time.time()
    results = domain.ai_gen.generate_text(application.ai_model.infer_model, start_string=start_string, num_generate=num_generate, temperature=temperature)
    # print(results)
    end_time = time.time()
    print('推論花了：',end_time - start_time,'秒的時間')

    return results
#app.app.run(host='0.0.0.0')
