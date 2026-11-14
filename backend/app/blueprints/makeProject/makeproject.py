from flask import jsonify, Blueprint, request
from backend.app.extensions import db
from backend.app.models import Project
from backend.app.blueprints.makeProject.functions import normalizeGithubLink, repoExists, TimeFormatGood
     
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
        return jsonify({"ok": False, "error": "Missing fields", "success-message": None}), 400
    else:
        if not repoExists(repo):
            return jsonify({"ok": False, 
                            "error": "Couldn't find repo",
                            "success-message": None
                            })
        
        if not TimeFormatGood(deadline):
            return jsonify({"ok": False, 
                            "error": "Deadline should follow this format: %d-%m-%Y %H:%M:%S",
                            "success-message": None
                            })

        if not len(description) > 46:
            return jsonify({"ok": False,
                            "error": "Description too short.",
                            "success-message": None,
                            "length": len(description)
                            })
        if not int(amount) > 0:
            return jsonify({"ok": True,
                            "error": "Amount needs to be a positive value",
                            "success-message": None
                            })

        project = Project(name=name, deadline=deadline, description=description, githubRepo=repo, amount=amount)
        db.session.add(project)
        db.session.commit()
        
        return jsonify({"ok": True,
                        "error": None,
                        "success-message": "Project was successfully created."})