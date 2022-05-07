"""
Structured English:

This program will output 3 values; number of grades, average grade, and percentage of grades that are above average.

In order to determine the number of grades in the class, the program will count the total number of items in the list.

To calculate the average grade, the program will add the total scores and divide by the number of grades in the class.

As for calculating the percentage of the above average grade, the program must depict whether the current grade being checked surpasses the average grade. The counter variable will allow us to keep track of the amount of grades that are above average and then the program will divide that number by the total number of grades in the class. 

After calculating each value, the program will print out the values of Number of grades: , Average grade: , and Percentage of grades above average: 

"""

"""
Pseudo-code:

infile = open 
#assign items in text to variable called grades
grades = [line.rstrip()]

#convert items in list to integer type 
for items in Final.txt
change grades at variable i to int

grade_average = sum of total grade / # of grades in list

initialize grade_average by dividing sum of the grade  and # of grades in list
counter = 0   # placeholder for the numbers of grades that are above the average grade


#Find the amount of grades that are above average
for every grade in grades
    if grade is greater than grade_average
    increment counter by 1

set grades_above_avg to: counter divided by total # of grades in the list, multiply by 100 to get percentage value

print total amount of grades
print average grade
print percentage of grades above average


"""
