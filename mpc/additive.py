import mt

def secret(a, b):
    # シェアを作成(3人にシェア)
    a1, a2, a3 = mt.make_share(a)
    b1, b2, b3 = mt.make_share(b)
    # print("シェア作成---complete---")
    # 各シェアを分配
    s1 = (a1, b1)
    s2 = (a2, b2)
    s3 = (a3, b3)
    # print("シェアの分配---complete---")
    return s1, s2, s3

def add(a, b, c):
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c
    s = a1 + b1 + c1 + a2 + b2 + c2
    return s