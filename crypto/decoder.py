# crypto/decoder.py
from typing import List
from .utils import round_complex

__all__ = ["decode_from_base_z", "decode_all", "merge_blocks_to_bytes"]

def decode_from_base_z(encoded_block: complex, base: complex) -> complex:
    """복소수 진법 블록을 원래 복소수 블록으로 변환"""
    return round_complex(encoded_block / base)

def merge_blocks_to_bytes(blocks: List[complex]) -> bytes:
    """복소수 블록을 바이트 단위로 변환"""
    data = []
    for block in blocks:
        high = int(block.real) & 0xF
        low = int(block.imag) & 0xF
        data.append((high << 4) | low)
    return bytes(data)

def decode_all(encoded_data: List[complex], base: complex) -> bytes:
    """전체 암호화 데이터 복원"""
    blocks = [decode_from_base_z(b, base) for b in encoded_data]
    return merge_blocks_to_bytes(blocks)
