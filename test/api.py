import test_application.test_ai_model
import test_application.test_ai_loadmodel
import test_domain.test_ai_gen

import time
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}})

temperature=0.1
start_string="孫楚恩打敗盧瑞山"
num_generate=100

@app.route('/test', methods=['GET'])
def home():
    results = []
    start_time = time.time()
    results = test_domain.test_ai_gen.generate_text(test_application.test_ai_model.infer_model, start_string=start_string, num_generate=num_generate, temperature=temperature)
    end_time = time.time()
    print('推論花了：',end_time - start_time,'秒的時間')
    print(results)
    return results

app.run(host='0.0.0.0',port='1124')
