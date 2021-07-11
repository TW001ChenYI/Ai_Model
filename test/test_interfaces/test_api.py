#from test_application import test_ai_model
#import test_application.test_ai_model
import time
#import application.test_ai_model
#import test_application.test_ai_loadmodel
#import test_domain.test_ai_gen
#from flask import jsonify, request
import flask
from flask_cors import CORS
#import interfaces.api 
import test_application.test_ai_model
import test_domain.test_ai_gen
app = flask.Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    results = []
    start_time = time.time()
    results = test_domain.test_ai_gen.generate_text(test_application.test_ai_model.infer_model, start_string="孫楚恩打敗盧瑞山", num_generate=1000, temperature=0.9)
    end_time = time.time()
    print('推論花了：',end_time - start_time,'秒的時間')
    return results
app.run(host='0.0.0.0',port='1124')

