# Import the discord library
import discord
from aiohttp import ClientSession
import asyncio
import aiocron
import json
import re
import requests
from datetime import datetime, timezone, timedelta
import pytz
import html2text
import math
import calendar

# Import classes
import sys
import os
sys.path.append(os.path.abspath("./classes"))
from dailyUpdates import *
from registration import *
from registration_mb import *
from classSchedule import *

#
# On startup
#

# Read the config json file
with open('json/config.json') as f:
    config = json.load(f)

# Create an instance of client - this is the connection to discord
client = discord.Client()

# On startup
#@client.event
#async def on_ready():

#
# Scheduled Jobs
#

# MONDAY Classes
# register - 12:00 AM PST
@aiocron.crontab('0 0 * * sun')
async def registerForClass():
    
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    if configFile['classRegistration']['monday']['shouldRun'].lower() == "true":
        await postResults(await register(configFile['classRegistration']['monday']['24hr_start_time'], configFile['classRegistration']['monday']['days_out']))
    else:
        await postToChannel("<@" + str(configFile['p360_admins']['talker9']) + "> " + "registration for Monday classes is disabled", '')

# TUESDAY Classes
# register - 12:00 AM PST
@aiocron.crontab('0 0 * * mon')
async def registerForClass():

    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    if configFile['classRegistration']['tuesday']['shouldRun'].lower() == "true":
        await postResults(await register(configFile['classRegistration']['tuesday']['24hr_start_time'], configFile['classRegistration']['tuesday']['days_out']))
    else:
        await postToChannel("<@" + str(configFile['p360_admins']['talker9']) + "> " + "registration for Tuesday classes is disabled", '')

# WEDNESDAY Classes
# register - 12:00 AM PST
@aiocron.crontab('0 0 * * tue')
async def registerForClass():
    
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    if configFile['classRegistration']['wednesday']['shouldRun'].lower() == "true":
        await postResults(await register(configFile['classRegistration']['wednesday']['24hr_start_time'], configFile['classRegistration']['wednesday']['days_out']))
    else:
        await postToChannel("<@" + str(configFile['p360_admins']['talker9']) + "> " + "registration for Wednesday classes is disabled", '')

# THURSDAY Classes
# register - 12:00 AM PST
@aiocron.crontab('0 0 * * wed')
async def registerForClass():
    
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    if configFile['classRegistration']['thursday']['shouldRun'].lower() == "true":
        await postResults(await register(configFile['classRegistration']['thursday']['24hr_start_time'], configFile['classRegistration']['thursday']['days_out']))
    else:
        await postToChannel("<@" + str(configFile['p360_admins']['talker9']) + "> " + "registration for Thursday classes is disabled", '')

# FRIDAY Classes
# register - 12:00 AM PST
@aiocron.crontab('0 0 * * thu')
async def registerForClass():
    
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    if configFile['classRegistration']['friday']['shouldRun'].lower() == "true":
        await postResults(await register(configFile['classRegistration']['friday']['24hr_start_time'], configFile['classRegistration']['friday']['days_out']))
    else:
        await postToChannel("<@" + str(configFile['p360_admins']['talker9']) + "> " + "registration for Friday classes is disabled", '')

# SATURDAY Classes
# register - 12:00 AM PST
@aiocron.crontab('0 0 * * fri')
async def registerForClass():

    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    if configFile['classRegistration']['saturday']['shouldRun'].lower() == "true":
        await postResults(await register(configFile['classRegistration']['saturday']['24hr_start_time'], configFile['classRegistration']['saturday']['days_out']))
    else:
        await postToChannel("<@" + str(configFile['p360_admins']['talker9']) + "> " + "registration for Saturday classes is disabled", '')


# getTodaysWorkout - 12:00 AM PST
@aiocron.crontab('30 8 * * mon,tue,wed,thu,fri,sat,sun')
async def getTodaysWorkoutMotivation():
    await postResults(await getDailyUpdate())


# Delete the specified number of unpinned messages from a channel that are < 14 days old
async def purgeChannel(channelToPurge, howManyMessages):
    await client.get_channel(channelToPurge).purge(limit=howManyMessages, check=lambda msg: not msg.pinned)

async def postResults(results):
    for result in results:
            await postToChannel(result['data'], result['embed'])

async def postToChannel(msg, embedType):
#---# Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

#---# Workouts Post
    if (embedType == 'workouts_embed'):
        msg = msg.split('\n\n')
        # Header
        embedMsg = discord.Embed(title=msg[0], description="", color=int(configFile[embedType]['borderColor'], 16))
        # Message Body
        for message in msg[1:]:
            message = message.split('**\n')
            for messages in message:
                messages = messages.replace('**  \n', '***  \n').split('*  \n')
                if (messages != ['']):
                    if len(messages) > 1:
                        embedMsg.add_field(name=messages[0], value=messages[1], inline=False)
                    else:
                        embedMsg.add_field(name=messages[0], value="\u200B", inline=False)
        # Thumbnail
        embedMsg.set_thumbnail(url=configFile[embedType]['thumbnail'])
        # Post message
        await client.get_channel(configFile[embedType]['channel']).send(embed=embedMsg)
    
#---# Daily Update Post
    elif (embedType == 'daily_update_embed'):

        messageRows = msg.replace("'", "\'").replace('**\n\n', '***\n\n').split('*\n\n')

        # Header
        embedMsg = discord.Embed(title="\u200B", description="\u200B", color=int(configFile[embedType]['borderColor'], 16))
        embedMsg.add_field(name="\u200B", value="\u200B", inline=False)

        # Message Body
        for message in messageRows:
            
            chars = len(message)

            if chars < 1024:
                embedMsg.add_field(name="\u200B", value=message, inline=False)
            else: 
                msgList = message.split('.\n') 
                for splitMsg in msgList:
                    if splitMsg != "":
                        embedMsg.add_field(name="\u200B", value=splitMsg, inline=False)

        # Thumbnail
        embedMsg.set_thumbnail(url=configFile[embedType]['thumbnail'])
        # Post message
        await client.get_channel(configFile[embedType]['channel']).send(embed=embedMsg)

#---# Post the class schedules
    elif (embedType == 'schedule_embed'):

        # Clean the class channels
        await purgeChannel(configFile[embedType]['classes_bp'], None)
        await purgeChannel(configFile[embedType]['classes_ob'], None)
        await purgeChannel(configFile[embedType]['classes_pb'], None)

        # Load the classes
        with open('json/classes_bp.json') as f:
            bpClasses = json.load(f)
        with open('json/classes_ob.json') as f:
            obClasses = json.load(f)
        with open('json/classes_pb.json') as f:
            pbClasses = json.load(f)

        # Post Pacific Beach Classes
        for day in pbClasses:

            # Post an image
            await client.get_channel(configFile[embedType]['classes_pb']).send(configFile[embedType][day])

            # Each post has a max of 4 classes
            maxClasses = 1

            # For each class that day
            for wkClasses in pbClasses[day]:
                if maxClasses == 1:
                    # Header
                    embedMsg = discord.Embed(color=int(configFile[embedType]['borderColor'], 16))
                # Format 12hr start time
                time = datetime.strptime(wkClasses['Start time'], '%Y-%m-%dT%H:%M:%S').time()
                formattedTime = datetime.strptime(str(time), "%H:%M:%S").strftime("%I:%M %p")
                # Body
                embedMsg.add_field(name='Class Time', value=day.upper() + ' ' + formattedTime, inline=True)
                embedMsg.add_field(name='Registration ID', value=wkClasses['regId'], inline=True)
                embedMsg.add_field(name='Instructor', value=wkClasses['instructor'], inline=True)
                #embedMsg.add_field(name='Spots Available', value=str(workoutClass['# booked']) + '/' + str(workoutClass['maxcapacity']), inline=False)
                #embedMsg.add_field(name='# Waitlisted', value=str(workoutClass['# waitlisted']), inline=False)

                # increment for another class added
                maxClasses = maxClasses + 1

                if maxClasses == 2 or wkClasses == pbClasses[day][-1]:
                    # Post message
                    await client.get_channel(configFile[embedType]['classes_pb']).send(embed=embedMsg)
                    maxClasses = 1

        # Post Bay Park Classes
        for day in bpClasses:

            # Post an image
            await client.get_channel(configFile[embedType]['classes_bp']).send(configFile[embedType][day])

            # Each post has a max of 4 classes
            maxClasses = 1

            # For each class that day
            for wkClasses in bpClasses[day]:
                if maxClasses == 1:
                    # Header
                    embedMsg = discord.Embed(color=int(configFile[embedType]['borderColor'], 16))
                # Format 12hr start time
                time = datetime.strptime(wkClasses['Start time'], '%Y-%m-%dT%H:%M:%S').time()
                formattedTime = datetime.strptime(str(time), "%H:%M:%S").strftime("%I:%M %p")
                # Body
                embedMsg.add_field(name='Class Time', value=day.upper() + ' ' + formattedTime, inline=True)
                embedMsg.add_field(name='Registration ID', value=wkClasses['regId'], inline=True)
                embedMsg.add_field(name='Instructor', value=wkClasses['instructor'], inline=True)
                #embedMsg.add_field(name='Spots Available', value=str(workoutClass['# booked']) + '/' + str(workoutClass['maxcapacity']), inline=False)
                #embedMsg.add_field(name='# Waitlisted', value=str(workoutClass['# waitlisted']), inline=False)

                # increment for another class added
                maxClasses = maxClasses + 1

                if maxClasses == 2 or wkClasses == bpClasses[day][-1]:
                    # Post message
                    await client.get_channel(configFile[embedType]['classes_bp']).send(embed=embedMsg)
                    maxClasses = 1

        # Post Ocean Beach Classes
        for day in obClasses:

            # Post an image
            await client.get_channel(configFile[embedType]['classes_ob']).send(configFile[embedType][day])

            # Each post has a max of 4 classes
            maxClasses = 1

            # For each class that day
            for wkClasses in obClasses[day]:
                if maxClasses == 1:
                    # Header
                    embedMsg = discord.Embed(color=int(configFile[embedType]['borderColor'], 16))
                # Format 12hr start time
                time = datetime.strptime(wkClasses['Start time'], '%Y-%m-%dT%H:%M:%S').time()
                formattedTime = datetime.strptime(str(time), "%H:%M:%S").strftime("%I:%M %p")
                # Body
                embedMsg.add_field(name='Class Time', value=day.upper() + ' ' + formattedTime, inline=True)
                embedMsg.add_field(name='Registration ID', value=wkClasses['regId'], inline=True)
                embedMsg.add_field(name='Instructor', value=wkClasses['instructor'], inline=True)
                #embedMsg.add_field(name='Spots Available', value=str(workoutClass['# booked']) + '/' + str(workoutClass['maxcapacity']), inline=False)
                #embedMsg.add_field(name='# Waitlisted', value=str(workoutClass['# waitlisted']), inline=False)

                # increment for another class added
                maxClasses = maxClasses + 1

                if maxClasses == 2 or wkClasses == obClasses[day][-1]:
                    # Post message
                    await client.get_channel(configFile[embedType]['classes_ob']).send(embed=embedMsg)
                    maxClasses = 1

#---# All other posts
    else:
        await client.get_channel(configFile['channel_ids']['general']).send(msg)

#
# Bot Commands
#

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#---# Get the daily update post
    if '!du' in message.content.lower():
        await asyncio.sleep(1)
        await message.channel.send('Getting today\'s workout..')
        await message.delete()
        await postResults(await getDailyUpdate())
        await message.channel.send('complete')
        await asyncio.sleep(5)
        await purgeChannel(config['channel_ids']['general'], 2)

#---# Purge channels
    if '!purge' in message.content.lower():
        await asyncio.sleep(1)
        await message.delete()
        await purgeChannel(config['channel_ids']['general'], None)
        await purgeChannel(config['channel_ids']['workouts'], None)
        await purgeChannel(config['channel_ids']['motivation'], None)

#---# Register for a class
    if '!reg' in message.content.lower():
        await asyncio.sleep(1)
        await message.delete()

        #await register_mb()

        # Load the config file
        with open('json/config.json') as f:
            configFile = json.load(f)

        if configFile['classRegistration']['wednesday']['shouldRun'].lower() == "true":
            await postResults(await register(configFile['classRegistration']['wednesday']['24hr_start_time'], configFile['classRegistration']['wednesday']['days_out']))
        else:
            await postToChannel("<@" + str(configFile['p360_admins']['talker9']) + "> " + "registration for tuesday classes is disabled", '')

#---# Get the class schedules
    if '!sched' in message.content.lower():
        await asyncio.sleep(1)
        await message.delete()
        await postResults(await getSchedule())
        await postToChannel('', 'schedule_embed')

#
# Login
#

# Login and run the client with the provided token
client.run(config['discord_client']['token'])