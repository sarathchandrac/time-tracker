from flask import Flask, json, jsonify
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    test_config = None

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),


            SWAGGER={
                'title': "Bookmarks API",
                'uiversion': 3
            }
        )
    else:
        app.config.from_mapping(test_config)

    @app.get('/')
    def index():
        return "Running server successfully"

    @app.get('/hello')
    def hello():
        return jsonify({ "message": "Running server successfully"})
    
    return app