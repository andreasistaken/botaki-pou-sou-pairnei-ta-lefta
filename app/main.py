from flask import Flask
from app.extensions import db
from app.blueprints.makeProject.makeproject import makeProject_bp

from app.config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.ensure_ascii = False

db.init_app(app)
app.register_blueprint(makeProject_bp)

from app import models
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(
            host=config.host, 
            port=config.port, 
            debug=config.debug
           )