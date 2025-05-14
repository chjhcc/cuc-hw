# 第二章 古典密码-作业

## 1. 用维吉尼亚密码加密明文“Communication University of China”，其中使用的密钥为“computer”,试求其密文。

computer|compu ter|compute r|c omput
Communic|ation Uni|versity o|f China
所以密文为：Ecybogmtchudh Nrzxsdhcmc fh Qtxht

## 2.明文friday”用m=2的Hill密码加密后得到密文“WJNYQY”，求Hill密码的密钥。

明文"friday"可以表示为：f=5, r=17, i=8, d=3, a=0, y=24。密文"WJNYQY"可以表示为：W=22, J=9, N=13, Y=24, Q=16, Y=24。
设m=2构成的矩阵为(a b
                 c d)
明文行列式为(5,17)
则有(5a+17c,5b+17d)=(22,9)(mod26)
    (8a+3c,8b+3d)=(13,24)(mod26)
    (24c,24d)=(16,3)(mod26)
可得
24c=16+26k
24d=3+26k(k=0,1,2...)
由上式可得c=5,d=13
可据此值求出a=3,b=16
所以密钥为(3 16
          5 13)