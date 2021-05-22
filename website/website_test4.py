import requests

# Create the session
with requests.session() as s:

    headers = {
        'authority': 'clients.mindbodyonline.com',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^88^\\^, ^\\^Google',
        'x-newrelic-id': 'XAIDV1FACwIBUVJUBgU=',
        'dnt': '1',
        'tracestate': '84467^@nr=0-1-84467-31153650-e5804c9d7e8102eb----1612943761064',
        'traceparent': '00-b545bd96c107dc0985560052e8f18e90-e5804c9d7e8102eb-01',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg0NDY3IiwiYXAiOiIzMTE1MzY1MCIsImlkIjoiZTU4MDRjOWQ3ZTgxMDJlYiIsInRyIjoiYjU0NWJkOTZjMTA3ZGMwOTg1NTYwMDUyZThmMThlOTAiLCJ0aSI6MTYxMjk0Mzc2MTA2NH19',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://clients.mindbodyonline.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://clients.mindbodyonline.com/asp/su1.asp?fl=true&tabID=2',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '__cfduid=ddba147d0d8d8f29600c1d757be05b9e01612935956; __cfruid=711f0badb6d3d906dc02d0a50e9f1735aa3f372d-1612935956; ASP.NET_SessionId=k0tc5mpwwge24hjapgo5a2nw; idsrvauth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U2VjdXJpdHlDb250ZXh0VG9rZW4gcDE6SWQ9Il8wMmRlNzQxMi04Mjg1LTQyZjAtYTA0Mi04MGJhMWM0NmUxOTQtQTEyNDI5OUY3Q0YxNEJDNzBCMjY4MjA2NDQwRjRGQjgiIHhtbG5zOnAxPSJodHRwOi8vZG9jcy5vYXNpcy1vcGVuLm9yZy93c3MvMjAwNC8wMS9vYXNpcy0yMDA0MDEtd3NzLXdzc2VjdXJpdHktdXRpbGl0eS0xLjAueHNkIiB4bWxucz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3Mtc3gvd3Mtc2VjdXJlY29udmVyc2F0aW9uLzIwMDUxMiI+PElkZW50aWZpZXI+dXJuOnV1aWQ6YWI0YzFlYmEtMDJkNi00Y2E3LWI4YmMtYjkwNWUyZjExNGQ4PC9JZGVudGlmaWVyPjxDb29raWUgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwNi8wNS9zZWN1cml0eSI+bHFXbDVJYnlBVmc4UDhzellyY3cvcE05eXNPMXA2azlmbzZsblRsYjFabUkvWUxYOUl5WGlCZ0c1R0Q4cVdmUkNhWUV6TW1DWVpsbUxxLzM3ZXBKdGgyZkROdTQrMGlpTUJDeEdBS1VwTTc1bEVZMWVJSUgxbjdzR21SVkozMzl6eUVRSmlpUE43SGJSV25CMUNucGMzZmRHRHNKY2taM3M1bVRvcWNsK2hmMldwaGE2VFRINU9oR21QdVlpZ3lEeE9ZVVRoeFBaR1JkaEZBYVhIZWNFdmJ1SEJyZmZBdHFycWFabmlvdGVNKyt1YUZ4dGVVNCtsR3YweXVZL3VzVmlXWnhYMGUvaDg0cTR2Wjd4Y09RUG5JdnBvVXhrWDFnOVNqRTNjUjBDZ0hVemhKYjZMcVZwVE1JYzBsdDUyM2c3bFFTVlJwMXJMeXF5dVEycTNTaG9rMFNndFlTRis5Zm4xQmlUY2NQbEhSSFFlS2l2WHJYZUVaU0ZFdzFySzZrU3NUWWljeG1XT2loZEdHaStRb3ZoRFhIZFZGMzV3NlJZUG0wSWYvVEZ6MkEzR05QcnpyWFlQQkhTZ3RLemp5M2FFY3lVditUV3d6Vjd1UUxYWXBmSHBTa0VWbjBBY1hQVXdDbTBPeHNobDZUNlp6cDRqbGxZcVRBR0k3VkpLT3R1Ui9VdjJlZUFibkhaUE1QRUFiYlRzR2ZyY2hUa3BrYmlrWUtMcmxRTi9Nd284L0szYzRYZ1hIN3U1enBKWFJGZ1NuR0xxRkJqcUZ3dFVDN2ZyMGxERE1RVGJyQzFOZjRyNzR5L3JqVjBkU1lQM3o4QlpmTHBoeHkvUHV3RE9SeVV6enNweFppamQxZ1BMbXN2bjZaRnBzaVBVSGkvYVRGY2I1M0FBdTdGM1F2aVJ0NjlLWWJuWjdFV0sxSjA2bnJqSDZodElGWVB6OHlLalk2alM2eGNiRDBRYXpVNnQvSlYxb3ZxRTB5L0lVUUZPVytLWkRWbHRJNzhnbEZMb082bks0bUdMUXJSRGh6NjFyNEFkZUE5YmVQUmg2cnYxWENKcE1XN3c1Z0dVdnlsLzVwamlhd0REbGltSVRpQ3lFa1lYV3lJb2FzcDhKUDg2c1JKN0E0QmpVaks5c0ZPaXZXdlI2cDB1OHZ0Kzdpd1BNdzROSWlPRGFEc1FTUi9CS1gycFdVWld4ckNoTWpBdmdRT3U0eUtjQU1zZ2tQY2pVU0RRK1dlSFpFazJUUXlaVzZWSVdwNEdLS2p2VXd3RHZYZThqRFExSWsyYWhhSGFJWEw1bnYzODFQREZCbENGQ0NLWVQzWWNJY3pCODFFbGVmVXBNd1A0QWwvSzVQSlhUS2JIY0UwVVBveG9CYTlJY2w3SVBPQWs0bEF4Z2Uwam1RMTZj; idsrvauth1=aG41MGEzS3lCbm96UnlieWlWR0RZYkROQjBBRGl2NGVJUFNhN2hTWit3MGtKOTBVSGxCdnlsTzRYMEhnRkJFTW1NdVVVbmxXMGIyN0hKU0FIRmJ1UlJRczN3WkNhTkZIK0FkamtlaGVrQ2ZYQVBaRFNnZ0JmL1RvZnRESnZKZ2dVK2hHdVg2eDh0Ym9Fa0xUNUtCNEYzby9JblQ4bVpQV29Ic29uMjhmcFFMN2ZIdTdvTFZFb2pxTVNGaVdidEdxbkJobE5VNXdDM3RwMW5ZNjVGWmxjRFE2N1NORmR1MTdFdUFKOVdtb2YxcEZHZ3RQQ0RoWVNHVERabEtTYmpKNHhhQ0dNeFhYN2FtWjAxcGlmN1RQRlZIQ0JPenNlT3hyOFRUbExacVhvNU4wWUFjK1JOUFZ5eEtkRzJzOE40YVV2Wk4vZjl6QTlWaEVVQ2RQMzBMcGkwMTZmcklsZDhIb1VFUS96RjM3ZFYrWUU4M1NDOWc9PTwvQ29va2llPjwvU2VjdXJpdHlDb250ZXh0VG9rZW4+; TS018b63df=01c8c98c892524989c21c74d4a4078b609547cc78741d58a38e40ff37a15ed9e46fbaf3a4d9862a6c95985dadba3612cc140e89b1fbf45db9d9606e59ca1a8d688abb9d17fe7aebf86d4f49a6c7edb99f00f9e1fec0fded1d4138402317b652789e1ac200b5928a3af6cae5ec5e436420f55e43f3c; __cfduid=d4769d2fd0dbb7fb5242f47023848cb8f1612939472; _ga=GA1.2.1324984483.1612939478; _gid=GA1.2.1809238698.1612939478; amplitude_id_97402fcd6ecc64057a3931d5ba552b09mindbodyonline.com=eyJkZXZpY2VJZCI6IjZlM2NjZjE3LWM3YzYtNDExZi1iZDUxLWY5ODA1MmRjNzM1M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYxMjkzOTQ2OTMzNSwibGFzdEV2ZW50VGltZSI6MTYxMjkzOTQ3ODg5NiwiZXZlbnRJZCI6NCwiaWRlbnRpZnlJZCI6MSwic2VxdWVuY2VOdW1iZXIiOjV9; SessionFarm^%^5FGUID=^{820A72DC-ACF1-48C1-80C2-32DF82954C4E^}; __cf_bm=6b4c0bfafe677d195732b93c4c36caab838105e9-1612942044-1800-AQlvNr+NyYR/MD4dlnW42GUkmstpfwK9zgAHII6JyhDj0bJQKNr6HMGRUk6LqGc50yQFRiKpdnM5lb5yko0bUkjrjqAj//+uHykI1JV8f70mryP4YPHfqIv7RoHi1o48pABJ+huRSR/+f1vIc1ifirNOauWu/ZWiisLrH+bhVTh3vr561L8ta5EwmWcGroWxew==; amplitude_id_c13fc4b6af51e4f152a6988a74ec6dfamindbodyonline.com=eyJkZXZpY2VJZCI6IjIwYTU4NDhjLTA2YWItNDQ0Yi04MGQzLTBmMjczMDc1MmI1M1IiLCJ1c2VySWQiOiIxMDAwMDU4MzIiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MTI5MzU5NTcwNjMsImxhc3RFdmVudFRpbWUiOjE2MTI5NDM3NDU4ODQsImV2ZW50SWQiOjM5LCJpZGVudGlmeUlkIjowLCJzZXF1ZW5jZU51bWJlciI6Mzl9; TS0167d462=01c8c98c8981576ee6b8cc51948befbfbf82a28f0b62ee81fdd60560c96c06b85100b42221aa1d82e802ca24f2157df35755ec47ef600f413fec75fe4472ee9a59e60ec17fb231faf603d5789d56e311be259db856',
    }

    params = (
        ('studioID', '16575'),
        ('isLibAsync', 'true'),
        ('isJson', 'true'),
    )

    data = {
    'requiredtxtUserName': 'dsmart2833^%^40gmail.com',
    'requiredtxtPassword': 'K^%^5BkJ4cPacjx9J^%^25N^%^26J^%^5E(A',
    'tg': '',
    'vt': '',
    'lvl': '',
    'stype': '',
    'qParam': '',
    'view': '',
    'trn': '0',
    'page': '',
    'catid': '',
    'prodid': '',
    'date': '2^%^2F9^%^2F2021',
    'classid': '0',
    'sSU': '',
    'optForwardingLink': '',
    'isAsync': 'false'
    }

    response = requests.post('https://clients.mindbodyonline.com/Login', headers=headers, params=params, data=data)

    print(response.content)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.post('https://clients.mindbodyonline.com/Login?studioID=16575&isLibAsync=true&isJson=true', headers=headers, data=data)
