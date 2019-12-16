import requests

headers = {
    'Host': 'www.tokopedia.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'accept-language': 'ms-MY,ms;q=0.9,id-ID;q=0.8,id;q=0.7,en-US;q=0.6,en;q=0.5',
}

params = (
    ('src', 'tokopedia.by'),
)

response = requests.get('https://www.tokopedia.com/people/35042989/mujurid', headers=headers, params=params, verify='/etc/ssl/certs/ca-certificates.crt')

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.tokopedia.com/people/35042989/mujurid?src=tokopedia.by', headers=headers)
