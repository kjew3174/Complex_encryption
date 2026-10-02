# crypto/utils.py
from typing import List
import math

__all__ = ["round_complex"]

def round_complex(z: tuple[float, float]) -> tuple[int, int]:
    """실수부와 허수부를 버림하여 복소수 반환"""
    return (math.floor(z[0]), math.floor(z[1]))
