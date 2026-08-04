# Memoization

def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Tabulation

def fibonacci_table(n):
    table = [0] * (n + 1)

    if n >= 1:
        table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]


# Main Program

n = int(input("Enter the value of n: "))

print("Using Memoization:", fibonacci_memo(n))
print("Using Tabulation:", fibonacci_table(n))

#output
# Enter the value of n: 10
# Using Memoization: 55
# Using Tabulation: 55