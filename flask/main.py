import os
from flask.api import create_app
from flask.config import Development as conf

environment = os.getenv("AFTERGLOW_ENV", "development")

app = create_app(environment)

if __name__ == "__main__":
    app.run(port=conf.PORT)
