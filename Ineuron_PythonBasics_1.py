#%%
#Program 1
"""1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line."""

y=[]
for x in range(2000,3200):
    if (x%7==0) and (x%5==0):
        y.append(str(x))
print(','.join(y))    

#%%
##Program 2
""" 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name. """



First_name = input("Enter your First name : ") 
print(First_name)
Last_name = input("Enter your Last name : ") 
print(Last_name)
print(First_name[::-1] + " " + Last_name[::-1])  



#%%
##Program 2
"""
3. Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3"""

Diameter = int(12)
Radius =  Diameter/2 
Volume_of_sphere =  ((4/3) * 3.14 * (Radius**3))
print("The Volume of Sphere is :" + str(f'{Volume_of_sphere:.2f}'))