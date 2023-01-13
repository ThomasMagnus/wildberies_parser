import json
import aiohttp
import asyncio

from typing import List, Dict, Any


class Parser:

    def __init__(self, urls: List[str]):
        self.urls: List[str] = urls
        self.tup_result: List[List[Dict[str, Any]]] = []
        self.keys: List[str] = []

    async def request_data(self, url) -> None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url) as response:
                    json_result = await response.text()
                    data = json.loads(json_result).get('data', 'Non action')
                    self.keys.append(response.url.query['query'])
                    self.tup_result.append(data['products'])
        except Exception as ex:
            print(repr(ex))

    def create_loop(self) -> None:
        try:
            futures = [self.request_data(url) for url in self.urls]
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(futures))
        except Exception as ex:
            print(repr(ex))

    def parse_data(self) -> List:
        self.create_loop()
        result_lst = []
        for x, item in enumerate(self.tup_result):
            result_lst.append([
                {
                    'Title': [elem['name'] for elem in item],
                    'Brand': [elem['brand'] for elem in item],
                    'Id': [elem['id'] for elem in item],
                    'Feedback': [elem['feedbacks'] for elem in item],
                    'Price': [int(str(elem['salePriceU'])[:(len(str(elem['salePriceU'])) - 2)]) for elem in item]
                }
            ])
        return result_lst

