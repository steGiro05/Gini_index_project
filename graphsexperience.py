import matplotlib.pyplot as plt 
import csv

def get_data(file,x,y):
    with open(file,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        percentage = 0
        line_count = sum(1 for line in csv_file)
        weight = 1/line_count * 100
        csv_file.seek(0)
        
        for l in csv_reader:
            y_val = float(l[3]) * 100
            y.append(y_val)
            percentage += weight
            x.append(percentage)
           
            #print(percentage,y_val)
        

exp1_x = [0]
exp1_y = [0]
get_data("1_fourth.csv",exp1_x,exp1_y)

exp2_x = [0]
exp2_y = [0]
get_data("2_fourth.csv",exp2_x,exp2_y)

exp3_x = [0]
exp3_y = [0]
get_data("3_fourth.csv",exp3_x,exp3_y)

exp4_x = [0]
exp4_y = [0]
get_data("4_fourth.csv",exp4_x,exp4_y)

#creating line of perfect equality
plt.xlim(0,100)
plt.ylim(0,100)

x = list(range(101))
y = list(range(101))


plt.plot(exp1_x,exp1_y,c = "orange",linewidth=1,label = "Q1 (0 - 4 years of experience)")
plt.plot(exp2_x,exp2_y,c = "blue",linewidth=1,label= "Q2 (4 - 7 years of experience)")
plt.plot(exp3_x,exp3_y,c = "green",linewidth=1,label = "Q3 (7 - 12 years of experience)")
plt.plot(exp4_x,exp4_y,c = "purple",linewidth=1,label = "Q4 (12 - 34 years of experince)")
plt.plot(x,y,c = 'black',label = "Perfect equality")
plt.xlabel("Cumulative percentage of population")
plt.ylabel("Cumulative percentage of income")
plt.legend()
plt.show()
