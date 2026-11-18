n = 7
def fibonacci_iterative(n):
    total = 0
    prev = 0
    for i in range(n-1):
        if i == 0:
            total = 1
        else:
            total = prev + total
            prev = total - prev
    return total

def fibonacci_recursive(n):
   n= n-1
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
print(fibonacci_recursive(n))
