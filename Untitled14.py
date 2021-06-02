#!/usr/bin/env python
# coding: utf-8

# A program that ask the user to input their age, weight and height. Display the resulting BMI of the person, provided the are not too young or elder. Let the person know if the BMI is overweight, healthy or underweight. 

# In[ ]:


def bmi(weight, height): #
    "Function that calculates the Body Mass Index of a person" #
    bmi = weight/(height*height)
    return BMI #


# In[ ]:


print("Input the requested details to calculate your BMI")
print("\nAge")
age = int(input()) # insert the data type
if age <13 and age >70:
    print(f"\nThe age submitted is INVALID. try again")
else:
    print("\nWeight in Kg:")
weight = float(input()) # insert the data type
height = float(input()) # insert data type
BMI = weight/(height*height)
result = bmi(weight, height) # insert your function
if result > 25: # insert a condition that can classify this
    print(f"\nYour BMI is:{result} and it shows you are overweight")
elif result < 18:
    print(f"\nYour BMI is: {result} and it shows you are underweight")
else:
    print(f"\nYour BMI is: {result} anad it shows you are healthy:)")


# In[ ]:




