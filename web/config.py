import os


class Production():
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "secret")


config = {
    "production": Production
}
