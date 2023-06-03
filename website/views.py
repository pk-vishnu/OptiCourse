from flask import Flask,Blueprint,render_template,session,request,redirect,url_for
from flask_login import login_required, current_user
import pandas as pd




views = Blueprint('views', __name__)


selected_choices=[]
df = pd.read_csv('../ffcs.csv')
df1=pd.read_csv('../ffcs.csv')
i=0
df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
@views.route('/')
def home():
    return render_template("home.html",user=current_user)


@views.route('/ffcsgen')
@login_required
def ffcsgen():
    global df1 
    courses12=df1['Course'].unique()
    courses1=courses12[:-1]
    return render_template("ffcsgen.html",user=current_user,courses1=courses1)



@views.route('/course', methods=['POST'])
@login_required
def course():
    global selected_choices
    selected_choices = request.form.getlist('selected_choices')
    return redirect(url_for('views.morning'))


@views.route('/time')
@login_required
def time():
    return render_template("time.html",user=current_user,selected_choices=selected_choices)

@views.route('/morning')
@login_required
def morning():



    return render_template("morning.html",user=current_user,selected_choices=selected_choices)