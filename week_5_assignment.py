"""
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
"""
temperatures = [12, 15, 18, 21, 19, 16, 14, 11]
def calculate_average(temperatures):
    total = 0
    for i in temperatures:
        total = total + i
    average = total / len(temperatures) 
    return average
print(calculate_average(temperatures))