from sqlalchemy import desc
from server.models import User, db
from flask import Blueprint, request
from .controllers.gamestate import GameController

user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route('/', methods=["POST"])
def create_user():
    data = request.get_json() or {}
    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()
    return {}


@user_blueprint.route('/', methods=["GET"])
def retrieve_users():
    user_list = User.query.all()
    users = {}
    for user in user_list:
        users[user.id] = user.get_dict()
    print(users)
    return users


@user_blueprint.route('/leaderboard')
def get_leaderboard():
    user_list = User.query.order_by(desc(User.user_rating))
    leaderboard = {}
    position = 0

    for user in user_list:
        position += 1
        leaderboard[position] = user.get_username()
    print(leaderboard)
    return leaderboard


@user_blueprint.route('/<int:user_id>', methods=["GET"])
def retrieve_user(user_id):
    GameController(user_id).update_game()
    user = User.query.get(user_id)
    return user.get_dict()


@user_blueprint.route('/<int:user_id>/add-journal', methods=["POST"])
def add_journal(user_id):
    data = request.get_json() or {}
    GameController(user_id).add_journal(data['journalEntry'])
    return {}


@user_blueprint.route('/<int:user_id>/add-mood', methods=["POST"])
def add_mood(user_id):
    data = request.get_json() or {}
    GameController(user_id).add_mood(data['mood'])
    return {}
