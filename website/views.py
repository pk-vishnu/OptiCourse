from flask import Blueprint,render_template,session
from flask_login import login_required, current_user
views = Blueprint('views', __name__)

@views.route('/')

def home():
    return render_template("home.html",user=current_user)


@views.route('/ffcsgen')
def ffcsgen():
    return render_template("ffcsgen.html",user=current_user)