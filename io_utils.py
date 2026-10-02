# io_utils.py
from typing import List
import json

__all__ = [
    "read_text_file",
    "write_text_file",
    "write_encrypted_file",
    "read_encrypted_file"
]

def read_text_file(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()

def write_text_file(path: str, data: bytes):
    with open(path, "wb") as f:
        f.write(data)

def write_encrypted_file(path: str, encoded_data: list[list[int]]):
    """복소수 블록을 JSON 형식으로 저장"""
    json_data = encoded_data
    with open(path, "w", encoding="utf-8") as f:
        json.dump(json_data, f)

def read_encrypted_file(path: str) -> list[list[int]]:
    """JSON에서 부호화 블록 불러오기"""
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    return list(json_data)
