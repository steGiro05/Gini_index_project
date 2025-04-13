import sqlite3
import pandas as pd 
import re

filenames = [
    'quartiles/first_fourth.csv',
    'quartiles/second_fourth.csv',
    'quartiles/third_fourth.csv',
    'quartiles/fourth_fourth.csv'
]

result_list=[]
quartiles=[
    0,
    4.0,
    7.0,
    12.0,
    50.0
]
for i in range (1,5):   
    salaries=[] 
    df = pd.read_csv(filenames[i-1])

    conn = sqlite3.connect(':memory:')  # In-memory database

    df.to_sql('my_table', conn, index=False, if_exists='replace')

    cursor = conn.cursor()

    cursor.execute("SELECT AVG(Salary) FROM my_table")
    res= cursor.fetchone()
    avg_salary = res[0]
    conn.close()
    
    
    result_list.append({"Years of experience": f'{quartiles[i-1]} - {quartiles[i]}', "Average": avg_salary})

results_df = pd.DataFrame(result_list)

results_df.to_csv('results/avg_experience.csv', index=False)