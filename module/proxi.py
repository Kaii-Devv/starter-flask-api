import requests

def filterProxy(proxy,valid):
    try:
        proxies = {
            'http': proxy,
            'https': proxy
                    }
        response = requests.request(
                    'GET',
                    'https://ipinfo.io/json',
                    proxies=proxies,timeout=3
                    )
        if not "ID" in response.json()['country']:
            valid.append(proxies)
    except Exception as e:pass