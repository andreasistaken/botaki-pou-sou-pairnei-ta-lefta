from flask import Flask
from app.extensions import db
from app.blueprints.makeProject.makeproject import makeProject_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(makeProject_bp)

import app.models  
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='localhost', port=3000, debug=True)