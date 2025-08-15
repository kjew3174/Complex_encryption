import json

def write_encrypted_file(path: str, data: list[list[int]]) -> None:
    """암호화된 데이터를 JSON 형식으로 저장"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def write_decrypted_file(path: str, data: bytes) -> None:
    """복호화된 데이터를 바이너리로 저장"""
    with open(path, "wb") as f:
        f.write(data)
