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
    global df 
    courses12=df['Course'].unique()
    courses1=courses12[:-1]
    return render_template("ffcsgen.html",user=current_user,courses1=courses1)



@views.route('/course', methods=['POST'])
@login_required
def course():
    global selected_choices
    selected_choices = request.form.getlist('selected_choices')
    return redirect(url_for('views.time'))


@views.route('/time')
@login_required
def time():
    return render_template("time.html",user=current_user,selected_choices=selected_choices)

@views.route('/morning',methods=['POST'])
@login_required
def morning():
    global df1,selected_choices,df_sorted,df,i
    df1=df1[df1['Slot'].str.endswith('1')]
    df1=df1.reset_index(drop=True)
    df_sorted = df1.sort_values(by='Rating', ascending=False).reset_index(drop=True)
    df_sorted = df_sorted[df_sorted['Course'].isin(selected_choices)]
    df_sorted=df_sorted.reset_index(drop=True)
    x=generatett()
    return render_template("morning.html",user=current_user,table=x.to_html(classes="table table-striped"))

@views.route('/evening',methods=['POST'])
@login_required
def evening():
    global df1,selected_choices,df_sorted,df,i
    df1=df1[df1['Slot'].str.endswith('2')]
    df1=df1.reset_index(drop=True)
    df_sorted = df1.sort_values(by='Rating', ascending=False).reset_index(drop=True)
    df_sorted = df_sorted[df_sorted['Course'].isin(selected_choices)]
    df_sorted=df_sorted.reset_index(drop=True)
    x=generatett()
    return render_template("evening.html",user=current_user,table=x.to_html(classes="table table-striped"))

def generatett():
    global selected1, df_sorted, selected_choices, df, i
    sellen=len(selected_choices)
    i+=1
    if i==25:
        return
    else:    
        selected1 = pd.DataFrame()        
        while (selected_choices):
            first_entry = df_sorted.iloc[0]
            selected1 = pd.concat([selected1, pd.DataFrame([first_entry])], ignore_index=True)
            df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
            selected_choices = df_sorted['Course'].unique().tolist()

        if (len(selected1)==sellen):
            return selected1