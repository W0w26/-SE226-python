result = 0


def calculate_sum():

    global result
    n = int(input("Enter a value for n: "))
    k = int(input("Enter a value for k: "))
    if k == 0:
        result += n
    else:
        result += ((-1) ** (k + 1)) * (n ** k / k)
        calculate_sum()


calculate_sum()
print(f"Result: {result:.2f}")
