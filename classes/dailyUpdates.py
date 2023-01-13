import asyncio
import json
import requests
from datetime import datetime, timezone, timedelta
import html2text

async def getDailyUpdate():
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    # Request the posts
    url=configFile["urls"]['posts']
    request_headers={
        'Host': 'perform-360.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-GPC': '1'
    }

    r = requests.get(url, headers=request_headers)
    workoutsData = r.json()
    
    # Get tomorrows date
    tomorrowsDate = datetime.now().date() + timedelta(days=1)

    for workouts in workoutsData:
        # post date time string
        postDateTime = workouts['date_gmt']
        # Convert to datetime object
        postDateTimeObject = datetime.strptime(postDateTime, '%Y-%m-%dT%H:%M:%S')        
        # Remove the time from the object
        postDate = postDateTimeObject.date()
        
        # print(workouts)
        # print(postDate)
        # print(tomorrowsDate)
        # print(workouts['slug'])
        # print('----\n----\n')

        if (postDate <= tomorrowsDate) and ('this-weeks-training' in workouts['slug']):
            post = workouts['content']['rendered']

            # html2text
            h = html2text.HTML2Text()
            h.ignore_links = True

            # Cut headings before 'NEWS'
            seperatePost = h.handle(post).split('* ####')

            tomorrow = tomorrowsDate.strftime('%A')

            for post in seperatePost:
                if (tomorrow.upper() in post) and (len(post) > 20):
                    newpost = post.replace('*', '').replace('_', '').replace('## PSC', 'PSC')

                    newpost = newpost.splitlines()

                    whereToStartFormattedPost = 0
                    formattedPost = tomorrow[:3] + ' ' + tomorrowsDate.strftime('%m-%d') + '\n'

                    for idx, line in enumerate(newpost):
                        if 'PSC' in line:
                            whereToStartFormattedPost = idx + 1
                    
                    for line in newpost[whereToStartFormattedPost:]:
                        if line != '\n':
                            formattedPost = formattedPost + line + '\n'
                    
                    return(formattedPost)