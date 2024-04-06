from flask import Blueprint, render_template, request, flash, jsonify, Response, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json, logging

views = Blueprint("views", __name__)

logging.basicConfig(filename="app.log", level=logging.INFO, format="[%(asctime)s] %(levelname)s %(name)s: %(message)s")

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(text=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")
            logging.info(f"Note added by user: {current_user.email}")
            
    return render_template("home.html", user=current_user)

@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    note_id = note["note_id"]
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            logging.info(f"Note deleted by user: {current_user.email}")

    return jsonify({})

@views.route("/edit-note/<int:note_id>", methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            if request.method == "POST":
                new_text = request.form.get("new_text")
                if len(new_text) < 1:
                    flash("Note is too short!", category="error")
                else:
                    note.text = new_text
                    db.session.commit()
                    flash("Note updated!", category="success")
                    logging.info(f"Note edited by user: {current_user.email}")
                    return redirect(url_for("views.home"))
            return render_template("edit_note.html", user=current_user, note=note)
        else:
            flash("You don't have permission to edit this note.", category="error")
    else:
        flash("Note not found.", category="error")
    
    return redirect(url_for("views.home"))

@views.route("/download-notes", methods=["GET"])
@login_required
def download_notes():
    logging.info(f"Notes downloaded by user: {current_user.email}")
    notes = Note.query.filter_by(user_id=current_user.id).all()

    text_data = ""
    for note in notes:
        text_data += f"Note ID: {note.id}\n"
        text_data += f"Text: {note.text}\n\n"

    response = Response(
        text_data,
        content_type="text/plain",
        headers = {
            "Content-Disposition": "attachment; filename=notes.txt"
        }
    )

    return response