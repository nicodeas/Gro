from flask import Blueprint

test_bp = Blueprint('test_bp', __name__,url_prefix='/test')
@test_bp.route('/')
def check():
    return {"server":"online!"}
