# Import the discord library
import requests

# Create the session
with requests.session() as s:

    s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'})

    s.get('https://clients.mindbodyonline.com/asp/su1.asp?fl=true&tabID=2')

    payload = {
        'requiredtxtUserName': '***REMOVED***',
        'requiredtxtPassword': 'K[kJ4cPacjx9J%N&J^(A',
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
        'date': '2/9/2021',
        'classid': '0',
        'sSU': '',
        'optForwardingLink': '',
        'isAsync': 'false'
    }

    print(s.cookies)

    headers = {
        'authority': 'clients.mindbodyonline.com',
        'method': 'POST',
        'path': '/Login?studioID=16575&isLibAsync=true&isJson=true',
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '218',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__cfduid=ddba147d0d8d8f29600c1d757be05b9e01612935956; __cfruid=711f0badb6d3d906dc02d0a50e9f1735aa3f372d-1612935956; ASP.NET_SessionId=k0tc5mpwwge24hjapgo5a2nw; __cf_bm=55d12f96012d176865ddb4735192cd172b7cfd99-1612936910-1800-Aauzaj32qL3KPeeCgwO8PrYnvTJWTDA0hZUwQpFYBG+PYX1NDJyQ30EawxmeBmlRDiwjDGx3lInQKEy9anv22fhmK+lFLTkjcRNoGICy1w5WkYb5NZpt1RQ/mkxQ+z/XAXAFrYXPhoLO7KfrU3B+HSb8QIfgyr+ARleY1dKOhdP3igfwZK8M93IZPOCUcVE0+w==; idsrvauth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U2VjdXJpdHlDb250ZXh0VG9rZW4gcDE6SWQ9Il85OGM2ZGE1MS1jNDFkLTQ3MTQtODQ2Mi00YTRjMjcxMmVjMDYtMUVCMjIzNTgzMjJBRkUwRkYzMzQ5MzQ1MTcwNTQzQTAiIHhtbG5zOnAxPSJodHRwOi8vZG9jcy5vYXNpcy1vcGVuLm9yZy93c3MvMjAwNC8wMS9vYXNpcy0yMDA0MDEtd3NzLXdzc2VjdXJpdHktdXRpbGl0eS0xLjAueHNkIiB4bWxucz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3Mtc3gvd3Mtc2VjdXJlY29udmVyc2F0aW9uLzIwMDUxMiI+PElkZW50aWZpZXI+dXJuOnV1aWQ6OTljYzdmNDQtNGFlMi00YzE2LWEzOWItMTVmMTI0NmIzNzg5PC9JZGVudGlmaWVyPjxDb29raWUgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwNi8wNS9zZWN1cml0eSI+RUtySCtabld2UDNMQWtMbEsyTE1uOGU5N2ZGMkM3V3hHcU5kbWhmd2dRMjIrblF5ZVV1a25lN29ZL3QvVjRqS1ZkU2lad1laKzg2Z05jTkJ3alZSZjQ1WFdoQmFRUHF5UlQ4M0JIMm9TOUoybE9iWlc4UGVYZkhhdzMyOEtpbG5mb2FSL0ZiUDU1UTdUM0FPVS92TGRybnhIL0hZN1ZoRWd3VHgyTWZBQTYwYm5MdlkvSGNmSGE2M3BDbm1hQnh3WUJtSWVXbFR6TXB0ZXl3RjVUUkczMDdNVXIxZ1F0WTEzRUpxc3FhU1M3SlQxQ1RCYWRMWVNISUQ4bXhyM2VxaURURnBNVzRLUzdYS2M5U0JRTE9kMzNadjZtUTVNcVhpVWo1UktMUHUwb2hwRVUyb0FrZEQ3SmVsc3FBMFBTNStCNnVPZ1ZpdEdOallQV2dnK1FFZm4rV0dxM1R4SDUwaTlNLzB0WWJiSjUxc1NmSTEySlZvTlhtMlpiYXV2VlpVeUhhbEVkY0x1UTlJTy8zQnBRbzR3RkJOWnVGZmYvSllxQzlwcjlLdDhCcHRFZFZMLzJ1Q09xQTlyc3hzckwvcDA5cG8rSVoydSt4WWQvbENYWElzYUYyaGRUOVBrTFE0eUhCZHVTTnVtbVJCODZUSjZkdzhML09rRFZJUEJrc28wZm5EN3lDZWFGai9sK0pnalhTaGM1WXNHOHB6elRhemN2cmpGVXo0QWxkRGJucjNqQzRRM0hYUzQ2NkJUNTk4ODk0QlVYbGw0cFd0a2VKbWorcFZLZ3FCMDFUYkw2RnhMM2RwVGFadHRWc0IwaTl4bm1wUHRIZ0pWQzlYSWFXUmFoMGZzb1RyR3hjTXFPV3JqRmdMbmxZV0xIN0g0ZEQrdERxdlV2Wmdtb2xOaGhBbGY2d3crWll5b3lZYTUrV29QSUZtZ09TdXA3UnVEeHRyQWdhK0ttVGpMcWZyRXpocCtYTDFUQ3VGM0FLLzJWVVNRS0k1dE45Mi8zMjlOUFZHSjBaWUoyWmo5U0hORkRTaWFzYWhERmppVXFYR3krUHJMSElqM3RmMzVXaHFYaGRKVTloR2EzTGpRTFdRV29Ud2ppTkhJUVQ0YjZyb3gza3N5Slo4anBMYllmU2dscWlFZkdXK0U2NksvMzBmQ3JPZW5Xd3ZnMFlkdVpsQXltSFo5UjNoMFAyQlhTSXJ6Nk83UG5GTEpwL3MvZk84UDVzak5HVmZCOUZhczBiR29GOHp4WXBmb3V4eTVhTEhLNWZ5OXJmUWMzbnZIcWFFVXhqZndlOG96bHpJcjdXK3NQZDZ2Y05YenBoU0RKNTk1UDcvTEhReW1vUE16bTJQTWNYT3JtYkZuUlN0TWZBbjF6ak44cUN1d1lvRGFhbWN5ZXdvSW9D; idsrvauth1=T3RtZng4YXFEYVJqTXFuZ2dzc2YxWFdqVjdxS3JzTVNoOVNRSjlyNGc5ZzZUQzlPbjRyc3lXOVpvOWpWRVZLMS9WNjRweVNBWG5LTmpIbk9Gd1M1VXk1cWI4b041SVlqZ1JIdnVzMXhEaFYwMWtqTDV1Ylg4ZGdYdFNIQTF6WnBYUlVEaE1oOHZzKzd2TGhtRXNoS0FTUjVzNzBmZnFIb1M0U0c0R3UybldrWVhwUVdRR3hLMGtwZjdDYmxuT3hSbkNhRFdnbTQxaU9FeFdNTklvZkNpU3JwaG1TUitaMEd2eVFzT2hsQlVvVjVJSExaK1N6TktDckY5U2tYS3hobXpCME5rM2lDSnhFTHRWa1hWZmlsMnBVMTFTWS8zRW9zTHNzdU1RUTcvalJLNFNrRHJtT3J4UGw2TVNLc2JUcGpvTStOd1pmNDdvbERXU2FrZFE0MnZES01TcG0rUjQyemMzdmtNNHJRK3VZSXdOU21oVlBXb2paNkc1UmhuTG5ISTRhc3NSOXc9PC9Db29raWU+PC9TZWN1cml0eUNvbnRleHRUb2tlbj4=; TS018b63df=01c8c98c89ac21d92f84b5bfcf1fd78a2034f89e3641d58a38e40ff37a15ed9e46fbaf3a4d9862a6c95985dadba3612cc140e89b1fbf45db9d9606e59ca1a8d688abb9d17fe7aebf86d4f49a6c7edb99f00f9e1fec6bb5898af0e389dca295bdad0506c1b0a75c369d5d279f988bd154b93cc8f539; SessionFarm%5FGUID={CCFC88D6-C5E6-444D-8484-35824720F4C1}; TS0167d462=01c8c98c890c322e785279797341cfc5873d8cc8b7fd5d15e108218fba0930f31670a52ae44c5b013642d9358ad21e172488d5168d50c16f0bb490e880589f8a76d9d3300a2bcde8a0680ae00fb1a3a7e40ad7bbf7; amplitude_id_c13fc4b6af51e4f152a6988a74ec6dfamindbodyonline.com=eyJkZXZpY2VJZCI6IjIwYTU4NDhjLTA2YWItNDQ0Yi04MGQzLTBmMjczMDc1MmI1M1IiLCJ1c2VySWQiOiIxMDAwMDU4MzIiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MTI5MzU5NTcwNjMsImxhc3RFdmVudFRpbWUiOjE2MTI5Mzc1OTczODQsImV2ZW50SWQiOjMwLCJpZGVudGlmeUlkIjowLCJzZXF1ZW5jZU51bWJlciI6MzB9',
        'dnt': '1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg0NDY3IiwiYXAiOiIzMTE1MzY1MCIsImlkIjoiZTkwZGI3YmEwYTlhODdjZiIsInRyIjoiYmE5NDhkNzhlZGE3MjgzYTI3YTNiNDgwYTM1NGYyNDAiLCJ0aSI6MTYxMjkzNzYxMzQwNH19',
        'origin': 'https://clients.mindbodyonline.com',
        'referer': 'https://clients.mindbodyonline.com/asp/su1.asp?fl=true&tabID=2',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-ba948d78eda7283a27a3b480a354f240-e90db7ba0a9a87cf-01',
        'tracestate': '84467@nr=0-1-84467-31153650-e90db7ba0a9a87cf----1612937613404',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'x-newrelic-id': 'XAIDV1FACwIBUVJUBgU=',
        'x-requested-with': 'XMLHttpRequest'
    }

    login = s.post('https://clients.mindbodyonline.com/Login?studioID=16575&isLibAsync=true&isJson=true', data = payload, headers = headers)
    print(login)
    print(login.content)

    headers2 = {
        'authority': 'clients.mindbodyonline.com',
        'method': 'GET',
        'path': '/classic/mainclass?fl=true&tabID=7',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '__cfduid=ddba147d0d8d8f29600c1d757be05b9e01612935956; __cfruid=711f0badb6d3d906dc02d0a50e9f1735aa3f372d-1612935956; ASP.NET_SessionId=k0tc5mpwwge24hjapgo5a2nw; SessionFarm%5FGUID={CCFC88D6-C5E6-444D-8484-35824720F4C1}; TS0167d462=01c8c98c890c322e785279797341cfc5873d8cc8b7fd5d15e108218fba0930f31670a52ae44c5b013642d9358ad21e172488d5168d50c16f0bb490e880589f8a76d9d3300a2bcde8a0680ae00fb1a3a7e40ad7bbf7; idsrvauth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U2VjdXJpdHlDb250ZXh0VG9rZW4gcDE6SWQ9Il8wMmRlNzQxMi04Mjg1LTQyZjAtYTA0Mi04MGJhMWM0NmUxOTQtQTEyNDI5OUY3Q0YxNEJDNzBCMjY4MjA2NDQwRjRGQjgiIHhtbG5zOnAxPSJodHRwOi8vZG9jcy5vYXNpcy1vcGVuLm9yZy93c3MvMjAwNC8wMS9vYXNpcy0yMDA0MDEtd3NzLXdzc2VjdXJpdHktdXRpbGl0eS0xLjAueHNkIiB4bWxucz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3Mtc3gvd3Mtc2VjdXJlY29udmVyc2F0aW9uLzIwMDUxMiI+PElkZW50aWZpZXI+dXJuOnV1aWQ6YWI0YzFlYmEtMDJkNi00Y2E3LWI4YmMtYjkwNWUyZjExNGQ4PC9JZGVudGlmaWVyPjxDb29raWUgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwNi8wNS9zZWN1cml0eSI+bHFXbDVJYnlBVmc4UDhzellyY3cvcE05eXNPMXA2azlmbzZsblRsYjFabUkvWUxYOUl5WGlCZ0c1R0Q4cVdmUkNhWUV6TW1DWVpsbUxxLzM3ZXBKdGgyZkROdTQrMGlpTUJDeEdBS1VwTTc1bEVZMWVJSUgxbjdzR21SVkozMzl6eUVRSmlpUE43SGJSV25CMUNucGMzZmRHRHNKY2taM3M1bVRvcWNsK2hmMldwaGE2VFRINU9oR21QdVlpZ3lEeE9ZVVRoeFBaR1JkaEZBYVhIZWNFdmJ1SEJyZmZBdHFycWFabmlvdGVNKyt1YUZ4dGVVNCtsR3YweXVZL3VzVmlXWnhYMGUvaDg0cTR2Wjd4Y09RUG5JdnBvVXhrWDFnOVNqRTNjUjBDZ0hVemhKYjZMcVZwVE1JYzBsdDUyM2c3bFFTVlJwMXJMeXF5dVEycTNTaG9rMFNndFlTRis5Zm4xQmlUY2NQbEhSSFFlS2l2WHJYZUVaU0ZFdzFySzZrU3NUWWljeG1XT2loZEdHaStRb3ZoRFhIZFZGMzV3NlJZUG0wSWYvVEZ6MkEzR05QcnpyWFlQQkhTZ3RLemp5M2FFY3lVditUV3d6Vjd1UUxYWXBmSHBTa0VWbjBBY1hQVXdDbTBPeHNobDZUNlp6cDRqbGxZcVRBR0k3VkpLT3R1Ui9VdjJlZUFibkhaUE1QRUFiYlRzR2ZyY2hUa3BrYmlrWUtMcmxRTi9Nd284L0szYzRYZ1hIN3U1enBKWFJGZ1NuR0xxRkJqcUZ3dFVDN2ZyMGxERE1RVGJyQzFOZjRyNzR5L3JqVjBkU1lQM3o4QlpmTHBoeHkvUHV3RE9SeVV6enNweFppamQxZ1BMbXN2bjZaRnBzaVBVSGkvYVRGY2I1M0FBdTdGM1F2aVJ0NjlLWWJuWjdFV0sxSjA2bnJqSDZodElGWVB6OHlLalk2alM2eGNiRDBRYXpVNnQvSlYxb3ZxRTB5L0lVUUZPVytLWkRWbHRJNzhnbEZMb082bks0bUdMUXJSRGh6NjFyNEFkZUE5YmVQUmg2cnYxWENKcE1XN3c1Z0dVdnlsLzVwamlhd0REbGltSVRpQ3lFa1lYV3lJb2FzcDhKUDg2c1JKN0E0QmpVaks5c0ZPaXZXdlI2cDB1OHZ0Kzdpd1BNdzROSWlPRGFEc1FTUi9CS1gycFdVWld4ckNoTWpBdmdRT3U0eUtjQU1zZ2tQY2pVU0RRK1dlSFpFazJUUXlaVzZWSVdwNEdLS2p2VXd3RHZYZThqRFExSWsyYWhhSGFJWEw1bnYzODFQREZCbENGQ0NLWVQzWWNJY3pCODFFbGVmVXBNd1A0QWwvSzVQSlhUS2JIY0UwVVBveG9CYTlJY2w3SVBPQWs0bEF4Z2Uwam1RMTZj; idsrvauth1=aG41MGEzS3lCbm96UnlieWlWR0RZYkROQjBBRGl2NGVJUFNhN2hTWit3MGtKOTBVSGxCdnlsTzRYMEhnRkJFTW1NdVVVbmxXMGIyN0hKU0FIRmJ1UlJRczN3WkNhTkZIK0FkamtlaGVrQ2ZYQVBaRFNnZ0JmL1RvZnRESnZKZ2dVK2hHdVg2eDh0Ym9Fa0xUNUtCNEYzby9JblQ4bVpQV29Ic29uMjhmcFFMN2ZIdTdvTFZFb2pxTVNGaVdidEdxbkJobE5VNXdDM3RwMW5ZNjVGWmxjRFE2N1NORmR1MTdFdUFKOVdtb2YxcEZHZ3RQQ0RoWVNHVERabEtTYmpKNHhhQ0dNeFhYN2FtWjAxcGlmN1RQRlZIQ0JPenNlT3hyOFRUbExacVhvNU4wWUFjK1JOUFZ5eEtkRzJzOE40YVV2Wk4vZjl6QTlWaEVVQ2RQMzBMcGkwMTZmcklsZDhIb1VFUS96RjM3ZFYrWUU4M1NDOWc9PTwvQ29va2llPjwvU2VjdXJpdHlDb250ZXh0VG9rZW4+; TS018b63df=01c8c98c892524989c21c74d4a4078b609547cc78741d58a38e40ff37a15ed9e46fbaf3a4d9862a6c95985dadba3612cc140e89b1fbf45db9d9606e59ca1a8d688abb9d17fe7aebf86d4f49a6c7edb99f00f9e1fec0fded1d4138402317b652789e1ac200b5928a3af6cae5ec5e436420f55e43f3c; amplitude_id_c13fc4b6af51e4f152a6988a74ec6dfamindbodyonline.com=eyJkZXZpY2VJZCI6IjIwYTU4NDhjLTA2YWItNDQ0Yi04MGQzLTBmMjczMDc1MmI1M1IiLCJ1c2VySWQiOiIxMDAwMDU4MzIiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MTI5MzU5NTcwNjMsImxhc3RFdmVudFRpbWUiOjE2MTI5Mzc2MTYyMTksImV2ZW50SWQiOjMxLCJpZGVudGlmeUlkIjowLCJzZXF1ZW5jZU51bWJlciI6MzF9',
        'dnt': '1',
        'referer': 'https://clients.mindbodyonline.com/ASP/main_info.asp?studioid=16575&tg=&vt=&lvl=&stype=&view=&trn=0&page=&catid=&prodid=&date=2%2f9%2f2021&classid=0&prodGroupId=&sSU=&optForwardingLink=&qParam=&justloggedin=true&nLgIn=&pMode=0&loc=1',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    classes = s.get('https://clients.mindbodyonline.com/classic/mainclass?fl=true&tabID=7', headers=headers2)

    print(classes)
    #print(classes.content)