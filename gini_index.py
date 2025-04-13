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



result_list=[]
for i in range (1,4):   
    salaries=[] 
    df = pd.read_csv(f'education_level_{i}.csv')    

    conn = sqlite3.connect(':memory:')  # In-memory database

    df.to_sql('my_table', conn, index=False, if_exists='replace')

    cursor = conn.cursor()

    cursor.execute("SELECT Salary, Cumulative_percentage, Population_percentage FROM my_table order by Salary")
    res= cursor.fetchall()
    for row in res:
        salaries.append({"salary":int(row[0]),"Cumulative_percentage":float(row[1]),"Population_percentage":float(row[2])})
    conn.close()
    
    
    gini = gini_index(salaries)
    result_list.append({"Education level": i, "Gini Index": gini})

results_df = pd.DataFrame(result_list)

results_df.to_csv('results/gini_index_education.csv', index=False)