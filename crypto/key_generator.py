# crypto/key_generator.py
import random
import math

__all__ = ["generate_random_complex_base"]

def generate_random_complex_base() -> tuple[int, int]:
    """0~15 범위의 실수부, 허수부를 가진 복소수 진법 키 생성"""
    real = 2
    imag = 2
    while not bool(math.gcd(real, imag) == 1 and (real**2 + imag**2 > 1)):
        real = random.randint(-15, 15)
        imag = 1 if random.randint(0, 1) == 0 else -1
    return (real, imag)
