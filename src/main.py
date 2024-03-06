from flask import Flask
from api.routes import catalogue_blueprint

app = Flask(__name__)

app.register_blueprint(catalogue_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
