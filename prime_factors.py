import time
import math 

def factorization(n):
    fact = []
    i = 2
    while i <= math.sqrt(n):     
        if n % i == 0:      
            fact.append(i)
            n//= i
        else:
            i+=1

    fact.append(n)

    return fact

def countBits(number):   
    return int((math.log(number) / math.log(2)) + 1)



number = 7894561230225782697289577897808978978897897897987898798789887987897978978

bits = countBits(number)

print('Number informed: ' + str(number))
print('Bits: '  + str(bits))
print('Bytes: '  + str(math.ceil(bits/8)))

start = time.time()

factorization(number)

print('It took ' + str(time.time() - start) + ' seconds to find all the prime factors.')
print('Factors found: ' +  str(factorization(number)))