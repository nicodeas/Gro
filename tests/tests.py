import unittest
from server import app, db
from server.models import JournalEntry, JournalPrompt, User, Mood
from werkzeug.security import generate_password_hash, check_password_hash


class UserModelCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        test_user = User(first_name='first_name', last_name='last_name',
                         username='test_user', password_hash=generate_password_hash('test_password'))
        db.session.add(test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_creation(self):
        user = User.query.filter_by(username='test_user').first()

        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.last_name, 'last_name')
        self.assertEqual(user.username, 'test_user')
        self.assertTrue(check_password_hash(
            user.password_hash, 'test_password'))
        self.assertEqual(user.moods, [])
        self.assertEqual(user.journals, [])
        self.assertEqual(user.plant_state, 0)
        self.assertEqual(user.pot_state, 0)
        self.assertEqual(user.user_rating, 0)
        self.assertFalse(user.mood_recorded)
        self.assertFalse(user.journal_recorded)
        self.assertFalse(user.breathing_complete)
        self.assertFalse(user.meditation_complete)

    def test_add_mood(self):
        user = User.query.filter_by(username='test_user').first()
        mood = Mood(mood=0, user=user)

        db.session.add(mood)
        db.session.commit()

        self.assertEqual(user.moods[0].mood, 0)

    def test_add_journal(self):
        user = User.query.filter_by(username='test_user').first()
        journal_prompt = JournalPrompt(prompt='test_prompt')
        journal_entry = JournalEntry(
            entry='test_entry', user=user, journalprompt=journal_prompt)

        db.session.add(journal_prompt)
        db.session.add(journal_entry)
        db.session.commit()

        self.assertEqual(user.journals[0].entry, 'test_entry')
        self.assertEqual(user.journals[0].journalprompt.prompt, 'test_prompt')

    def test_get_dict(self):
        user = User.query.filter_by(username='test_user').first()

        expected_result = {
            'username': 'test_user',
            'user_rating': 0,
            'moods': [],
            'journals': [],
            'plant_state': 0,
            'pot_state': 0,
            'mood_recorded': False,
            'journal_recorded': False,
            'breathing_complete': False,
            'meditation_complete': False,
            'is_prunable': False
        }
        result = user.get_dict()

        for expected in expected_result:
            self.assertEqual(result.get(expected), expected_result[expected])


if __name__ == '__main__':
    unittest.main(verbosity=2)
