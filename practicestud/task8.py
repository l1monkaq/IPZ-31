import pandas as pd

try:
    df = pd.read_csv('students.csv')
    
    subjects = df.columns[2:]
    df['Average'] = df[subjects].mean(axis=1).round(2)
    
    print("--- Student Table ---")
    print(df[['Прізвище', "Ім'я", 'Average']])
    
    print("\n--- Group Average per Subject ---")
    print(df[subjects].mean().round(2))

except FileNotFoundError:
    print("Error: File 'students.csv' not found.")