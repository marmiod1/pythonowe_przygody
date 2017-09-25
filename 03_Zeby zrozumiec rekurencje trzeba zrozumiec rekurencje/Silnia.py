n = int(input("Prosze podac liczbe: "))
 
def factorial(n):
    factorial_inter = 1
    if n in (0,1):
        return 1
    else:
        for i in range(2,n+1):
            factorial_inter = factorial_inter * i
        return factorial_inter

print(factorial(n))


 

def factorial_recursion(n):
    if n > 1:
        return n * factorial_recursion(n-1)
    elif n in (0,1):
        return 1
 
 
print (factorial_recursion(n))
