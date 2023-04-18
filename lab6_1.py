from math import factorial

n = int(input("Enter a value for n: "))
x = int(input("Enter a value for x: "))

sum_list = [n**i/factorial(i) for i in range(x+1)]
result = sum(sum_list)

print(f"Result: {result:.2f}")