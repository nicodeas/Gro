from server import app,db
from flask import  request, abort
from .models import JournalPrompt,JournalEntry,Mood
from .controllers import GameController
from flask_login import current_user, login_required

@app.route('/api/user-gamestate',methods=["GET"])
@login_required
def api_get_game_state():
    return current_user.get_dict()

@app.route('/api/meditation',methods=["POST"])
@login_required
def api_post_meditation():
    # posting to this endpoint will be enough to update game state
    GameController.update_meditation_complete()
    return {}

@app.route('/api/breathing',methods=["POST"])
@login_required
def api_post_breathing():
    # posting to this endpoint will be enough to update game state
    GameController.update_breathing_complete()
    return {}

@app.route('/api/journal',methods=["POST"])
@login_required
def api_post_journal():
    # post data in this format
    # {
    #     "prompt_id":##,
    #     "entry":##,
    # }
    user_id = current_user.id
    data = request.get_json()
    prompt_id = int(data.get('prompt_id'))
    entry = data.get('entry')
    
    if entry=="" or not user_id or not prompt_id:
        abort(500,description="Missing fields")
    
    journal_entry = JournalEntry(user_id= user_id,entry=entry,journal_prompt_id=prompt_id)
    db.session.add(journal_entry)
    db.session.commit()
    GameController.update_journal_recorded()
    return {}

@app.route('/api/mood',methods=['POST'])
@login_required
def api_post_mood():
    # post data in this format
    # {
    #     "mood":##,
    # }
    user_id = current_user.id
    data = request.get_json()
    
    mood = int(data.get('mood'))
    
    if mood=="" or not user_id:
        abort(500,description="Missing fields")
        
    new_mood = Mood(mood=mood,user_id=user_id)
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
    data = request.get_json()
    if current_user.username != 'admin':
        abort(405,description="Not allowed for non admin users")
    else:
        prompt = data.get('journal_prompt')
        if prompt=="":
            abort(500,description="Missing fields")
        new_journal_prompt = JournalPrompt(prompt = prompt)
        db.session.add(new_journal_prompt)
        db.session.commit()
        return {}