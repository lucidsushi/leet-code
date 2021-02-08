import json
import time
from typing import Callable

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


"""
- https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/
- https://requests.readthedocs.io/en/master/user/advanced/
- https://stackoverflow.com/questions/21371809/cleanly-setting-max-retries-on-python-requests-get-or-post-method
- https://stackoverflow.com/questions/35704392/how-to-make-python-post-requests-to-retry
"""

# print(
#     json.dumps(json_response, sort_keys=True, indent=2)
# )

# base code
def find_boomer(gender: str) -> dict:

    adapter = HTTPAdapter(max_retries=Retry(total=3, status_forcelist=[503]))
    http = requests.Session()
    http.mount("http://", adapter)
    http.mount("https://", adapter)
    json_response = http.get(f'https://randomuser.me/api/?gender={gender}').json()  # IO

    result, = json_response['results']
    is_boomer = result['dob']['age'] >= 55
    if not is_boomer:
        raise ValueError(f'User {result["name"]["first"]} is not an adult {gender}')
    return result

find_boomer(gender='male')


def exponential_backoff(
    retries: int = 2, delay: float = 1, backoff: float = 1, max_delay: int = 1
) -> Callable:
    """
    for timeout in exponential_backoff()():
        response = requests.get(url)  # I/O
        if response.ok:
            json_response = response.json()
        else:
            time.sleep(timeout)
            continue
    """
    def backoff_gen():
        for retry in range(0, retries):
            sleep = delay * backoff ** retry
            yield sleep if max_delay is None else min(sleep, max_delay)
    return backoff_gen