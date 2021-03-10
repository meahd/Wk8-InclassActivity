import unittest
import fibonacci


class TestCase(unittest.TestCase):
    def testNIs0(self):
        self.assertEqual(fibonacci.Fibonacci(0),0)
    def testNIs1(self):
        self.assertEqual(fibonacci.Fibonacci(1),1)
    def testNIs2(self):
        self.assertEqual(fibonacci.Fibonacci(2),1)
    def testFindNthFib(self):
        self.assertEqual(fibonacci.Fibonacci(9),34)
    
        
if __name__ == '__main__':
    unittest.main()