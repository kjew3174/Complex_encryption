
import math
from typing import Union

Number = Union[int, float, complex]

# 복소수 진법의 자릿수 계산
def get_num_digits(z: complex, base: complex) -> int:

    if z == 0:
        return 1

    # 복소수 진법의 자릿수 계산 시 절댓값을 사용
    magnitude = abs(z)
    base_magnitude = abs(base)

    # base가 0이나 1이면 무한 자릿수이므로 예외 처리
    if base_magnitude <= 1:
        raise ValueError("진법의 밑 절댓값은 1보다 커야 합니다.")

    return math.floor(math.log(magnitude, base_magnitude)) + 1

# 복소수의 실수부와 허수부를 지정한 소수점 자리수까지 반올림
def round_complex(z: complex, digits: int = 6) -> complex:

    return complex(round(z.real, digits), round(z.imag, digits))

# 0으로 나눔 방지
def safe_divide(a: Number, b: Number) -> Number:

    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b
