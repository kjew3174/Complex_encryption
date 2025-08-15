
from typing import List
from .utils import round_complex

# 복소수 진법을 10진법으로 변환
def decode_from_base_z(digits: List[int], base: complex) -> complex:

    value = 0 + 0j
    power = 1 + 0j
    for digit in digits:
        value += digit * power
        power *= base
    return round_complex(value, 10)

# 복소수 블록들을 바이트로 복원
def merge_blocks_to_bytes(blocks: List[complex]) -> bytes:

    byte_array = bytearray()
    for block in blocks:
        high = int(round(block.real)) & 0xF
        low = int(round(block.imag)) & 0xF
        byte_array.append((high << 4) | low)
    return bytes(byte_array)

# 전체 암호화 데이터 복원
def decode_all(encoded_data: List[List[int]], base: complex) -> bytes:

    blocks = []
    for digits in encoded_data:
        z = decode_from_base_z(digits, base)
        blocks.append(z)
    return merge_blocks_to_bytes(blocks)