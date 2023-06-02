import pandas as pd
print("Hello World")
df = pd.read_csv('ffcs - Copy.csv')

print(df)

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
print(df)

print("--------------------")
df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
print(df_sorted)

print("--------------------")
courses = df['Course'].unique().tolist()
print(courses)
selected1 = pd.DataFrame()

while (courses):
    first_entry = df_sorted.iloc[0]
    selected1 = pd.concat([selected1, pd.DataFrame([first_entry])], ignore_index=True)
    df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
    courses = df_sorted['Course'].unique().tolist()

print("-----First Choice-----")
print(selected1)

df = pd.merge(df, selected1, how='left', indicator=True)
df = df[df['_merge'] == 'left_only'].drop('_merge', axis=1).reset_index(drop=True)
df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
selected2 = pd.DataFrame()
courses = df['Course'].unique().tolist()
while (courses):
    first_entry = df_sorted.iloc[0]
    selected2 = pd.concat([selected2, pd.DataFrame([first_entry])], ignore_index=True)
    df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
    courses = df_sorted['Course'].unique().tolist()

print("-----Second Choice-----")
print(selected2)

df = pd.merge(df, selected2, how='left', indicator=True)
df = df[df['_merge'] == 'left_only'].drop('_merge', axis=1).reset_index(drop=True)
df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
selected3 = pd.DataFrame()
courses = df['Course'].unique().tolist()
while (courses):
    first_entry = df_sorted.iloc[0]
    selected3 = pd.concat([selected3, pd.DataFrame([first_entry])], ignore_index=True)
    df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
    courses = df_sorted['Course'].unique().tolist()

print("-----Third Choice-----")
print(selected3)