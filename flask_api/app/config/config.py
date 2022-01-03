import os
from dotenv import load_dotenv
load_dotenv()


class development:
    HOST = "localhost"
    PORT = os.getenv("PORT", 3030)
    DEBUG = True
    SERVER_NAME = "{}:{}".format(HOST, PORT)
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class producction:
    HOST = "0.0.0.0"
    PORT = os.getenv("PORT", 3030)
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


conf = {"development": development,
        "producction": producction}
