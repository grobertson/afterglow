from flask import Flask, render_template, request
from pprint import pprint
import json

def load(app: Flask) -> Flask:
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/plex/webhook", methods=['POST', 'GET'])
    def webhook():
        #pprint(request)
        print("---------")
        print(json.loads(request.form['payload'])['event'])
        pprint(json.loads(request.form['payload']))
        print("---------\n\n")
        error = None
        if request.method == 'POST':
            return render_template("plex_webhook.html", hook=request.form)
        return render_template("plex_webhook.html")
    
    return app
