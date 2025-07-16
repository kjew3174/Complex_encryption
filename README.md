🔹 main.py
역할:
프로그램 실행 진입점

키 생성 → 파일 읽기 → 암호화/복호화 → 파일 저장 흐름 제어

주요 함수:
python
복사
편집
def main():
    ...
이름	설명
main()	암호화 전체 과정을 단계별로 실행함

🔹 crypto/encoder.py
역할:
데이터를 복소수로 구성하고 복소수 진법으로 인코딩함

함수:
1. split_to_complex_blocks(data: bytes) -> list[complex]
바이트 데이터를 두 4비트로 나눠 a + bi 형태로 변환

2. encode_to_base_z(z: complex, base: complex) -> list[int]
하나의 복소수를 base 진법으로 표현 (자리수 리스트)

3. encode_blocks(blocks: list[complex], base: complex) -> list[list[int]]
복수의 복소수 블록들을 모두 진법 변환

🔹 crypto/decoder.py
역할:
복소수 진법 자릿수 표현 → 복소수 → 바이트로 복원

함수:
1. decode_from_base_z(digits: list[int], base: complex) -> complex
복소수 진법 자릿수 리스트를 복소수로 복원

2. merge_blocks_to_bytes(blocks: list[complex]) -> bytes
a + bi 복소수를 바이트(8비트)로 다시 합쳐 원래 데이터 복원

3. decode_all(encoded_data: list[list[int]], base: complex) -> bytes
전체 인코딩된 데이터 복호화

🔹 crypto/utils.py
역할:
수학적 유틸 함수들 정의

함수:
1. get_num_digits(z: complex, base: complex) -> int
해당 복소수를 주어진 base로 표현할 때 자릿수 개수 계산

2. round_complex(z: complex) -> complex
실수/허수부를 반올림하여 오차 줄임

🔹 io/file_reader.py
역할:
원본 파일을 바이트 데이터로 읽음

함수:
1. read_binary_file(path: str) -> bytes
이진 파일 읽기

2. read_text_file(path: str, encoding: str = 'utf-8') -> bytes
텍스트 파일을 바이트로 인코딩하여 읽기

🔹 io/file_writer.py
역할:
암호화된 데이터를 저장

함수:
1. write_encrypted_file(path: str, data: list[list[int]]) -> None
암호화된 복소수 진법 데이터 저장 (예: JSON 형식 등)

2. write_decrypted_file(path: str, data: bytes) -> None
복호화한 결과를 바이너리로 저장

🔹 keys/key_generator.py
역할:
암호화 키(복소수 밑) 생성 및 설정

함수:
1. generate_random_complex_base() -> complex
랜덤한 a + bi 형태의 진법 밑 생성

2. parse_base_from_string(s: str) -> complex
문자열 입력 ("2+3i")을 복소수로 해석

3. validate_base(base: complex) -> bool
진법 밑으로 사용 가능한 복소수인지 검증

🔹 tests/test_encoder.py
역할:
암호화·복호화 과정 테스트
