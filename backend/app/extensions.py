from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

cors = CORS(origins=["http://localhost:5173"])
db = SQLAlchemy()