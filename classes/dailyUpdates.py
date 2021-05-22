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
    r = requests.get(url)
    workoutsData = r.json()
    
    # Get todays date
    todaysDate = datetime.now().date()

    for workouts in workoutsData:
        # post date time string
        postDateTime = workouts['date_gmt']
        # Convert to datetime object
        postDateTimeObject = datetime.strptime(postDateTime, '%Y-%m-%dT%H:%M:%S')        
        # Remove the time from the object
        postDate = postDateTimeObject.date()
        
        if (postDate == todaysDate) and ('this-weeks-training' not in workouts['slug']):
            post = workouts['content']['rendered']
            #post = post.split('</em></p>')

            # html2text
            h = html2text.HTML2Text()
            h.ignore_links = True

            # workout = {"data":h.handle(post[1]), "embed":'workouts_embed'}
            # motivation = {"data":h.handle(post[0]), "embed":'daily_update_embed'}
            
            # # Format
            # motivation['data'] = workout['data'].split('\n')[0] + motivation['data'].replace('###', '').replace('\n ', '\n').replace('_-', '\t-')

            seperatePost = h.handle(post).split('-Dave')

            dailyUpdateFormatted = seperatePost[0] + '-Dave' 

            dailyUpdate = {"data":dailyUpdateFormatted.replace('###', '').replace('\n ', '\n').replace('_-', '\t-'), "embed":'daily_update_embed'}
            #workout = {"data":seperatePost[1], "embed":'workouts_embed'}

            #result = [workout, motivation]
            #result = [dailyUpdate, workout]
            result = [dailyUpdate]

            return result