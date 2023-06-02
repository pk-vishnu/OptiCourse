import pandas as pd
df = pd.read_csv('ffcs.csv')

print("--------------------")
print("Press 1 for Morning Theory and 2 for Evening Theory")
choice = int(input())
if choice == 1:
    df = df[df['Slot'].str.endswith('1')]
elif choice == 2:
    df = df[df['Slot'].str.endswith('2')]
else:
    print("Invalid input!")
df = df.reset_index(drop=True)

df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)

courses = df['Course'].unique().tolist()
selected1 = pd.DataFrame()
i=0

def generatett():
    global selected1, df_sorted, courses, df, i
    i+=1
    while (courses):
        first_entry = df_sorted.iloc[0]
        selected1 = pd.concat([selected1, pd.DataFrame([first_entry])], ignore_index=True)
        df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
        courses = df_sorted['Course'].unique().tolist()

    print(f"Choice {i}")
    print(selected1)

    df = pd.merge(df, selected1, how='left', indicator=True)
    df = df[df['_merge'] == 'left_only'].drop('_merge', axis=1).reset_index(drop=True)
    df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
    selected1 = pd.DataFrame()
    courses=df['Course'].unique().tolist()

print("-------------------\nChoose one of the given options:\n1. Generate Time Table\n2. Exit")
menuinput = int(input())
while menuinput != 2:
    generatett()
    print("-------------------\nChoose one of the given options:\n1. Generate Time Table\n2. Exit")
    menuinput = int(input())