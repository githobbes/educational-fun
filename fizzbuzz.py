""" 
My fizzbuzz solution

Author: Jordan R. Hall, Date: 12/16/2020

Main feature: script which prints (on a new line) every integer from 1 to 100
              but replacing all factors of 3 with 'fizz,' factors of 5 with 'buzz', and
              factors of both with 'fizzbuzz' 
"""

my_string = '\n 1 \n'

for i in range(2,101):

    if i % 15 == 0:
        my_string += '\n fizzbuzz \n'
        
    elif i % 5 == 0:
        my_string += '\n buzz \n'
        
    elif i % 3 == 0:
        my_string += '\n fizz \n'
    
    else:
        my_string += '\n '+ str(i) + '\n'
        
print(my_string)
        