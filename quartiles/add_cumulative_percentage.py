import pandas as pd
import sqlite3

filenames = [
    'quartiles/first_fourth.csv',
    'quartiles/second_fourth.csv',
    'quartiles/third_fourth.csv',
    'quartiles/fourth_fourth.csv'
]

def query_csv(input_csv, output_csv, i):
    result=[]
    # Step 1: Read data from CSV
    df = pd.read_csv(input_csv)

    # Step 2: In-memory SQLite DB
    conn = sqlite3.connect(':memory:')
    df.to_sql('data', conn, index=False, if_exists='replace')
    
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT SUM(Salary) FROM data")
    res= cursor.fetchone()
    sum=res[0]
    
    cursor.execute(f'SELECT Salary, Education_level, Years_of_experience FROM data')
    r = cursor.fetchall()
    percentage=0
    populayion_percentage=0
   
    for row in r:
        populayion_percentage+= round(1 / len(r),5)
        percentage += round(row[0] / sum,4) 
        result.append({"Salary": row[0],"Education_level":row[1],"Years_of_experience":row[2],"Cumulative_percentage":percentage,"Population_percentage":populayion_percentage})

    
    # Step 6: Write to CSV
    pd.DataFrame(result).to_csv(output_csv, index=False)

    conn.close()


for i in range (1,5):
    input_csv = filenames[i-1]  # Replace with your input CSV path

    query_csv(input_csv, input_csv, i)
