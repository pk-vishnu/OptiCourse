from flask import Flask,Blueprint,render_template,session,request,redirect,url_for,flash
from flask_login import login_required, current_user
import pandas as pd




views = Blueprint('views', __name__)


selected_choices=[]
df = pd.read_csv('../ffcs.csv')
df1=pd.read_csv('../ffcs.csv')
dfkek=df.copy()
i=0
df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
@views.route('/')
def home():
    return render_template("home.html",user=current_user)


@views.route('/ffcsgen')
@login_required
def ffcsgen():
    global df,dfkek
    courses12=dfkek['Course'].unique()
    kek=1
    if kek==1:
        courses1=courses12[:-1]
        kek+=1
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
    df1=pd.read_csv('../ffcs.csv')
    df1=df1[df1['Slot'].str.endswith('1')]
    df1=df1.reset_index(drop=True)
    df=df1.copy()
    df = df[df['Course'].isin(selected_choices)]
    df_sorted = df1.sort_values(by='Rating', ascending=False).reset_index(drop=True)
    df_sorted = df_sorted[df_sorted['Course'].isin(selected_choices)]
    df_sorted=df_sorted.reset_index(drop=True)
    x=generatett()
    return render_template("morning.html",user=current_user,table=x.to_html(classes="table table-striped"))

@views.route('/morn_gen',methods=['POST'])
@login_required
def morn_gen():
    global df_sorted
    df_sorted = df_sorted[df_sorted['Course'].isin(selected_choices)]
    x=pd.DataFrame()
    x=generatett()
    return render_template("morning.html",user=current_user,table=x.to_html(classes="table table-striped"))




@views.route('/even_gen',methods=['POST'])
@login_required
def even_gen():
    global df_sorted
    df_sorted = df_sorted[df_sorted['Course'].isin(selected_choices)]
    x=pd.DataFrame()
    x=generatett()
    return render_template("evening.html",user=current_user,table=x.to_html(classes="table table-striped"))

@views.route('/evening',methods=['POST'])
@login_required
def evening():
    global df1,selected_choices,df_sorted,df,i
    df1=pd.read_csv('../ffcs.csv')
    df1=df1[df1['Slot'].str.endswith('2')]
    df1=df1.reset_index(drop=True)
    df=df1.copy()
    df = df[df['Course'].isin(selected_choices)]
    df=df.reset_index(drop=True)
    df_sorted = df1.sort_values(by='Rating', ascending=False).reset_index(drop=True)
    df_sorted = df_sorted[df_sorted['Course'].isin(selected_choices)]
    df_sorted=df_sorted.reset_index(drop=True)
    x=generatett()
    return render_template("evening.html",user=current_user,table=x.to_html(classes="table table-striped"))

def generatett():
    global selected1, df_sorted, selected_choices, df, i,df1
    sellen=len(selected_choices)
    selc=selected_choices
    i+=1
    if i==25:
        return -9999
    else:    
        selected1 = pd.DataFrame()        
        while (selc):
            first_entry = df_sorted.iloc[0]
            selected1 = pd.concat([selected1, pd.DataFrame([first_entry])], ignore_index=True)
            df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
            selc = df_sorted['Course'].unique().tolist()

        df1 = df1[~df1['Name'].isin(selected1['Name'])].reset_index(drop=True)
        df_sorted = df1.sort_values(by='Rating', ascending=False).reset_index(drop=True)
        if (len(selected1)==sellen):
            return selected1    
        else:
            selected_entries = []
            selected_courses = set()
            selected_slots = set()
            for _, row in df.iterrows():
                course = row['Course']
                slot = row['Slot']    
                if course not in selected_courses and slot not in selected_slots:
                    selected_entries.append(row)
                    selected_courses.add(course)
                    selected_slots.add(slot)
                    if len(selected_entries) == 7:
                        break
            selected_df = pd.DataFrame(selected_entries)
            selected_df = selected_df.sample(frac=1).reset_index(drop=True)
            return selected_df

@views.route('/faculty')
@login_required
def faculty():
    df = pd.read_csv("../ffcs.csv")
    faculty = df["Name"].tolist()
    return render_template("faculty.html",user=current_user,faculty=faculty)

@views.route('/rating',methods=['POST'])
@login_required
def rating():
    if request.method == 'POST':
        rating = request.form.get('rating')
        faculty_n=request.form.get('faculty_name')

        df = pd.read_csv("../ffcs.csv")
        temprating = df.loc[df['Name'] == faculty_n, 'Rating']
        count = df.loc[df['Name'] == faculty_n, 'count']
        finalrating = ((float(temprating)*int(count))+float(rating))/int(count)+1
        df.loc[df['Name'] == faculty_n, 'Count'] = int(count)+1
        df.loc[df['Name'] == faculty_n, 'Rating'] = finalrating
        df.to_csv("../ffcs.csv", index=False)

        flash('Rating Submitted',category='sucess')
        return redirect("/")