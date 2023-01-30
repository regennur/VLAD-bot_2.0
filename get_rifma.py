import requests


def getRif(word="кот"):
    res = []
    response = requests.get('https://py-data-scale.herokuapp.com/w/' + word)
    if response.status_code == 200:
        res_t = response.json()
        if 'data' in res_t:
            res = res_t['data']

    return res
