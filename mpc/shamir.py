import random

# 有限体上の多項式の係数を生成する
def generate_random_polynomial(secret, threshold, prime):
    coefficients = [secret] + [random.randint(1, prime - 1) for _ in range(threshold - 1)]
    # print(coefficients)
    return coefficients

# 多項式を評価する
def evaluate_polynomial(coefficients, x, prime):
    result = 0
    count = 0
    for coefficient in coefficients:
        result = (coefficient * (x ** count) + result) % prime
        count += 1
    return result

# 秘密をシェアに分割する
def generate_shares(secret, threshold, num_shares, prime):
    if threshold > num_shares:
        raise ValueError("しきい値はシェアの数以下である必要があります")

    coefficients = generate_random_polynomial(secret, threshold, prime)
    shares = [(x, evaluate_polynomial(coefficients, x, prime)) for x in range(1, num_shares + 1)]
    
    return shares

# シェアから和を計算
def plus(shares1, shares2, num_shares, prime):
    # shares = [(x, shares1[x - 1] + shares2[x - 1]) for x in range(1, num_shares + 1)]
    shares = []
    for x in range(1, num_shares + 1):
        _, y1 = shares1[x - 1]
        _, y2 = shares2[x - 1]
        y = (y1 + y2) % prime
        shares = shares + [(x, y)]
    return shares

# シェアから秘密を再構築する
def interpolate(shares, prime):
    secret = 0
    for i in range(len(shares)):
        xi, yi = shares[i]
        term = yi
        for j in range(len(shares)):
            if i == j:
                continue
            xj, _ = shares[j]
            term = (term * (0 - xj)) % prime
            term = (term * pow(xi - xj, -1, prime)) % prime
        secret = (secret + term) % prime
    return secret