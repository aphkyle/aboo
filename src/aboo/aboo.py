"""Get random images and facts of bananas"""
import random
from urllib import request

from googleapiclient.discovery import build


class Banana:
    def __init__(self, api_key: str = None, cse_id: str = None):
        self._api_key = api_key
        self._cse_id = cse_id

    def get_random_banana(self) -> bytes:
        if self._api_key is None or self._cse_id is None:
            raise Exception("Please set api key and cse id")

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

    def get_banana_fact(self) -> str:
        facts = [
            "Bananas are one of the most popular fruits in the American diet",
            "Bananas grow on plants that are officially considered an herb",
            "The banana is actually classified as a berry",
            "Bananas ripen significantly faster when attached to a bunch",
            "A thief in Mumbai was forced to eat 48 bananas so that the gold chain he had swallowed when he was arrested would leave his body.",
            "Bananas are curved because they grow upside-down towards the sun",
            "There are more trade restrictions on bananas than on AK-47s.",
            "Bananas give off radiation",
            "Slipping on banana peels became a comedic staple after banana peels were deemed a threat to public safety in the late 1800s.",
            "Despite frequently being portrayed in a sexual way, the most common strain of bananas are completely sterile",
            "Bananas can be found in other colors, including red ",
        ]
        fact = random.choice(facts)
        return fact
