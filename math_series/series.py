def fibonacci(n):
    if n<= 0:
        return("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def lucas(n) :
    a = 2
    b = 1
    if (n == 0) :
        return a
  
    
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
     
    return b
     
def sum_series(n, n1, n2):
    if type(n) != int:
        return ("invalid Input")
    elif n < 0:
        return ("invalid Negative Value")
    elif n == 0:
       return n1
    elif n == 1:
       return n2
    else:
       return (sum_series(n-1, n1, n2) + sum_series(n-2, n1, n2))
