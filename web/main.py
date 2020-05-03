import os
from app import create_app


app = create_app(os.getenv("production", "development"))


if __name__ == "__main__":
    app.run(port=3001)
