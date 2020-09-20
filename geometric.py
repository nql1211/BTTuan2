import math

def prob(n, p):
    result = p * pow((1 - p), n - 1)
    return result

def infoMeasure(n, p):
    pr = prob(n, p)
    result = - math.log(pr, 2)
    return result

def sumProb(N, p):
    sum = 0
    for i in range(1, N):
        sum += prob(i, p)
    return sum
""" Gọi hàm sumProb(100, 0.2) ta được kết quả là 0.9999999997453705 ~ 1
        Gọi hàm sumProb(1000, 0.2) ta được kết quả là 0.9999999999999998 ~ 1
        Vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố geometric bằng 1 """

def approxEntropy(N, p):
    
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p) * infoMeasure(i, p)
    return entropy
""" Entropy của nguồn geometric với N=50, p=0.5 là 1.9999999999999094 ~ 2
    Entropy của nguồn geometric với N=500, p=0.5 là 1.9999999999999998 ~ 2 """
