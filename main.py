import pandas as pd
print("Hello World")
df = pd.read_csv('ffcs.csv')

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
selected = pd.DataFrame()

while (courses):
    first_entry = df_sorted.iloc[0]
    selected = pd.concat([selected, pd.DataFrame([first_entry])], ignore_index=True)
    df_sorted = df_sorted[(df_sorted['Course'] != first_entry['Course']) & (df_sorted['Slot'] != first_entry['Slot'])].reset_index(drop=True)
    courses = df_sorted['Course'].unique().tolist()

print(df_sorted)
print(selected)