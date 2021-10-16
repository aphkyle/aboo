"""Get random images of bananas"""
import random
from urllib import request

from googleapiclient.discovery import build


class Banana:
    def __init__(self, api_key, cse_id):
        self._api_key = api_key
        self._cse_id = cse_id

    def get_random_banana(self) -> bytes:
        start_index = random.randrange(1, 11)
        service = build("customsearch", "v1", developerKey=self._api_key)
        results = (
            service.cse()
            .list(q="banana", cx=self._cse_id, searchType="image", start=start_index)
            .execute()
        )["items"]
        random_num = random.randrange(1, len(results))
        image_link = results[random_num]["image"]["thumbnailLink"]
        r = request.urlopen(image_link)
        image = r.read()
        r.close()
        return image
