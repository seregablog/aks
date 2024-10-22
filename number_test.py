from aks.Aks import *
import sys

number = int(sys.argv[1])

aks = Aks()
if aks.isPrime(number):
    answer = 'prime'
else:
    answer = 'composite'
print('Number ' + str(number) + ' is ' + answer)

