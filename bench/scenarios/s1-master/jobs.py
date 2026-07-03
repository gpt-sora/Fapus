from netclient import fetch_status


def check(url):
    return fetch_status(url) == 200
