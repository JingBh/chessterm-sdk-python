from urllib.parse import urljoin

import requests

from . import __version__ as sdk_version
from requests.__version__ import __version__ as lib_version

BASEURL = "https://chessterm.tech/"
HEADERS = {
    "User-Agent": "JWS chessterm-sdk-python/%s python-requests/%s" % (sdk_version, lib_version)
}


def request(method, uri, **options):
    url = urljoin(BASEURL, uri)

    headers = HEADERS.copy()
    if "headers" in options:
        headers.update(options["headers"])
    options["headers"] = headers

    r = requests.request(method, url, **options)
    r.raise_for_status()
    if r.headers["content-type"] == "application/json":
        result = r.json()
        if "success" in result and not result["success"]:
            if "message" in result and result["message"]:
                raise Exception(result["message"])
            else:
                raise Exception("Request is unsuccessful.")
        elif "data" in result:
            return result["data"]
        elif "success" in result:
            return True
        else:
            return result
    else:
        return r.text
