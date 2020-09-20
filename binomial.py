import math

def prob(n, p, N):
    fact = lambda f: 1 if f == 0 else f * fact(f - 1)
    nCk = fact(N) / (fact(n) * fact(N - n))
    result = nCk * pow(p, n) * pow(1 - p, N - n)
    return result

def infoMeasure(n, p, N):
    pr = prob(n, p, N)
    result = - math.log(pr, 2)
    return result

def sumProb(N, p):
    
    sum = 0
    for i in range(1, N):
        sum += prob(i, p, N)
    return sum
""" Gọi hàm sumProb(100, 0.2) ta được kết quả là 0.9999999997963016 ~ 1
        Gọi hàm sumProb(500, 0.4) ta được kết quả là 0.9999999999999999 ~ 1
        Vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binamial bằng 1 """

def approxEntropy(N, p):
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy

""" Entropy của nguồn binomial với N=50, p=0.5 là 3.868973533024591
    Entropy của nguồn binomial với N=400, p=0.5 là 5.36902292487739 """
