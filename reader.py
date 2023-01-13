from typing import List


class Reader:
    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def get_keys(self) -> List[str]:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = file.read()
            keys: List[str] = reader.split('\n')
            return keys[0:len(keys) - 1]
