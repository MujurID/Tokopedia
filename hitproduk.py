import requests

cookies = {
    'bm_sz': 'ECF2A514E986C8C1AE7F7A0A9946EB1E~YAAQvIt4aAOCEN1uAQAADsLMDwYX49fw0en0mE7aH/irdfZOpr3Th1aHxvuy4QU8qVwsgrbv9oiDhtEbV3cbQhkueJ8tUN8S6cJ93pqX3EUnvpe3EJYkmQneLqfjeaKLAwUcneyD9atj/2VEadY5bEEXLiwaYbLPi4JJSkGqRyqUa87wZllr11Pt3Sa0r6HhyJub',
    'bm_mi': '38267715046F01D687D5A80C9007DB72~JocE82NvxEKtQCHa+3eJ8LGIbwHp5s7B043I4xNkTTwv8ji16I8z3muHudBQ1OYnAV81HOQsr3q98Rx4V0Vkzl7S12HHqzKNAHzulzaSDqS43HOzaPHH/2CxReXFdibrZl1Az6HDIr2JvSa4MK75d/wkulZC850IHDjW7h2pF3Y2lYnRe/nbnB3vM2TudNR4Ub13bkj4UjKRwZqOJ5/xMFgtUrOhiR98gD2ITY4ufEVRt9JB4khcK2b40yVSyB0KiGqr1Uh48V63F5ge7/lTw4SPQZTXFElL2blFjF5g4fT6WEKQf95rqAi3icLMGe44',
    '_abck': '00A54818A2C62045396F6C8D4598FC68~0~YAAQjh0gF/85YOZuAQAAq8nMDwPPQMCT6qqMBArcQQ3n0CEC61KoDhKyJy55Yk/cn8vJCp3Nhs4Ex7u2EmiwirycxtBWsFYJW7CbU+gStWDiWBX+NGFFAjmslkK/MheYMbZQDYI8y1TLy4gajjDIOoEXw8Dra6wHGi1nJmgbmmnfgZFC+bIQIIz4e10ulgi1iEQxoGKjUFnjOhQfmjLTHkRN9zxI7piMoBBl+zwxWYm2X6iEJ+tC+5qgEuonJ6eMlt/+FEtg7KlOdzTl7ob1m8THLCM3qPOhFI8rxi3BjHGKxo9HaoVav5LCXjHBI2mzSZt13bT4LlBJ+g==~-1~-1~-1',
    '_gcl_au': '1.1.807042596.1576518078',
    'ak_bmsc': 'F1C667DE1C978DCF606D667A5FC1BBFF68788BBC5E010000BAC1F75D55FBDB12~plALGF8FgRAl2hoOGcVwOMoEsV+9oa6vxTdOAhuR5F2htne+6ScGU8Ooxtfk2g7XW0KEQwjBaAEynlkhoXDw8/iOJodfHaekl1G6Cj6ZC5CuYS8WzWhcqqwmCP/abjoH/BufAIOmC+zXlGKfzm2qYF30pp5ytozBSUXnNY1WaXW9+OWzbuQW9THhAmQ1eZ9uEvzkmk4z33HZCthZ4dALcwszBQtPqc7IGwqBDY1vknFT50HM//mzT+/HV0lr4Ll99C',
    '_SID_Tokopedia_': '1TFNPfMQ513DFDYErZ2gmoEvvtCsjlk3FHBCHbo0X_sXEkSDn-njLzQ7ZGHZtVnnMiQCt_b91YkmdZMr6yqrwz-RkDOwuIqJl2OeHAx7O-TK-N3DVb6iBsyFG7iw_PpH',
    'DID': 'd862855711d28688d72d5ed4b6c68b40ba0a9840616d24fbff151efe98532b3022c19342f8b1b733b403d78317c142c8',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_ga': 'GA1.2.1622530881.1576518082',
    '_gid': 'GA1.2.1190386054.1576518082',
    '__asc': 'e3e519e916f0fcce4c108a1d721',
    '__auc': 'e3e519e916f0fcce4c108a1d721',
    'cto_lwid': '6e5a5fde-a68f-4a2e-9876-071086696278',
    'cto_bundle': 'Hnb6zF8xJTJCdEw5bWxiUWRpUmFyQ05nWnFJQjZKaWM4eEFUU1ZKbjZ2RlJaTkNMd09weiUyRmNxeTZsZTVseEtDNHpHbnFxNm1EdkJYYTZIM01KRlh6Tk1ONlprMW8wekJGNGprQjhUeXJLa0J6R2klMkJ1N01GMFMwWldzTnh6bFY2YjEzTGxrcQ',
    'bm_sv': '1D8C769D0037A8E65A7411C6C04DAE2D~195+X6dRxxpLoZ/2vIKQUmOD5tAcILNk7iNAVplfWm3mUUXmu0DW0b6nNlTF2/3Wgz+llHHpj2hajE5q5MjeLQf05NXoQf9mG0asuGhnxRReRvpFvc7XIN3uDRNjRsGB90jG/9qnAEyycpRjb3ld9KEOrE5fhbQG/Zk/wPsLEBU=',
    '_dc_gtm_UA-9801603-6': '1',
    'RT': 'sl=1&ss=1576518075899&tt=3352&obo=0&bcn=%2F%2F684fc53b.akstat.io%2F&sh=1576518691724%3D1%3A0%3A3352&dm=tokopedia.com&si=55e0a6dc-ca0a-4c91-975d-eee2e64e8255&ld=1576518691726',
}

headers = {
    'Host': 'ta.tokopedia.com',
    'origin': 'https://m.tokopedia.com',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://m.tokopedia.com/printerdtgmurah/printer-kaos-digital-import-gen3-a?aff=MzUwNDI5ODl8Ym5ycGFrM2JjMWE5ODQ4bjFsMWc=',
    'accept-language': 'ms-MY,ms;q=0.9,id-ID;q=0.8,id;q=0.7,en-US;q=0.6,en;q=0.5',
}

params = (
    ('tracker_id', '14607dfd-4700-5013-1f44-fa62509904cf.1576518321493'),
    ('ustring', 'MzUwNDI5ODl8Ym5ycGFrM2JjMWE5ODQ4bjFsMWc='),
    ('user_id', '0'),
    ('event', 'affiliate'),
    ('', ''),
)

response = requests.get('https://ta.tokopedia.com/affiliate/v1/tracker/track', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://ta.tokopedia.com/affiliate/v1/tracker/track?tracker_id=14607dfd-4700-5013-1f44-fa62509904cf.1576518321493&ustring=MzUwNDI5ODl8Ym5ycGFrM2JjMWE5ODQ4bjFsMWc=&user_id=0&event=affiliate&', headers=headers, cookies=cookies)
