from aks.Aks import *

m = 1000
count = 0
for i in range(1, m):
   if aksTest.isPrime(i):
      count += 1
      print(i)

print('Total', count)
