from aks.Aks import *

aks = Aks()
m = 100
count = 0
for i in range(1, m):
   if aks.isPrime(i):
      count += 1
      print(i)

print('Total', count)
