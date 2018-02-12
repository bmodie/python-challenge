import os
import csv
import pandas as pd 
import dateutil


# Path to collect data
budget_data_1_CSV = os.path.join('budget_data_1.csv')
budget_data_2_CSV = os.path.join('budget_data_2.csv')

# df = pd.read_csv(budget_data_1_CSV, names=['Date', 'Revenue'])
# df1 = pd.read_csv(budget_data_2_CSV, header=None)

# all_budget_data = pd.concat([df, df1], axis=0)

numbers1 = budget_data_1_CSV[1]
numbers2 = budget_data_2_CSV[2]
# Define the function and have it accept the 'BD1' as its sole parameter
#def data_insights(revenue):
    
    # total # of months in dataset
#total_months = str(all_budget_data[0])

    # total revenue gained
total_rev = sum(float(numbers1) + float(numbers2))

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
    # print("Total Months: " + total_months)
print("Total Revenue: " + total_rev)
    #print("Average Revenue Change: " + avg_rev)
    #print("Greatest Increase in Revenue: " + greatest_incr)
    #print("Greatest Decrease in Revenue: " + greatest_decr)
