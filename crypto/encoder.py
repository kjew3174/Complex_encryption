# crypto/encoder.py
from typing import List

__all__ = ["split_to_complex_blocks", "encode_blocks"]

def split_to_complex_blocks(data: bytes) -> List[tuple[int, int]]:
    """바이트를 4비트 단위로 나누어 복소수 블록 생성"""
    blocks = []
    for b in data:
        high = (b >> 4) & 0xF
        low = b & 0xF
        blocks.append((high, low))
    return blocks

def nearest_int(n: int, m: int) -> int:
    """분수 반올림 함수"""
    return (2 * n + m) // (2 * m)

def encode_blocks(blocks: List[tuple[int, int]], base: tuple[int, int]) -> List[List[int]]:
    """복소수 블록을 복소수 진법으로 암호화"""
    encoded_blocks: list[list[int]] = []
    a, b = base[0], base[1]
    Norm: int = a**2 + b**2
    D: dict[tuple[int, int], int] = {}
    i = 0
    limit = (abs(a) + abs(b) + 1) // 2
    for x in range(-limit, limit+1):
        for y in range(-limit, limit+1):
            if -Norm <= 2 * (a*x + b*y) < Norm and -Norm <= 2 * (a*y - b*x) < Norm:
                D[(x, y)] = i
                i += 1
    if len(D) != Norm:
        raise ValueError("D의 크기가 Norm과 일치하지 않음: len(D)={}, Norm={}".format(len(D), Norm))

    for block in blocks:
        x, y = block[0], block[1]
        q_x, q_y = 0, 0
        encoded_block: list[int] = []

        visited = set()
        while x != 0 or y != 0:
            state = (x, y)
            if state in visited:
                raise ValueError("무한 루프 발생: 순환 상태 감지")
            visited.add(state)
            q_x, q_y = nearest_int(a*x + b*y, Norm), nearest_int(a*y - b*x, Norm)
            r_x = x - a*q_x + b*q_y
            r_y = y - b*q_x - a*q_y
            x, y = q_x, q_y
            encoded_block.append(D[(r_x, r_y)])
        encoded_block.reverse()
        encoded_blocks.append(encoded_block)
    return encoded_blocks
