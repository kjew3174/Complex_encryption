def read_binary_file(path: str) -> bytes:
    """이진 파일 읽기"""
    with open(path, "rb") as f:
        return f.read()

def read_text_file(path: str, encoding: str = 'utf-8') -> bytes:
    """텍스트 파일 읽어서 바이트로 변환"""
    with open(path, "r", encoding=encoding) as f:
        text = f.read()
    return text.encode(encoding)
