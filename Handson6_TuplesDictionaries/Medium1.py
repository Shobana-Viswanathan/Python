def large(t, n):
    if n == 1:
        return t[0]
    return max(t[n-1], large(t, n-1))

t = tuple(map(int, input("Enter tuple elements: ").split()))

print(large(t, len(t)))