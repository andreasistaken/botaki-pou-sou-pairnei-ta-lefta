from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from extensions import db
from models import Project
from functions import normalizeGithubLink, repoExists
     
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
        if repoExists(repo):
            return jsonify({"ok": True})
        return jsonify({"ok": True})


