# Import the discord library
import json
import asyncio
import requests
from datetime import datetime, timezone, timedelta

async def register_mb(startTime, daysOut):
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    # Create the result to return
    result = []
    
    # Create the session
    with requests.session() as s:

        payload = {
            'requiredtxtUserName': '***REMOVED***',
            'requiredtxtPassword': 'K[kJ4cPacjx9J%N&J^(A'
            # 'tg': ,
            # 'vt': ,
            # 'lvl': ,
            # 'stype': ,
            # 'qParam': ,
            # 'view': ,
            # 'trn': '0',
            # 'page': ,
            # 'catid': ,
            # 'prodid': ,
            # 'date': '2/9/2021',
            # 'classid': '0',
            # 'sSU': ,
            # 'optForwardingLink': ,
            # 'isAsync': 'false'
        }

        login = s.post('https://clients.mindbodyonline.com/Login?studioID=16575&isLibAsync=true&isJson=true', data = payload)

        print(login)