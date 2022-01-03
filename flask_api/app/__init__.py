from flask import Flask
from app.routes.routes import app_bp
from app.config.config import conf
from app.database.database import db

app = Flask(__name__)

app.config.from_object(conf["development"])
app.register_blueprint(app_bp)


def initApp():
    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.run()
