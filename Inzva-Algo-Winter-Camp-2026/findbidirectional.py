total = 0
    for i in range(0, k-1):
        total += (i+1) * inputs[i]
    for i in range(n-k+1, n):
        total += (n-i) * inputs[i]
    total += prefixSum[n-k] - prefixSum[k-1]
    if total >= c:
        print(k)
        break