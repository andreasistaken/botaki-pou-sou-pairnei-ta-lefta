from flask import jsonify, Blueprint, request
from app.extensions import db
from app.models import Project
from app.blueprints.makeProject.functions import normalizeGithubLink, repoExists, TimeFormatGood
     
makeProject_bp = Blueprint("makeProject_bp", __name__)
     
@makeProject_bp.route('/make-project', methods=['POST'])
def makeProject():
    data = request.get_json(silent=True) or {}
     
    name = data.get("name")
    deadline = data.get("deadline")
    description = data.get("description")
    repo = normalizeGithubLink(data.get("repo"))
    amount = data.get("amount")
         
    if not all([name, deadline, description, repo, amount]):
        return jsonify({"ok": False, "error": "Missing fields"}), 400
    else:
        if not repoExists(repo):
            return jsonify({"ok": False, "error-en": "Couldn't find repo", "error-gr": "Δεν βρεθηκε το repository"})

        if not TimeFormatGood():
            return jsonify({"ok": False, "error-en": "Deadline should follow this format: %d-%m-%Y %H:%M:%S", 
                                         "error-gr": "Η ημερομηνια ληξης πρεπει να ακολουθει αυτο το format: %d-%m-%Y %H:%M:%S"
                                         })
        
        
        
        
        # return jsonify({"ok": True})