x = float(input("Enter the value of x: "))
n = term = num =1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Times ={} and Sum = {}".format(n, result))

#n = 1   term = 1 * x               result = 1.0 + x 
#n = 2   term = x * x / 2           result = 1.0 + x + x * x / 2
#n = 3   term = x * x / 2 * x / 3   result = 1.0 + x + x * x / 2 + (x * x * x / 3 * 2)


