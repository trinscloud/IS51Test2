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


#Find the amount of grades that are above average
initialize calculate_percent_above_average() function

counter = 0   # placeholder for the numbers of grades that are above the average grade
for every grade in grades
    if grade is greater than grade_average
    increment counter by 1
return 100*(counter/number of total grades)

initialize main function
print total amount of grades
print average grade
print percentage of grades above average


"""

# Python code
infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()

for i in range(len(grades)):
    grades[i] = int(grades[i])

# solve for grade average by finding sum of total grades and dividing by amount of grades in the class
grade_average = sum(grades)/len(grades)


def calculate_percent_above_average():
    # program determines whether grade being checked is greater than the average grade, then counter variable will be incremented by 1
    counter = 0    #placeholder variable for grades that are above average
    for grade in grades:
        if grade > grade_average:
            counter += 1

    # calculates percentage of grades that are above the average grade
    return 100*(counter/len(grades))


def main():
    print("Number of grades: ", len(grades))
    print("Average grade: ", grade_average)
    print("Percentage of grades above average:  {0:.2f}%".format(calculate_percent_above_average()))


