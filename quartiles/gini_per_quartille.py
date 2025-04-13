import sqlite3
import pandas as pd 
import re

def gini_index(sorted_salaries):
    # Ensure data is sorted by Population_percentage (ascending)
    sorted_salaries = sorted(sorted_salaries, key=lambda x: x["Population_percentage"])
    
    # Add (0, 0) if missing
    if sorted_salaries[0]["Population_percentage"] != 0 or sorted_salaries[0]["Cumulative_percentage"] != 0:
        sorted_salaries.insert(0, {"Population_percentage": 0, "Cumulative_percentage": 0})
    
    sum_area = 0
    n = len(sorted_salaries)
    
    for i in range(1, n):
        x1 = sorted_salaries[i - 1]["Population_percentage"]
        x2 = sorted_salaries[i]["Population_percentage"]
        y1 = sorted_salaries[i - 1]["Cumulative_percentage"]
        y2 = sorted_salaries[i]["Cumulative_percentage"]
        
        # Area of trapezoid
        area = (x2 - x1) * (y1 + y2)
        sum_area += area
    
    gini = 1 -  sum_area
    return gini

        


filenames = [
    "quartiles/first_fourth.csv",
    "quartiles/second_fourth.csv",
    "quartiles/third_fourth.csv",
    "quartiles/fourth_fourth.csv"
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

    cursor.execute("SELECT Salary, Cumulative_percentage, Population_percentage FROM my_table order by Salary")
    res= cursor.fetchall()
    for row in res:
        salaries.append({"salary":int(row[0]),"Cumulative_percentage":float(row[1]),"Population_percentage":float(row[2])})
    conn.close()
    
    
    gini = gini_index(salaries)
    result_list.append({"Years of experience": f'{quartiles[i-1]} - {quartiles[i]}', "Gini Index": gini})

results_df = pd.DataFrame(result_list)

results_df.to_csv('results/gini_index_experience.csv', index=False)

