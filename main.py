import pandas as pd
import random as rand
df = pd.read_csv('ffcs.csv')
df1=pd.read_csv('ffcs.csv')
courses1=df1['Course'].unique().tolist()

print("--------------------")
print("Press 1 for Morning Theory and 2 for Evening Theory")
choice = int(input())
if choice == 1:
    df = df[df['Slot'].str.endswith('1')]
    df1=df1[df1['Slot'].str.endswith('1')]
    slots=['A1','B1','C1','D1','E1','F1','G1']
elif choice == 2:
    df = df[df['Slot'].str.endswith('2')]
    df1=df1[df1['Slot'].str.endswith('2')]
    slots=['A2','B2','C2','D2','E2','F2','G2']
else:
    print("Invalid input!")
df = df.reset_index(drop=True)
df1=df1.reset_index(drop=True)

df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)

courses = df['Course'].unique().tolist()
selected1 = pd.DataFrame()
i=0

def generator():
    global df1,choice
    df1 = df1.sample(frac=1).reset_index(drop=True)
    selected_entries = []
    selected_courses = set()
    selected_slots = set()
    for _, row in df1.iterrows():
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
    df1=pd.read_csv('ffcs.csv')
    if choice == 1:
        df1 = df1[df1['Slot'].str.endswith('1')]
    elif choice == 2:
        df1 = df1[df1['Slot'].str.endswith('2')]
    return selected_df

def generatett():
    global selected1, df_sorted, courses, df, i
    i+=1
    if i==25:
        print("No Time Table Possible")
        return -1
    else:    
        selected1 = pd.DataFrame()        
        while (courses):
            first_entry = df_sorted.iloc[0]
            selected1 = pd.concat([selected1, pd.DataFrame([first_entry])], ignore_index=True)
            df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
            courses = df_sorted['Course'].unique().tolist()

        print(f"Choice {i}")
        if (len(selected1)==7):
            print(selected1)
        else:
            selected1=generator()
            print(selected1)

        df = pd.merge(df, selected1, how='left', indicator=True)
        df = df[df['_merge'] == 'left_only'].drop('_merge', axis=1).reset_index(drop=True)
        df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
        courses=df['Course'].unique().tolist()
        return

print("-------------------\nChoose one of the given options:\n1. Generate Time Table\n2. Exit")
menuinput = int(input())
while menuinput != 2:
    x=generatett()
    if x==-1:
        break
    print("-------------------\nChoose one of the given options:\n1. Generate Time Table\n2. Exit")
    menuinput = int(input())