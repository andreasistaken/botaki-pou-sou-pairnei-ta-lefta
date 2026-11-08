from app.extensions import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    deadline = db.Column(db.String)
    description = db.Column(db.String)
    githubRepo = db.Column(db.String)
    amount = db.Column(db.Integer)
    BTCwallet = db.Column(db.String)