from typing import List
from reader import Reader
from table import Table


def main():
    file_reader = Reader('Keys.txt')
    keys: List[str] = file_reader.get_keys()

    table: Table = Table([
        'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=2,12,3,18,15,21,101&curr=rub&dest=-1029256,-51490,-181290,123585809&emp=0&lang=' +
        f'ru&locale=ru&pricemarginCoeff=1.0&query={url.replace(" ", "%20")}&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&resultset=catalog&sort=popular&spp=' +
        '0&suppressSpellcheck=false' for url in keys])

    table.create_table()


if __name__ == '__main__':
    main()
