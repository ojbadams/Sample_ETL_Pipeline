""" Make Query and Return Data """
import json
import requests


def make_request(url: str) -> dict:
    """ Make a Request and Return Response

    ```
    Parameters:
    -----------
    url: str

    ```
    """

    response = requests.get(url)
    response = json.loads(response.content)

    return response
