from server import app, db
from flask import request, abort
from .models import JournalPrompt, JournalEntry, Mood
from .controllers import GameController
from flask_login import current_user, login_required
import random


@app.route('/api/user-gamestate', methods=["GET"])
@login_required
def api_get_game_state():
    return current_user.get_dict()


@app.route('/api/meditation', methods=["POST"])
@login_required
def api_post_meditation():
    # posting to this endpoint will be enough to update game state
    GameController.update_meditation_complete()
    return {}


@app.route('/api/breathing', methods=["POST"])
@login_required
def api_post_breathing():
    # posting to this endpoint will be enough to update game state
    GameController.update_breathing_complete()
    return {}


@app.route('/api/journal', methods=["POST"])
@login_required
def api_post_journal():
    # post data in this format
    # {
    #     "prompt_id":##,
    #     "entry":##,
    # }
    user_id = current_user.id
    prompt_id = request.form['prompt_id']
    entry = request.form['entry']

    if entry == "" or not prompt_id:
        abort(500, description="Missing fields")

    journal_entry = JournalEntry(
        user_id=user_id, entry=entry, journal_prompt_id=prompt_id)
    db.session.add(journal_entry)
    db.session.commit()
    GameController.update_journal_recorded()
    return {}


@app.route('/api/mood', methods=['POST'])
@login_required
def api_post_mood():
    # post data in this format
    # {
    #     "mood":##,
    # }
    user_id = current_user.id
    mood = request.form['mood']

    if mood == "":
        abort(500, description="Missing fields")

    new_mood = Mood(mood=mood, user_id=user_id)
    db.session.add(new_mood)
    db.session.commit()
    GameController.update_mood_recorded()
    return {}


@app.route('/api/create-journal-prompt', methods=["POST"])
@login_required
def api_create_journal_prompt():
    # post data in this format
    # {
    #     "journal_prompt":##,
    # }
    if current_user.username != 'admin':
        abort(405, description="Not allowed for non admin users")
    else:
        prompt = request.form['journal_prompt']
        if prompt == "":
            abort(500, description="Missing fields")
        new_journal_prompt = JournalPrompt(prompt=prompt)
        db.session.add(new_journal_prompt)
        db.session.commit()
        return {}


@app.route('/api/get-prompt', methods=["GET"])
@login_required
def api_get_journal_prompt():
    prompts = JournalPrompt.query.all()
    prompt = random.choice(prompts)
    if not prompt:
        abort(204, description='No prompts in database')
    else:
        return {prompt: prompt}
