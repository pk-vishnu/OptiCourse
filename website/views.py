from flask import Flask,Blueprint,render_template,session,request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)




@views.route('/')

def home():
    return render_template("home.html",user=current_user)


@views.route('/ffcsgen')
@login_required
def ffcsgen():
    import pandas as pd
    df = pd.read_csv('ffcs.csv')
    df1=pd.read_csv('ffcs.csv')
    courses1=df1['Course'].unique()
    return render_template("ffcsgen.html",user=current_user,courses1=courses1)

@views.route('/process_form', methods=['POST'])
@login_required
def process_form():
    selected_choices = request.form.getlist('selected_choices')
    return f"Selected Choices: {selected_choices}"