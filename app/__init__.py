from flask import Flask
from .config import Config
from .database import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__, static='../static')
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    with app.app_context():
        db.create_all()
        
    return app

