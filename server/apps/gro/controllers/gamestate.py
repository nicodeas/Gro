from server.models import db, User, JournalEntry, Mood
from datetime import datetime


class GameController():

    def __init__(self, id):
        self.current_user = User.query.get_or_404(id)

    def update_game(self):

        num_days_missed = (datetime.now().date() -
                           self.current_user.last_session.date()).days
        tasks_completed = self.current_user.mood_recorded + self.current_user.journal_recorded + \
            self.current_user.activity_one_complete + \
            self.current_user.activity_two_complete

        if num_days_missed == 0:
            return
        else:

            if num_days_missed > 0:
                self.current_user.plant_state -= (num_days_missed+1)
            elif tasks_completed == 4:
                self.current_user.plant_state += 1
            elif tasks_completed == 0:
                self.current_user.plant_state -= 1
            if self.current_user.plant_state < -1:
                self.current_user.plant_state = -1

            self.current_user.pot_state = -1

            self.current_user.mood_recorded = False
            self.current_user.journal_recorded = False
            self.current_user.activity_one_complete = False
            self.current_user.activity_two_complete = False

        self.current_user.last_session = datetime.now()
        db.session.commit()

    def add_journal(self, journalEntry):
        journalentry = JournalEntry(
            user_id=self.current_user.id, entry=journalEntry)

        self.current_user.journal_recorded = True
        self.current_user.last_session = datetime.now()

        db.session.add(journalentry)
        db.session.commit()

    def add_mood(self, mood):
        moodEntry = Mood(user_id=self.current_user.id, mood=mood)

        self.current_user.mood_recorded = True
        self.current_user.pot_state = 0
        self.current_user.last_session = datetime.now()

        db.session.add(moodEntry)
        db.session.commit()
