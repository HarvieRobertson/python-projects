
def sales_prediction(sales):
    profit= sales*0.23
    print(f"Expected profit: ", profit)
sales = int(input("Enter projected sales: "))
sales_prediction(sales)


def cost_calc():
    distance= float(input("Enter journey distance(miles): "))
    mpg = float(input("Enter your cars MPG: "))
    fuel = float(input("Enter the fuel price per litre: "))
    mpl = mpg / 4.546
    fuel_needed = distance / mpl
    fuel_price = fuel_needed * fuel
    fuel_price = round(fuel_price,2)
    print(f"Estimated fuel cost: ", fuel_price)
cost_calc()

a = int(input("First Num: "))
b = int(input("Second Num: "))
c = int(input("Third Num: "))
def calc_area(a, b, c):
    s = (a + b + c) / 2
    Area = (s*((s - a)*(s - b)*(s - c))) ** 0.5
    print(f"Area: " , Area)
calc_area(a, b, c)

temperatures = [12, 15, 18, 21, 19, 16, 14, 11]
def calculate_average(temperatures):
    total = 0
    for i in temperatures:
        total += i
    average = total / len(temperatures) 
    return average
print(calculate_average(temperatures))

def find_highest(temperatures):
    highest_temp = 0
    for i in temperatures:
        if i > highest_temp:
            highest_temp = i
    return highest_temp
print(find_highest(temperatures))

def find_lowest(temperatures):
    lowest_temp = 1000
    for i in temperatures:
        if i < lowest_temp:
            lowest_temp = i
    return lowest_temp
print(find_lowest(temperatures))

def find_hot_days(temperatures):
    hot_days = 0
    for i in temperatures:
        if i > 20:
            hot_days += 1
    return hot_days
print(find_hot_days(temperatures))

numbers = [3, 1, 5, 3, 2, 1]
def unique_sorted(numbers):
    sorted = []
    for i in numbers:
       if i not in sorted:
           sorted.append(i)
    sorted.sort(reverse = True)
    return sorted
print(unique_sorted(numbers))

dup = [1, 2, 3, 1] 
def contains_duplicate(dup):
    count = 0
    for i in dup:
        count = 0
        for j in dup:
            if i == j:
                count += 1
        if count > 1:
            return True
            break
        elif count == 1:
            return False
            continue
print (contains_duplicate(dup))

list1 = [1, 2, 45]
list2 = [3, 5, 5]
def max_difference(list1, list2):
    max1 = max(list1)
    max2 = max(list2)
    min1 = min(list1)
    min2 = min(list2)
    bigger_max = max(max1, max2)
    if bigger_max == max1:
        smaller_min = min2
    else:
        smaller_min = min1
    difference = bigger_max - smaller_min
    return difference
print(max_difference(list1, list2))