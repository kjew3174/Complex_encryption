# crypto/encoder.py
from typing import List
from .utils import round_complex

__all__ = ["split_to_complex_blocks", "encode_blocks"]

def split_to_complex_blocks(data: bytes) -> List[complex]:
    """바이트를 4비트 단위로 나누어 복소수 블록 생성"""
    blocks = []
    for b in data:
        high = (b >> 4) & 0xF
        low = b & 0xF
        blocks.append(complex(high, low))
    return blocks

def encode_blocks(blocks: List[complex], base: complex) -> List[complex]:
    """복소수 블록을 복소수 진법으로 암호화"""
    encoded = []
    for block in blocks:
        encoded.append(round_complex(block * base))
    return encoded
