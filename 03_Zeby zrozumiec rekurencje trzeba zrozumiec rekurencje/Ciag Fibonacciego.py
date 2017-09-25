'''Oblicz n-tą liczbę ciągu fibonacciego (n – podane jako parametr)'''

def fibonacciNumber(n):
      if n == 0:
            return 0
            
      elif n == 1:
            return 1
            
      while n > 1:
            solution = fibonacciNumber(n-1) + fibonacciNumber(n-2)
            return solution

            
            
print (fibonacciNumber(19))
                  

            
