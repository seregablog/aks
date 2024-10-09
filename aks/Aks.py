import math
from aks.PolyMod import PolyMod


class Aks:
    def isPrime(self, n: int) -> bool:
        if (self.isPerfectPower(n)):
            return False

        r = self.findR(n)

        if self.checkGcd(n, r):
            return False
        
        if (n <= r):
            return True
        
        if (self.checkPolynom(n, r)):
            return False
    
        return True

    def isPerfectPower(self, n: int) -> bool:
        maxB = math.ceil(math.log(n, 2))
        if maxB <= 2:
            maxB = 3
            
        for b in range(2, maxB):
            if pow(math.floor(pow(n, 1.0 / b)), b) == n:
                return True
        return False
    
    def findR(self, n: int) -> int:
        ord = math.ceil(math.log(n, 2) ** 2)
        r = 2

        while True:
            find = True
            for j in range(1, ord):
                if pow(n, j, r) == 1:
                    find = False
                    break
            if (find):
                return r
            else:
                r += 1
    
    def checkGcd(self, n: int, r: int) -> bool:
        for a in range(2, r + 1):
            gcd = math.gcd(a, n)
            if gcd > 1 and gcd < n:
                return True
        return False
    
    def checkPolynom(self, n: int, r: int) -> bool:
        max = math.ceil(math.sqrt(self.__euler(r)) * math.log(n, 2))
        
        for a in range(1, max):
            p1 = PolyMod([a, 1], n, r) ** n
            p2 = PolyMod([a] + [0] * (n - 1) + [1], n, r).mod()
            if not p1 == p2:
                print('A=', a)
                print(p1)
                print(p2)
                return True

        return False

    def __euler(self, m: int) -> int:
        euler = 0
        for i in range(1, m + 1):
            if math.gcd(m, i) == 1:
                euler += 1
        return euler
