#######################################################################################################################################################
# 
# Name:Prince Kumar
# SID:
# Exam Date:740098508
# Module:BEM458 j
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-Princeexeter123
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
# Given customer feedback string and key_comments dictionary
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# As according to my  SID 740098508, the allocated keys are 7 and 8
allocated_keys = [7, 8]

# First i have created  an empty list to store the tuples (start_index, end_index)
my_list = []

# Loop over the allocated keys
for key in allocated_keys:
    word = key_comments[key]                   # for Getting the word corresponding to the key
    start = customer_feedback.find(word)        # to Find the start index of the word into the string
    end = start + len(word) - 1                   # for Calculating the end index 
    my_list.append((start, end))                 # to Append the tuple to my_list

print(my_list)



##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:08 (but zero will be omitted and taking 8 )

# Write your code for Operating Profit Margin
# Operating Profit Margin function: 
# Formula is : (Operating Profit / Revenue) * 100
def operating_profit_margin(op_profit, revenue):
    if revenue != 0:
        return (op_profit / revenue) * 100
    else:
        return None

# Write your code for Revenue per Customer
# Formula: Revenue / No of Customers
def revenue_per_customer(revenue, num_customers):
    if num_customers != 0:
        return revenue / num_customers
    else:
        return None
# Write your code for Customer Churn Rate
# Customer Churn Rate function:
# Formula: (Lost Customers / Total Customers) * 100
def customer_churn_rate(lost_customers, total_customers):
    if total_customers != 0:
        return (lost_customers / total_customers) * 100
    else:
        return None

# Write your code for Average Order Value
# Average Order Value function:
# Formula: Revenue / Number of Orders
def average_order_value(revenue, num_orders):
    if num_orders != 0:
        return revenue / num_orders
    else:
        return None
# Call your designed functions here
# Call the functions using the first_two and last_two digits
opm = operating_profit_margin(first_two, last_two)
rpc = revenue_per_customer(first_two, last_two)
churn = customer_churn_rate(first_two, last_two)
aov = average_order_value(first_two, last_two)


# Printing the results
print("Operating Profit Margin:", opm)
print("Revenue per Customer:", rpc)
print("Customer Churn Rate:", churn)
print("Average Order Value:", aov)
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
# Data points
prices = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
demands = [300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85]

# Calculate means
n = len(prices)
mean_price = sum(prices) / n
mean_demand = sum(demands) / n

# Calculate the slope (m) and intercept (b)
numerator = sum((prices[i] - mean_price) * (demands[i] - mean_demand) for i in range(n))
denom = sum((prices[i] - mean_price) ** 2 for i in range(n))
m = numerator / denom
b = mean_demand - m * mean_price

print("Regression equation: Demand = {:.4f} * Price + {:.4f}".format(m, b))

# 1. Price that  maximizes the revenue:
# Revenue R(p) = p * (m * p + b) = m*p^2 + b*p
# Maximum revenue occurs at p = -b/(2*m)  (m is negative)
p_max_revenue = -b / (2 * m)
print("Price that maximizes revenue: £{:.2f}".format(p_max_revenue))

# 2. Demand when price is set at £52:
demand_at_52 = m * 52 + b
print("Estimated demand at £52: {:.2f} units".format(demand_at_52))
##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and your Student ID
max_value = int(input("Enter your Student ID: "))  # Using int() instead of integer()
random_numbers = [random.randint(1, max_value) for i in range(100)]



# Plotting the numbers in a line chart
plt.plot(random_numbers, 
         marker='o', 
         markerfacecolor='green', 
         markeredgecolor='red', 
         linestyle='--', 
         label='Random Numbers', 
         color='blue')

plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()



