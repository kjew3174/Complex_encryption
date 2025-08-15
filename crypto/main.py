from keys.key_generator import generate_random_complex_base, validate_base
from io.file_reader import read_binary_file
from io.file_writer import write_encrypted_file

def main():
   
    base = generate_random_complex_base()
    if not validate_base(base):
        print("생성된 키가 유효하지 않습니다.")
        return
    print(f"생성된 복소수 진법 밑: {base}")

    # 예시: 파일 읽
    original_data = read_binary_file("sample.bin")
    print(f"원본 데이터 크기: {len(original_data)} 바이트")

    
    fake_encrypted_data = [[1, 2, 3], [4, 5, 6]] 
    write_encrypted_file("encrypted.json", fake_encrypted_data)
    print("암호화된 데이터 저장 완료: encrypted.json")

if __name__ == "__main__":
    main()
