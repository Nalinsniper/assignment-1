#-------------------------------------------------------------------------------
# Name:        assignment1
# Purpose:
# SID          21103027
# Author:      Nalin Gupta
#
# Created:     13-01-2022
# Copyright:   (c) Nalin Gupta 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# assignment question 1
a=input("enter first number")
b=input("enter second number")
c=input("enter third number")
d=(int(a)+int(b)+int(c))/3
print("the average of three numbers is :")
print(float(d))


# assignment question 2
standard_deduction=10000
depend_deduction=3000
gross=input("enter your gross income")
no_of_dependents=input("enter your number of dependents")
taxable_income=int(gross)-int(standard_deduction)-(int(dependent_deduction)+int(no_of_dependents))
tax=(float(tax))



#assignment question 3
SID=input("enter your SID")
Name=input("enter your name")
Gender=input("enter your gender")
Course_name=input("enter your course name")
CGPA=float(input("enter your CGPA"))
STUDENT=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT)


#assignment question 4
marks=[]
for i in range(5):
    marks.append(input("enter marks of students"))
    marks.sort()
    print(marks)



#assignment question 5
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("part a question : ",colour)
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple']
print("Part b of question :",colour)

