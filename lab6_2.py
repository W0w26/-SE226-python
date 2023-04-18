result = 0

def calculate_sum(n, k):
    global result
    if k == 0:
        result += n
    else:
        result += ((-1) ** (k + 1)) * (n ** k / k)
        calculate_sum(n, k - 1)


calculate_sum(2, 5)
print(f"Result: {result:.2f}")
