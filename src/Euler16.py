'''

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

@author: Alex Greco
'''
import time


def euler16():
    total_num = 2 ** 1000
    str_num = str(total_num)
    
    sum = 0
    #for every digit in the total num
    for d in range(0,len(str_num)):
        #add the dig to the total
        sum += int(str_num[d])
        
    print(sum)
    

start_time = time.time()
euler16()
print(time.time() - start_time)