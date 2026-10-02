# crypto/decoder.py
from typing import List

__all__ = ["decode_blocks", "merge_blocks_to_bytes"]

def decode_blocks(encoded_blocks: list[list[int]], base: tuple[int, int]) -> list[tuple[int, int]]:
    """복소수 진법 블록을 원래 복소수 블록으로 변환"""
    a, b = base[0], base[1]

    Norm: int = a**2 + b**2
    D: dict[int, tuple[int, int]] = {}
    i = 0
    limit = (abs(a) + abs(b) + 1) // 2
    for x in range(-limit, limit+1):
        for y in range(-limit, limit+1):
            if -Norm <= 2 * (a*x + b*y) < Norm and -Norm <= 2 * (a*y - b*x) < Norm:
                D[i] = (x, y)
                i += 1
    if len(D) != Norm:
        raise ValueError("D의 크기가 Norm과 일치하지 않음: len(D)={}, Norm={}".format(len(D), Norm))


    decoded_blocks: list[tuple[int, int]] = []
    for encoded_block in encoded_blocks:
        z = 0 + 0j
        encoded_block.reverse()
        for posit, digit in enumerate(encoded_block):
            # z = q * base + r
            # z = d_0 * base^0 + d_1 * base^1 + ... + d_n * base^n
            x, y = D[digit]
            z += complex(x, y) * (complex(a, b) ** posit)
        decoded_blocks.append((int(z.real), int(z.imag)))
    return decoded_blocks

def merge_blocks_to_bytes(blocks: List[tuple[int, int]]) -> bytes:
    """복소수 블록을 바이트 단위로 변환"""
    data: list[int] = []
    for block in blocks:
        high = block[0] & 0xF
        low = block[1] & 0xF
        data.append((high << 4) | low)
    return bytes(data)

