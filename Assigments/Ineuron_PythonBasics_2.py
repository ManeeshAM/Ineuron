#%%
"""1. Create the below pattern using nested for loop in Python."""

n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

#%%
"""
2. Write a Python program to reverse a word after accepting the input from the user."""

Name = input("Enter a word to be reversed : ")
print("Output :",Name[::-1])

