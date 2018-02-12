import os
import csv
import pandas as pd 
import dateutil

# Path to collect data
budget_data_1_CSV = os.path.join('budget_data_1.csv')
budget_data_2_CSV = os.path.join('budget_data_2.csv')

# convert to datafile
df = pd.read_csv(budget_data_1_CSV, names=['Date', 'Revenue'])
df1 = pd.read_csv(budget_data_2_CSV, header=None)

# concatenate the two files
all_budget_data = pd.concat([df, df1], axis=0)

# Define the function
def data_insight(all_budget_data):
    for revenue in all_budget_data:
        sum(all_budget_data[1])
    
    # total revenue gained
#total_rev = sum(float(numbers1) + float(numbers2))

    # total # of months in dataset
    #total_months = str(all_budget_data[0])

    # average change in revenue between months
    #avg_rev = 

    # greatest increase in revenue (date, amount)
    #greatest_incr = 

    # greatest decrease in revenue (date, amount)
    #greatest_decr = 

    # Print Results
    print("Financial Analysis")
    print("------------------------------------------------")
    print(" ")
    print(revenue)
    # print("Total Months: " + total_months)
#print("Total Revenue: " + total_rev)
    #print("Average Revenue Change: " + avg_rev)
    #print("Greatest Increase in Revenue: " + greatest_incr)
    #print("Greatest Decrease in Revenue: " + greatest_decr)
