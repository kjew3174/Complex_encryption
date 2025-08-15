import random

def generate_random_complex_base() -> complex:
    """랜덤한 a + bi 형태의 복소수 진법 밑 생성"""
    a = random.uniform(1, 10)   # 실수부 (1~10 범위)
    b = random.uniform(1, 10)   # 허수부 (1~10 범위)
    return complex(round(a, 2), round(b, 2))

def parse_base_from_string(s: str) -> complex:
    """문자열("2+3i") → 복소수로 변환"""
    s = s.replace("i", "j") 
    try:
        return complex(s)
    except ValueError:
        raise ValueError("잘못된 복소수 문자열 형식입니다.")

def validate_base(base: complex) -> bool:
    """진법 밑으로 사용 가능한지 검증 (0이 아니고, 1도 아님)"""
    if base == 0 or base == 1:
        return False
    return True

# 실행 예시
if __name__ == "__main__":
    base = generate_random_complex_base()
    print("랜덤 키:", base)
    print("유효성 검사:", validate_base(base))
