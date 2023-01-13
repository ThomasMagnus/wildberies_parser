import pandas as pd

from typing import List
from parser import Parser


class Table:
    def __init__(self, urls: List):
        self.data: Parser = Parser(urls)
        self.writer = pd.ExcelWriter('datatype.xlsx', engine='xlsxwriter')
        self.keys: List[str] = self.data.keys

    def create_table(self):
        try:
            for x, item in enumerate(self.data.parse_data()):
                df = pd.DataFrame(item[0])
                df.to_excel(self.writer, self.keys[x], index=False)
            self.writer.save()
            print('Файл создан')
        except Exception as ex:
            print(repr(ex))
