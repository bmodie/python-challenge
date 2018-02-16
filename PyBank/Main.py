import pandas as pd 

# Path to collect data
budget_data_1_csv = "budget_data_1.csv"
budget_data_2_csv = "budget_data_2.csv"

# Create dataframe
budget_data_1_df = pd.read_csv(budget_data_1_csv, encoding = "ISO-8859-1")
budget_data_2_df = pd.read_csv(budget_data_2_csv, encoding = "ISO-8859-1")

# Merge the two data sources
budget_merge = pd.merge(budget_data_1_df, budget_data_2_df)

# Define the function and have it accept the 'BD1' as its sole parameter

    
# total # of months in dataset
    

# total revenue gained
    

# average change in revenue between months
    

# greatest increase in revenue (date, amount)
    

# greatest decrease in revenue (date, amount)
    

# Print Results
print("Financial Analysis")
print("------------------")
#print("Total Months: " + str(total_months))
#print("Total Revenue: " + str(total_revenue)
#print("Average Revenue Change: " + str(avg_revenue_change))
#print("Greatest Increase in Revenue: " + str(greatest_revenue_increase))
#print("Greatest Decrease in Revenue: " + str(greatest_revenue_decrease))
