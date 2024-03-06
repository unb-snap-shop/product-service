from flask import Flask
from api.routes import catalogue_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(catalogue_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
