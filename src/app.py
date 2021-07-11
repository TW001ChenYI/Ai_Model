import interfaces.api 

import flask
from flask_cors import CORS

app = flask.Flask(__name__)
app.register_blueprint(interfaces.api.bp)
app.config["JSON_AS_ASCII"] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ =='__main__':
    app.run(host='0.0.0.0',port='5000')
