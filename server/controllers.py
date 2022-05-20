from datetime import datetime
from server import app,db
from .models import User, JournalPrompt,JournalEntry
from flask_login import current_user

class GameController():
    
    @staticmethod
    def get_num_days():
      return (datetime.now().date() - current_user.last_session.date()).days
        
    
    def update_user():  
        num_days_diff = GameController.get_num_days()
        
        if num_days_diff==0:
            return
        elif num_days_diff==1:
            if current_user.pot_state==4:
                current_user.plant_state+=1
            # pot goes back to sleep
            current_user.pot_state=0
        else:
            # plant shrinks
            current_user.plant_state-=num_days_diff
            # set pot to upset
            current_user.pot_state=-1
            
        current_user.mood_recorded=False
        current_user.journal_recorded= False
        current_user.breathing_complete=False
        current_user.meditation_complete=False
        
        current_user.last_session = datetime.now()
        db.session.commit()
        
    def update_mood_recorded():
        if not current_user.mood_recorded:
            current_user.mood_recorded=True
            current_user.pot_state+=1
        current_user.last_session = datetime.now()
        db.session.commit()
            
    def update_journal_recorded():
        if not current_user.journal_recorded:
            current_user.journal_recorded=True
            current_user.pot_state+=1
        current_user.last_session = datetime.now()
        db.session.commit()
            
            
    def update_breathing_complete():
        if not current_user.breathing_complete:
            current_user.breathing_complete=True
            current_user.pot_state+=1
        current_user.last_session = datetime.now()    
        db.session.commit()

    def update_meditation_complete():
        if not current_user.meditation_complete:
            current_user.meditation_complete=True
            current_user.pot_state+=1
        current_user.last_session = datetime.now()
        db.session.commit()
        
    def prune():
        if current_user.get_dict()['is_prunable']:
            current_user.plant_state=-1
            current_user.user_rating+=1
            db.session.commit()
            
    

        