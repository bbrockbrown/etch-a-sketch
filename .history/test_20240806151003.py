def kthFactor(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    factors = []
    temp = k
    for i in range(1, n+1):

        if n % i == 0:
            factors.append(i)
            k -= 1
        
        if k == 0:
            return i
    
    if temp <= len(factors):
        return factors[temp-1]
    else:
        return -1
    
print(kthFactor(4, 4))