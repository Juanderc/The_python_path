from flask import Flask
from app.routes.routes import app_bp
from app.config.config import config

app = Flask(__name__)
app.register_blueprint(app_bp)
app.config.from_object(config["development_config"])


def initApp():
    app.run()
