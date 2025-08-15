
from typing import List
from .utils import get_num_digits, round_complex

# 1byte를 복소수로 변환
def split_to_complex_blocks(data: bytes) -> List[complex]:

    blocks = []
    for byte in data:
        high = (byte >> 4) & 0xF  # 상위 4비트
        low = byte & 0xF          # 하위 4비트
        blocks.append(complex(high, low))
    return blocks

# 복소수 진법으로 변환 (역순: LSD → MSD)
def encode_to_base_z(z: complex, base: complex) -> List[int]:

    if base == 0:
        raise ValueError("진법의 밑(base)은 0일 수 없습니다.")

    digits = []
    value = z
    while value != 0:
        # 정수 나눗셈 유사 처리
        remainder = complex(round(value.real) % abs(int(base.real)), 0)  # 임시 단순화
        digits.append(int(remainder.real))
        value = (value - remainder) / base
        value = round_complex(value, 10)  # 누적 오차 방지
    return digits if digits else [0]

# 복소수 블록들을 복소수 진법으로 변환
def encode_blocks(blocks: List[complex], base: complex) -> List[List[int]]:

    encoded_data = []
    for block in blocks:
        encoded_data.append(encode_to_base_z(block, base))
    return encoded_data
