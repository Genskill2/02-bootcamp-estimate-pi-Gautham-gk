import math
import unittest
import random
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")



def wallis(n):
    pival=1
    for i in range(1,n+1):
        pival*=(4*i*i)/(4*i*i-1)
    pival*=2
    print(pival)
    return pival


def monte_carlo(num):
    total=0
    inside=0
    for j in range(num):
        x=random.random()
        y=random.random()
        dist=(x**2+y**2)**0.5
        if dist<1:
            inside+=1
        total+=1
    print(inside,total)
    pival=4*inside/total
    print(pival)
    return pival

    
if __name__ == "__main__":
    unittest.main()
