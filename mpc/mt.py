import numpy as np

# シェアを生成
def make_share(a):
    if type(a) is np.ndarray:
        # 配列の最大値を求める
        m_a = np.max(a)
        # 各シェアを求める
        share_num1 = np.random.randint(-10 * m_a, 10 * m_a, a.shape)
        share_num2 = np.random.randint(-10 * m_a, 10 * m_a, a.shape)
        share_num3 = a - share_num1 - share_num2
        return share_num1, share_num2, share_num3
    elif type(a) is int:
        share_num1 = np.random.randint(-1000000,1000000)
        share_num2 = np.random.randint(-1000000,1000000)
        share_num3 = a - share_num1 - share_num2
        return share_num1, share_num2, share_num3

# multiplication triplesのa,b,cを作成
def make_abc():
    a = np.random.randint(1,10000)
    b = np.random.randint(1,10000)
    c = a * b
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    # a,b,cのシェアを作成
    a1, a2, a3 = make_share(a)
    b1, b2, b3 = make_share(b)
    c1, c2, c3 = make_share(c)
    # できたシェアを各パーティに配る
    s1 = (a1, b1, c1)
    s2 = (a2, b2, c2)
    s3 = (a3, b3, c3)
    print("s1 = ", s1)
    print("s2 = ", s2)
    print("s3 = ", s3)
    return s1, s2, s3

def share_de(s, abc):
    x, y = s
    a, b, _ = abc
    d = x - a
    e = y - b
    return d, e

def times(abc, d, e):
    a, b, c = abc
    z = e * a + d * b + c + d * e
    return z

def times2(abc, d, e):
    a, b, c = abc
    z = e * a + d * b + c
    return z

# multiplication triplesの計算を行う
def mts(s1, s2, s3, s1_abc, s2_abc, s3_abc):
    # d,eのシェアを作成
    d1, e1 = share_de(s1, s1_abc)
    d2, e2 = share_de(s2, s2_abc)
    d3, e3 = share_de(s3, s3_abc)
    # d,eを復元（ここで通信が必要）
    d = d1 + d2 + d3
    e = e1 + e2 + e3
    print("d = ", d)
    print("e = ", e)
    # ローカルに計算するところ[z]
    z1 = times(s1_abc, d, e)
    z2 = times2(s2_abc, d, e)
    z3 = times2(s3_abc, d, e)
    print("z1 = ", z1)
    print("z2 = ", z2)
    print("z3 = ", z3)
    # シェアを合わせてzを復元（通信が必要）
    z = z1 + z2 + z3
    return z