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
