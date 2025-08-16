# crypto/key_generator.py
import random
from typing import Tuple

__all__ = ["generate_random_complex_base"]

def generate_random_complex_base() -> complex:
    """0~15 범위의 실수부, 허수부를 가진 복소수 진법 키 생성"""
    real = random.randint(1, 15)
    imag = random.randint(1, 15)
    return complex(real, imag)
