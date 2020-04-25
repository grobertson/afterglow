from flask import Flask, render_template, request
from pprint import pprint
import json

def load(app: Flask) -> Flask:
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/webhook/plex", methods=['POST'])
    def webhook():
        event = json.loads(request.form['payload'])['event']
        if event == 'media.play':
            meta = json.loads(request.form['payload'])['Metadata']
            print("\n\n---------")
            print(' '.join((meta['grandparentTitle'], meta['parentTitle'])))
            print(meta['title'])
            #print(' '.join(('Rating: ', meta['contentRating'])))
            print(meta['summary'])
            print("---------")
            error = None
        else:
            print("\n\n---------")
            print(event)
            print("---------")
        return render_template("plex_webhook.html")    
    
    return app
