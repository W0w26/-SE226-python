def calculate_sum(n, k):
    if k == 0:
        return n
    else:
        return ((-1)^(k+1)) * (n^k / k) + calculate_sum(n, k-1)

n = int(input("Enter a value for n: "))
k = int(input("Enter a value for k: "))
result = calculate_sum(n, k)
print(f"Result: {result:.2f}")