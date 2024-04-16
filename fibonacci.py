import unittest
def fibonacci(arg):
	if arg==0:
		return 0
	if arg==1:
		return 1
	#if n in (0,1):
		#return n
	resultado=fibonacci(arg-1)+fibonacci(arg-2)
	return resultado

class TestFibonacci(unittest.TestCase):
    def test_with_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)
    def test_with_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)
    def test_with_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    def test_with_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    def test_with_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)
    def test_with_40(self):
        resultado = fibonacci(14)
        self.assertEqual(resultado, 377)

if __name__== '__main__':
	unittest.main()
