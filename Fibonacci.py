n = int(input("Enter n: "))

if n <= 1:
    print("Fibonacci number:", n)
else:
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    print("Fibonacci number:", b)
