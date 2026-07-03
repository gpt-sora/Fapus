import urllib.request


def fetch_status(url):
    with urllib.request.urlopen(url, timeout=2) as r:
        return r.status
