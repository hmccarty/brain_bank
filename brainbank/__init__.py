import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        from . import db
        from . import routes
    
        db.init_app(app)
        
        return app