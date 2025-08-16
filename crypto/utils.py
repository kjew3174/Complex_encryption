# crypto/utils.py
from typing import List

__all__ = ["round_complex"]

def round_complex(z: complex) -> complex:
    """실수부와 허수부를 반올림하여 복소수 반환"""
    return complex(round(z.real), round(z.imag))
