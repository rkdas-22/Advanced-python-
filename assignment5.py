def lcs(s1, s2):

    m = len(s1)
    n = len(s2)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    ans = ""

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans = s1[i - 1] + ans
            i = i - 1
            j = j - 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i = i - 1
        else:
            j = j - 1

    return ans, dp[m][n]


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result, length = lcs(string1, string2)

print("\nLongest Common Subsequence:", result)
print("Length of LCS:", length)