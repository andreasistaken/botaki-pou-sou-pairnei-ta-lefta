from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from functions import repoExists

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    deadline = db.Column(db.String)
    description = db.Column(db.String)
    githubRepo = db.Column(db.String)
    amount = db.Column(db.Integer)
    BTCwallet = db.Column(db.String)

with app.app_context():
    db.create_all()

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    
    if data:
        return jsonify({"test": "Hello!"})

@app.route('/make-project', methods=['POST'])
def makeProject():
    data = request.get_json()

    name = data.get("name")
    deadline = data.get("deadline")
    description = data.get("description")
    repo = data.get("repo")
    amount = data.get("amount")

    if name and deadline and description and repo and amount:
        return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(
        host='localhost',
        port=3000,
        debug=True
    )