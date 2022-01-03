import os
from dotenv import load_dotenv


class development_config:
    HOST = "0.0.0.0"
    PORT = os.getenv("PORT", 8080)
    DEBUG = True
    SECRET_KEY = os.getenv("DEVELOPMENT_SECRET_KEY")


class production_config:
    HOST = "0.0.0.0"
    PORT = os.getenv("PORT", 8080)
    SECRET_KEY = os.getenv("PRODUCTION_SECRET_KEY")


config = {
    "development_config": development_config,
    "production_config": production_config,
}
