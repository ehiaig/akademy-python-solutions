"""
Task 1 (Easy)
Peter studies and lives in Barcelona. He will start an internship in Sabadell in the next year and unfortunately, he has to pay to travel for the train. The supervisor of his internship gave Peter a choice: Peter can decide for himself how many days he wants to follow the internship. Because Peter does not want to have any loan in the end of his studies, he wants to calculate how many days he can follow the internship without ending up with any debts.

Write function internship_days that calculates the amount of days Peter can travel back and forth given his income and the travel costs, rent and other expenses he has to pay every month (hint: remember that Peter needs to come back every day).

Please complete the definition of the function. Here is what you can assume about this function:

The input parameters 'income', 'travel_costs', 'rent' and 'other_expenses' are non-negative float values.
The function 'internship_days' must return a non-negative integer as its return value, reflecting the number of days Peter can afford traveling back and forth.
The returned value cannot be greater than 30 (maximum days in a month that Pieter can do the internship, for this assignment: each month contains 30 days).
"""

def internship_days(income, travel_costs, rent, other_expenses):
    return (income-rent-other_expenses)/(travel_costs*2)

internship_days(1000,12,300,100)

"""
Task 2 (Easy)
Peter wants to earn a bit more money and takes a job as a bartender at a student cafe that only serves beer (cost 2.00), wine (cost 2.50) and sodas (cost 1.50). After taking each order, Peter should calculate the amount people have to pay.

Write function calculate_payment that gets a string with the ordered drinks as single letters, where each letter indicates one ordered drink ('B' stands for beer, 'W' stands for wine and 'S' stands for sodas). The function returns the amount that should be payed for the given order.

Please complete the definition of the function. Here is what you can assume about this function:

The input parameter 'order' is a string, where each letter is either 'B', 'S' or 'W'.
The input string can be empty or it can contain multiple occurrences of the same letter.
You can assume that all letters in 'order' are capitalized, and no letters other than 'B', 'S' and 'W' can be found in 'order'.
The function 'calculate_payment' returns a float value, reflecting the total cost of drinks specified by 'order'.
Example: calculate_payment('BBSS') returns 7.0.
"""

def calculate_payment(od):
    order = {'B': 2, 'W':2.5, 'S':1.5}
    od = od.upper()
    od = list(od)
    x = []
    
    for a in od:
        if a in order.keys():
            x.append(order[a])
            print(sum(x))
calculate_payment("BBSS")


"""
Task 3 (Medium)
Implement function maximum_by which takes a pandas DataFrame and a column name, and returns the row of this DataFrame which has the largest value for the specified column. For example:

(Use the "winequality-red.csv" file stored in the assessment folder)
"""

import pandas as pd
wine = pd.read_csv("winequality-red.csv", sep=';')
papers = pd.read_table("papers.txt", delimiter='\t')

def maximum_by(x, y):
    return x.ix[x[y].idxmax()]

print(maximum_by(wine, "alcohol"))
print()
print(maximum_by(papers, "year"))
print()
print(maximum_by(papers, "cited"))

"""Task 4 (Medium)
Define function KL which computes the Kullback-Leibler divergence between two discrete probability distributions. The formula for KL-divergence is as follows:
KL(p,q)=∑i=1Npilog2(piqi)
KL(p,q)=∑i=1Npilog2⁡(piqi)
 
The function should take two vectors with non-negative numbers specifying (possibly unnormalized) probability distributions. Before computing KL-divergence, make sure both vectors sum up to 1. The function should work as follows:
"""


"""Task 5 (Hard)
Write function diagonals which takes a MxN array, returns a list of all the diagonal vectors of this array, in order from the upper right to bottom left. For example:
"""
import numpy
numpy.random.seed(41); a = numpy.random.uniform(-50,50, (4,2)).round()
print(a)

d = [a[::1,:].diagonal(i) for i in range(4,1)]
d.extend(a.diagonal(i) for i in range(1,-4,-1))
print ([n.tolist() for n in d])