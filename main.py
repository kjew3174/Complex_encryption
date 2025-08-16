# main.py
import crypto.encoder as encoder
import crypto.decoder as decoder
import io_utils
from crypto.key_generator import generate_random_complex_base

def main():
    file_path = "test.txt"
    decrypted_path = "decrypted.txt"
    encrypted_path = "encrypted.json"

    # 원본 읽기
    data = io_utils.read_text_file(file_path)
    print("원본 바이트:", list(data))

    # 복소수 블록 생성
    blocks = encoder.split_to_complex_blocks(data)

    # 랜덤 키 생성
    base = generate_random_complex_base()
    print("사용 키:", base)

    # 암호화
    encoded_data = encoder.encode_blocks(blocks, base)
    io_utils.write_encrypted_file(encrypted_path, encoded_data)
    print("암호화 저장 완료:", encrypted_path)

    # 복호화
    loaded_encoded = io_utils.read_encrypted_file(encrypted_path)
    decrypted_data = decoder.decode_all(loaded_encoded, base)
    io_utils.write_text_file(decrypted_path, decrypted_data)
    print("복호화 결과 저장 완료:", decrypted_path)

    # 검증
    if data == decrypted_data:
        print("복호화 성공: 원본과 일치")
    else:
        print("복호화 실패: 원본과 다름")

if __name__ == "__main__":
    main()
