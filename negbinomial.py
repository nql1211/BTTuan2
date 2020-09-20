import math

def prob(n, p, r):
    fact = lambda f:1 if f==0 else f*fact(f-1)
    nCk = fact(n-1) / (fact(r-1) * fact(n-r))
    result = nCk * pow(p, r) * pow(1 - p, n - r)
    return result

def infoMeasure(n, p, r):
    pr = prob(n, p, r)
    result = - math.log(pr, 2)
    return result

def sumProb(N, p, r):
    sum = 0
    for i in range(r, N):
        sum += prob(i, p, r)
    return sum
""" Gọi hàm sumProb(100, 0.5, 2) ta được kết quả là 0.9999938852188545 ~ 1
    Gọi hàm sumProb(500, 0.5, 2) ta được kết quả là 0.9999999999999991 ~ 1
    Vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố negative binomial bằng 1 """
def approxEntropy(N, p, r):
    entropy = 0
    for i in range(r, N):
        entropy += prob(i, p, r) * infoMeasure(i, p, r)
    return entropy
""" Entropy của nguồn negative binomial với N=50, p=0.5, r=3 là 3.11564779622215
    Entropy của nguồn negative binomial với N=400, p=0.5, r=3 là 3.1156477963110514 """
print(sumProb(50, 0.3, 3))
print(sumProb(500, 0.3, 3))
print(approxEntropy(50, 0.5, 3))
print(approxEntropy(400, 0.5, 3))