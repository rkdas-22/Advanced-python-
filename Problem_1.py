# Fibonacci using Memoization (Top-Down DP)

memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Main Program
N = int(input("Enter the value of N: "))

print("First", N, "Fibonacci numbers are:")
for i in range(N):
    print(fibonacci(i), end=" ")