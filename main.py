from flask import Flask
from flask_cors import CORS
from app.api import api  

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

app.register_blueprint(api, url_prefix='/api')  

if __name__ == "__main__":
    app.run(debug=True)
