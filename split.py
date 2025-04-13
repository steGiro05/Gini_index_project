import pandas as pd
import sqlite3

def query_csv(input_csv, output_csv, i):
    result=[]
    # Step 1: Read data from CSV
    df = pd.read_csv(input_csv)

    # Step 2: In-memory SQLite DB
    conn = sqlite3.connect(':memory:')
    df.to_sql('data', conn, index=False, if_exists='replace')
    
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT SUM(Salary) FROM data WHERE Education_Level= {i}")
    res= cursor.fetchone()
    sum=res[0]
    
    cursor.execute(f'SELECT Salary FROM data WHERE Education_Level= {i} order by Salary')
    r = cursor.fetchall()
    percentage=0
    populayion_percentage=0
    for row in r:
        percentage += round(row[0] / sum,4)
        populayion_percentage += round(1/len(r),6)
        result.append({"Salary": row[0],"Cumulative_percentage":percentage, "Population_percentage": populayion_percentage})


    # Step 6: Write to CSV
    pd.DataFrame(result).to_csv(output_csv, index=False)

    conn.close()


for i in range (1,4):
    input_csv = f'Salary.csv'  # Replace with your input CSV path
    output_csv = f'education_level_{i}.csv'  # Replace with your output CSV path

    query_csv(input_csv, output_csv, i)
