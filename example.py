import random

def enc(n, k):
    return complex(n) * k

def dec(c, k):
    return int((c / k).real)

# 사용자 입력
n = int(input("숫자를 입력하세요: "))

# 랜덤 복소수 키 생성 (실수와 허수가 1~10 사이)
k = complex(random.randint(1, 10), random.randint(1, 10))
print("암호화 키:", k)

# 암호화
c = enc(n, k)
print("암호화된 값:", c)

# 복호화
r = dec(c, k)
print("복호화된 값:", r)
