from server import db
from server.models import User

User.query.filter(User.username == 'test-uname').delete()

db.session.commit()