import cv2
import numpy as np
import mpc.mt as mt
import mpc.additive as ad
import mpc.shamir as sh

def main():
    while True:
        print("シェアの作り方を選んでください")
        print("加法的秘密分散：a  shamirの秘密分散：s")
        switch = input()
        if switch == 'a':
            # 加法的秘密分散
            print("１つ目の秘密情報")
            a = input()
            print("２つ目の秘密情報")
            b = input()
            s1, s2, s3 = ad.secret(int(a),int(b))
            print("s1 = ", s1)
            print("s2 = ", s2)
            print("s3 = ", s3)
            # 和
            s = ad.add(s1, s2, s3)
            print("add secret : ", s)
            # 積
            s1_abc, s2_abc, s3_abc = mt.make_abc()
            s = mt.mts(s1, s2, s3, s1_abc, s2_abc, s3_abc)
            print("times secret : ", s)
            break
        elif switch == 's':
            # shamirの秘密分散
            print("１つ目の秘密情報")
            a = int(input())
            print("２つ目の秘密情報")
            b = int(input())
            print("参加する人数")
            num_shares = int(input())   # 生成するシェアの総数
            print("復元に必要な人数")
            threshold = int(input())    # 秘密を再構築するために必要なシェアの最小数
            prime = 104729                 # 通常は大きな素数を選びます
            shares1 = sh.generate_shares(a, threshold, num_shares, prime)
            print("生成されたシェア1:", shares1)
            shares2 = sh.generate_shares(b, threshold, num_shares, prime)
            print("生成されたシェア2:", shares2)
            # 和
            shares = sh.plus(shares1, shares2, num_shares, prime)
            # シェアから秘密を再構築
            s = sh.interpolate(shares, prime)
            print("add secret : ", s)
            # 
            print("times secret : ", s)
            
            break
        else:
            print("入力が正しくありません")
