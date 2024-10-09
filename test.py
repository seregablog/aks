import unittest
from aks.Aks import *
from aks.PolyMod import *


class TestAks(unittest.TestCase):
    
    def testIsPerfectPowerTrue(self):
        aks = Aks()
        self.assertTrue(aks.isPerfectPower(4))
        self.assertTrue(aks.isPerfectPower(9))
        self.assertTrue(aks.isPerfectPower(16))
        self.assertTrue(aks.isPerfectPower(100))
    

    def testIsPerfectPowerFalse(self):
        aks = Aks()
        self.assertFalse(aks.isPerfectPower(2))
        self.assertFalse(aks.isPerfectPower(3))
        self.assertFalse(aks.isPerfectPower(35))
        self.assertFalse(aks.isPerfectPower(101))
    
    def testFindR(self):
        aks = Aks()
        self.assertEqual(29, aks.findR(31))
        self.assertEqual(263, aks.findR(74513))
    
    def testCheckGcdTrue(self):
        aks = Aks()
        self.assertTrue(aks.checkGcd(4, 2))
        self.assertTrue(aks.checkGcd(15, 4))
        self.assertTrue(aks.checkGcd(15, 3))
    
    def testCheckGcdFalse(self):
        aks = Aks()
        self.assertFalse(aks.checkGcd(35, 4))
    
    def testPolyAdd(self):
        x = PolyMod([1, 2, 0], 5, 2)
        y = PolyMod([3, 4], 5, 2)
        expect = PolyMod([4, 1], 5, 2)
        
        self.assertEqual(expect, x + y)
    
    def testPolyMul(self):
        x = PolyMod([1, 2], 5, 4)
        y = PolyMod([0, 3], 5, 4)
        expect = PolyMod([0, 3, 1], 5, 4)
        
        self.assertEqual(expect, x * y)
    
    def testPolyMod(self):
        x = PolyMod([2, 0, 3, 0, 1], 5, 2)
        expect = PolyMod([1], 5, 2)
        
        self.assertEqual(expect, x.mod())
    
    def testIsPrime31(self):
        aks = Aks()
        self.assertTrue(aks.isPrime(31))
    
    def testIsPrimeBefore100(self):
        aks = Aks()
        primes = []
        for i in range(2, 100):
            if aks.isPrime(i):
                primes.append(i)
        
        expect = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(expect, primes)
    
    
    
    



if __name__ == '__main__':
    unittest.main()