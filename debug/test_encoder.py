# tests/test_encoder.py

import sys
import os

# 현재 파일 기준 프로젝트 루트 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from crypto.encoder import split_to_complex_blocks, encode_to_base_z, encode_blocks
from crypto.utils import round_complex
from crypto.key_generator import generate_random_complex_base

def test_split_to_complex_blocks():
    data = b"AB"  # 2바이트 예시
    blocks = split_to_complex_blocks(data)
    print("원본 바이트:", list(data))
    print("복소수 블록:", blocks)
    assert all(isinstance(b, complex) for b in blocks), "블록이 복소수가 아님"

def test_encode_to_base_z():
    z = complex(10, 5)
    base = complex(2, 1)
    digits = encode_to_base_z(z, base)  # 이제 [[실수부, 허수부], ...] 반환
    print(f"복소수 {z}를 진법 {base}로 변환한 결과:", digits)
    assert isinstance(digits, list) and all(isinstance(d, list) and len(d) == 2 for d in digits), \
        "결과가 [[실수부, 허수부], ...] 구조가 아님"

def test_encode_blocks():
    data = b"AB"
    blocks = split_to_complex_blocks(data)
    base = generate_random_complex_base()
    encoded = encode_blocks(blocks, base)  # [[실수부, 허수부], ...] 형태
    print(f"랜덤 진법 {base}로 블록 인코딩 결과:", encoded)
    assert all(isinstance(row, list) and all(isinstance(d, list) and len(d) == 2 for d in row) for row in encoded), \
        "인코딩 결과 구조가 올바르지 않음"

if __name__ == "__main__":
    print("==== test_split_to_complex_blocks ====")
    test_split_to_complex_blocks()
    print("\n==== test_encode_to_base_z ====")
    test_encode_to_base_z()
    print("\n==== test_encode_blocks ====")
    test_encode_blocks()
    print("\n모든 테스트 완료!")
