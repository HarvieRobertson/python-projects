n = 7
def fibonacci_iterative(n):
    total = 0
    prev = 0
    for i in range(n):
        if i == 0:
            total = 0
        else:
            total = prev + total
            prev = total - prev
    return total