

class PolyMod:

    def __init__(self, coeffs, n, r):
        self.coeffs = coeffs
        self.n = n
        self.r = r

        self.__fit()
    
    def __fit(self):
        for i in range(len(self.coeffs)):
            self.coeffs[i] %= self.n

        i = len(self.coeffs) - 1
        while (i > 0 and self.coeffs[i] == 0):
            i -= 1
    
        self.coeffs = self.coeffs[:i + 1]
    
    def __eq__(self, other):
        return self.coeffs == other.coeffs
    
    def __add__(self, other):
        if len(self.coeffs) >= len(other.coeffs):
            x = self.coeffs
            y = other.coeffs + [0] * (len(self.coeffs) - len(other.coeffs))
        else:
            x = self.coeffs + [0] * (len(other.coeffs) - len(self.coeffs))
            y = other.coeffs
        
        z = []
        for i in range(len(x)):
            z.append((x[i] + y[i]) % self.n)
        
        return PolyMod(z, self.n, self.r)
    
    def __mul__(self, other):
        lenX = len(self.coeffs)
        lenY = len(other.coeffs)
        length = lenX + lenY - 1
        z = [0] * length
        for i in range(0, lenX):
            for j in range(0, lenY):
                z[i + j] = (z[i + j] + self.coeffs[i] * other.coeffs[j]) % self.n
        return PolyMod(z, self.n, self.r).mod()

    def __pow__(self, m):
        c = PolyMod(self.coeffs, self.n, self.r)
        s = PolyMod([1], self.n, self.r)
        while (m > 0):
            if (m % 2 == 1):
                s = s * c
            m = m >> 1
            c = c * c
        return s

    def mod(self):
        m = self.r
        for i in range(len(self.coeffs) - 1, m - 1, -1):
            self.coeffs[i - m] = (self.coeffs[i - m] + self.coeffs[i]) % self.n
            self.coeffs[i] = 0
        return PolyMod(self.coeffs, self.n, self.r)
 
    def __str__(self):
        s = []
        for i in range(len(self.coeffs)):
            if not self.coeffs[i] == 0:
                s.append(str(self.coeffs[i]) + '*x^' + str(i))
        
        s.reverse()
        return '+'.join(s) + "\n"
