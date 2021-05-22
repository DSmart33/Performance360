# Import the discord library
import discord
from discord.ext import commands
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
from registrationNew import *
from classSchedule import *

#
# On startup
#

# Read the config files to global variables
with open('json/config.json') as f:
    config = json.load(f)
with open('json/users/users.json') as f:
    userConfig = json.load(f)
with open('json/http/headers.json') as f:
    headersConfig = json.load(f)

# Create a global instance of client - this is the connection to discord
# Set the prefix for commands as well
client = commands.Bot(command_prefix='.', case_insensitive=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class userClass():
    # Constructor
    def __init__(self, name):
        self.name = name
        self.session = requests.session()
        self.dataToken = ''
        self.userId = 0
    # GET
    def getName(self):
        return(self.name)
    def getSession(self):
        return(self.session)
    def getDataToken(self):
        return(self.dataToken)
    def getUserId(self):
        return(self.userId)
    # SET
    def setDataToken(self, dataToken):
        self.dataToken = dataToken
    def setUserId(self, userId):
        self.userId = userId

# Create a global list to store each user object
users = []

# Create an object for each user
for idx, user in enumerate(userConfig):
    # Construct the user object
    users.append(userClass(user))
    # Login to p360 and store the dataToken
    p360 = users[idx].getSession().post("https://p360ppt.com/granjur/api/auth/login", json=userConfig[user]['login']['p360ppt'], headers=headersConfig['p360_headers'])
    json_response = json.loads(p360.text)
    users[idx].setDataToken(json_response['data']['token'])
    # Login to mindbody and store the user id
    mindbody = users[idx].getSession().post("https://p360ppt.com/granjur/api/auth/mind-body/get-client-id?token=" + users[idx].getDataToken(), json=userConfig[user]['login']['mindbody'], headers=headersConfig['mindbody_headers'])
    json_data = json.loads(mindbody.text)
    users[idx].setUserId(json_data['data']['ID'])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# On startup
#@client.event
#async def on_ready():

#
# Announce scheduled Jobs at 6:30PM PST
#
@aiocron.crontab('30 18 * * mon,tue,wed,thu,sat,sun')
async def announceSchedule():
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)
    with open('json/users/users.json') as f:
        userConfig = json.load(f)
    with open('json/http/headers.json') as f:
        headersConfig = json.load(f)

    # Store the day of the week
    tomorrow  = datetime.now() + timedelta(days=2)
    dayMonthYear = tomorrow.strftime('%m/%d/%Y')
    dayOfTheWeek = tomorrow.strftime("%A").lower()

    # Store the announcments in a list to be posted
    theSchedule = []

    # Announcment header
    theSchedule.append(dayOfTheWeek.capitalize() + ' - ' + dayMonthYear)
    # Announcement
    for user in userConfig: 
        if userConfig[user]['classRegistration'][dayOfTheWeek]['shouldRun'].lower() == "true":
            classTime = datetime.strptime(userConfig[user]['classRegistration'][dayOfTheWeek]['24hr_start_time'], "%H:%M").strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
            theSchedule.append("<@" + str(userConfig[user]['discord']) + "> - " + classTime + '')
        else:
            theSchedule.append("<@" + str(userConfig[user]['discord']) + "> - " + 'DISABLED')
    theSchedule.append("This message will self-destruct at 11:59 PM")
    # Post it
    await postToChannel(theSchedule, 'nightly_schedule_embed')

# All Classes
# register - 12:00 AM PST
@aiocron.crontab('0 0 * * mon,tue,wed,thu,fri,sun')
async def registerForClass():
    
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)
    with open('json/users/users.json') as f:
        userConfig = json.load(f)
    with open('json/http/headers.json') as f:
        headersConfig = json.load(f)

    # Store the day of the week
    today  = datetime.now() + timedelta(days=1)
    dayMonthYear = today.strftime('%m/%d/%Y')
    dayOfTheWeek = today.strftime("%A").lower()

    # For each user
    for idx, user in enumerate(userConfig):        
        if userConfig[user]['classRegistration'][dayOfTheWeek]['shouldRun'].lower() == "true":
            await postResults(await register(userConfig[user]['classRegistration'][dayOfTheWeek]['24hr_start_time'], userConfig[user]['classRegistration'][dayOfTheWeek]['days_out'], users[idx].getSession(), users[idx].getDataToken(), users[idx].getUserId()))
        else:
            await postToChannel("<@" + str(userConfig[user]['discord']) + "> " + "registration for " + dayOfTheWeek.capitalize() + " classes is disabled", 'register_for_class_embed')

# All Classes
# register - 12:00 AM PST
@aiocron.crontab('30 0 * * mon,tue,wed,thu,fri,sun')
async def registerForClassBackup():
    
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)
    with open('json/users/users.json') as f:
        userConfig = json.load(f)
    with open('json/http/headers.json') as f:
        headersConfig = json.load(f)

    # Store the day of the week
    today  = datetime.now() + timedelta(days=1)
    dayMonthYear = today.strftime('%m/%d/%Y')
    dayOfTheWeek = today.strftime("%A").lower()

    # For each user
    for idx, user in enumerate(userConfig):        
        if userConfig[user]['classRegistration'][dayOfTheWeek]['shouldRun'].lower() == "true":
            await postResults(await register(userConfig[user]['classRegistration'][dayOfTheWeek]['24hr_start_time'], userConfig[user]['classRegistration'][dayOfTheWeek]['days_out'], users[idx].getSession(), users[idx].getDataToken(), users[idx].getUserId()))
        else:
            await postToChannel("<@" + str(userConfig[user]['discord']) + "> " + "registration for " + dayOfTheWeek.capitalize() + " classes is disabled", 'register_for_class_embed')

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

    elif (embedType == 'nightly_schedule_embed'):
        # Header
        embedMsg = discord.Embed(title=msg[0], description="__Any changes must be made before midnight__", color=int(configFile[embedType]['borderColor'], 16))

        # Thumbnail
        embedMsg.set_thumbnail(url=configFile[embedType]['thumbnail'])

        # list of all users to be tagged
        listOfUsers = ''

        # Message Body
        for message in msg[1:]:
            embedMsg.add_field(name="\u200B", value=message, inline=False)
            if '@' in message:
                # extract the user and add it to the list to be notified
                user = message.split(' - ')
                listOfUsers = listOfUsers + user[0] + ' '

        # Post messages
        await client.get_channel(configFile[embedType]['channel']).send('@everyone', delete_after=19740)
        await client.get_channel(configFile[embedType]['channel']).send(embed=embedMsg, delete_after=19740)
        #await client.get_channel(configFile[embedType]['channel']).send(listOfUsers)

    elif (embedType == 'schedule_request_embed'):
        # Header
        embedMsg = discord.Embed(title="", description=msg[0], color=int(configFile[embedType]['borderColor'], 16))

        # Thumbnail
        embedMsg.set_thumbnail(url=configFile[embedType]['thumbnail'])

        # list of all users to be tagged
        listOfUsers = ''

        # Message Body
        for message in msg[1:]:
            embedMsg.add_field(name="\u200B", value=message, inline=False)
            # extract the user and add it to the list to be notified
            user = message.split(' - ')
            listOfUsers = listOfUsers + user[0] + ' '

        # Post messages
        await client.get_channel(configFile[embedType]['channel']).send(embed=embedMsg, delete_after=600)
        #await client.get_channel(configFile[embedType]['channel']).send(listOfUsers)

    elif (embedType == 'register_for_class_embed'):
        await client.get_channel(configFile['channel_ids']['general']).send(msg, delete_after=43200)
        await client.get_channel(configFile['channel_ids']['general']).send('The above message will self-destruct at noon', delete_after=43200)

#---# All other posts
    else:
        await client.get_channel(configFile['channel_ids']['general']).send(msg, delete_after=600)

async def showSchedule(userId):
    with open('json/users/users.json') as f:
        userConfig = json.load(f)

    # Store the users schedule
    theSchedule = []

    # Schedule header
    theSchedule.append("<@" + str(userId) + "> Here is your schedule")
    # Schedule
    for user in userConfig: 
        # Match the requesting user
        if userId == userConfig[user]['discord']:
            # for each day of the week
            for day in userConfig[user]['classRegistration']:
                # if the day is enabled
                if userConfig[user]['classRegistration'][day]['shouldRun'].lower() == "true":
                    classTime = datetime.strptime(userConfig[user]['classRegistration'][day]['24hr_start_time'], "%H:%M").strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
                    theSchedule.append(day.capitalize() + " - " + classTime + '')
                else:
                    theSchedule.append(day.capitalize() + " - " + 'DISABLED')
    theSchedule.append("This message will self-destruct in 10 minutes")
    # Post it
    await postToChannel(theSchedule, 'schedule_request_embed')

#
# Bot Commands
#

# See your full schedule
@client.command()
async def schedule(ctx):
    await ctx.message.delete()

    with open('json/users/users.json') as f:
        userConfig = json.load(f)

    # Store the users schedule
    theSchedule = []

    # Schedule header
    theSchedule.append("<@" + str(ctx.message.author.id) + "> Here is your schedule")
    # Schedule
    for user in userConfig: 
        # Match the requesting user
        if ctx.message.author.id == userConfig[user]['discord']:
            # for each day of the week
            for day in userConfig[user]['classRegistration']:
                # if the day is enabled
                if userConfig[user]['classRegistration'][day]['shouldRun'].lower() == "true":
                    classTime = datetime.strptime(userConfig[user]['classRegistration'][day]['24hr_start_time'], "%H:%M").strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
                    theSchedule.append(day.capitalize() + " - " + classTime + '')
                else:
                    theSchedule.append(day.capitalize() + " - " + 'DISABLED')
    theSchedule.append("This message will self-destruct in 10 minutes")
    # Post it
    await postToChannel(theSchedule, 'schedule_request_embed')

# Schedule Monday
@client.command()
async def monday(ctx, *, time):
    await ctx.message.delete()

    # Store the og time request for the success message
    ogTime = time
    # Time is in 12 hour convert to 24 hour
    # Remove any spaces
    if ' ' in time:
        time = time.replace(' ','')

    classTime = datetime.strptime(time, "%I:%M%p").strftime("%H:%M")
    
    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration']['monday']['24hr_start_time'] = classTime

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> Monday at " + ogTime + ' has been scheduled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)

# Schedule Tuesday
@client.command()
async def tuesday(ctx, *, time):
    await ctx.message.delete()

    # Store the og time request for the success message
    ogTime = time
    # Time is in 12 hour convert to 24 hour
    # Remove any spaces
    if ' ' in time:
        time = time.replace(' ','')

    classTime = datetime.strptime(time, "%I:%M%p").strftime("%H:%M")
    
    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration']['tuesday']['24hr_start_time'] = classTime

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> Tuesday at " + ogTime + ' has been scheduled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)

# Schedule Wednesday
@client.command()
async def wednesday(ctx, *, time):
    await ctx.message.delete()

    # Store the og time request for the success message
    ogTime = time
    # Time is in 12 hour convert to 24 hour
    # Remove any spaces
    if ' ' in time:
        time = time.replace(' ','')

    classTime = datetime.strptime(time, "%I:%M%p").strftime("%H:%M")
    
    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration']['wednesday']['24hr_start_time'] = classTime

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> Wednesday at " + ogTime + ' has been scheduled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)

# Schedule Thursday
@client.command()
async def thursday(ctx, *, time):
    await ctx.message.delete()

    # Store the og time request for the success message
    ogTime = time
    # Time is in 12 hour convert to 24 hour
    # Remove any spaces
    if ' ' in time:
        time = time.replace(' ','')

    classTime = datetime.strptime(time, "%I:%M%p").strftime("%H:%M")
    
    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration']['thursday']['24hr_start_time'] = classTime

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> Thursday at " + ogTime + ' has been scheduled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)

# Schedule Friday
@client.command()
async def friday(ctx, *, time):
    await ctx.message.delete()

    # Store the og time request for the success message
    ogTime = time
    # Time is in 12 hour convert to 24 hour
    # Remove any spaces
    if ' ' in time:
        time = time.replace(' ','')

    classTime = datetime.strptime(time, "%I:%M%p").strftime("%H:%M")
    
    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration']['friday']['24hr_start_time'] = classTime

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> Friday at " + ogTime + ' has been scheduled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)

# Schedule Saturday
@client.command()
async def saturday(ctx, *, time):
    await ctx.message.delete()

    # Store the og time request for the success message
    ogTime = time
    # Time is in 12 hour convert to 24 hour
    # Remove any spaces
    if ' ' in time:
        time = time.replace(' ','')

    classTime = datetime.strptime(time, "%I:%M%p").strftime("%H:%M")
    
    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration']['saturday']['24hr_start_time'] = classTime

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> Saturday at " + ogTime + ' has been scheduled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)


# Disable a day
@client.command()
async def disable(ctx, dayToDisable):
    await ctx.message.delete()

    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration'][str(dayToDisable).lower()]['shouldRun'] = "false"

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> " + str(dayToDisable).lower() + ' has been disabled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)

# Enable a day
@client.command()
async def enable(ctx, dayToDisable):
    await ctx.message.delete()

    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['classRegistration'][str(dayToDisable).lower()]['shouldRun'] = "true"

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> " + str(dayToDisable).lower() + ' has been enabled! \n This message will self-destruct in 10 minutes', '')
    await showSchedule(ctx.message.author.id)

# Create a new user
@client.command()
async def createUser(ctx, *, name):
    await ctx.message.delete()

    # check if the user already exists
    doesUserExist = False

    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                doesUserExist = True

    if doesUserExist == False:
        newUser = {
            str(name): {
                "discord": ctx.message.author.id,
                "login": {
                "p360ppt": {
                    "email": "",
                    "password": ""
                },
                "mindbody": {
                    "password": "***REMOVED***",
                    "username": ""
                }
                },
                "classRegistration": {
                "monday": {
                    "shouldRun": "true",
                    "24hr_start_time": "16:30",
                    "days_out": "1"
                },
                "tuesday": {
                    "shouldRun": "true",
                    "24hr_start_time": "16:30",
                    "days_out": "1"
                },
                "wednesday": {
                    "shouldRun": "true",
                    "24hr_start_time": "16:30",
                    "days_out": "1"
                },
                "thursday": {
                    "shouldRun": "true",
                    "24hr_start_time": "16:30",
                    "days_out": "1"
                },
                "friday": {
                    "shouldRun": "true",
                    "24hr_start_time": "16:30",
                    "days_out": "1"
                },
                "saturday": {
                    "shouldRun": "true",
                    "24hr_start_time": "10:00",
                    "days_out": "1"
                }
                }
            }
        }

        userTemp.update(newUser)

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(userTemp, f)
        
        # Success
        await postToChannel("<@" + str(ctx.message.author.id) + "> (" + str(name) + ') the bot has added you to the database! \n This message will self-destruct in 10 minutes', '')
        #await showSchedule(ctx.message.author.id)
        await postToChannel("Please set your performace360 email and password using the .p360email and .p360password commands" + "\nAdditionally please set your mindbody email by using the .mindbodyemail command" + "\nIf you need help just message <@" + str(config['p360_admins']['talker9']) + ">\n These messages will self-destruct in 10 minutes", '')

    else:
        await postToChannel("Error - <@" + str(ctx.message.author.id) + "> you already have an account in database! \n This message will self-destruct in 10 minutes", '')

# Set the p360 email
@client.command()
async def p360email(ctx, email):
    await ctx.message.delete()

    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['login']['p360ppt']['email'] = email

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> your p360 email (" + str(email) + ') has been set! \n This message will self-destruct in 10 minutes', '')

# Set the p360 password
@client.command()
async def p360password(ctx, *, password):
    await ctx.message.delete()

    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['login']['p360ppt']['password'] = password

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> your password has been set! \n This message will self-destruct in 10 minutes", '')

# Set the mindbody email
@client.command()
async def mindbodyemail(ctx, email):
    await ctx.message.delete()

    filename = 'json/users/users.json'
    with open(filename, 'r') as f:
        userTemp = json.load(f)
        for user in userTemp:
            if ctx.message.author.id == userTemp[user]['discord']:
                userTemp[user]['login']['mindbody']['username'] = email

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(userTemp, f)
    
    # Success
    await postToChannel("<@" + str(ctx.message.author.id) + "> your mindbody email (" + str(email) + ') has been set! \n This message will self-destruct in 10 minutes', '')   

# test the active connection
@client.command()
async def test(ctx):
        # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)
    with open('json/users/users.json') as f:
        userConfig = json.load(f)
    with open('json/http/headers.json') as f:
        headersConfig = json.load(f)

    # Store the day of the week
    today  = datetime.now() + timedelta(days=1)
    dayMonthYear = today.strftime('%m/%d/%Y')
    dayOfTheWeek = today.strftime("%A").lower()

    numberOfDaysout = 1

    # Skip sunday (no classes)
    if dayOfTheWeek == 'sunday':
        numberOfDaysout = 2
        dayOfTheWeek = 'monday'

    # For each user
    for idx, user in enumerate(userConfig):        
        if (userConfig[user]['classRegistration'][dayOfTheWeek]['shouldRun'].lower() == "true") and (userConfig[user]['discord'] == 219983475833307136):
            await postResults(await register(userConfig[user]['classRegistration'][dayOfTheWeek]['24hr_start_time'], numberOfDaysout, users[idx].getSession(), users[idx].getDataToken(), users[idx].getUserId()))
        else:
            await postToChannel("<@" + str(userConfig[user]['discord']) + "> " + "- you cannot use this command", '')


# # Set the mindbody email
# @client.command()
# async def logmein(ctx):
#     await ctx.message.delete()

#     isUserLoggedIn = False

#     # Check if a session for this user already exists
#     for user in users:
#         print(user.getName())
#         for idx, user in enumerate(userConfig):
#             print(userConfig[idx])
#             if user.getName() == userConfig[idx]:
#                 isUserLoggedIn = True
    
#     # If not add the user to the user list
#     #for idx, user in enumerate(userConfig):

# # test a function
# @client.command()
# async def test(ctx):
#     await ctx.message.delete()
#     await registerForClass()

#
# Login
#

# Login and run the client with the provided token
client.run(config['discord_client']['token'])

# ---------------------------------------------------------------------

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

# #---# Get the daily update post
#     if '!du' in message.content.lower():
#         await asyncio.sleep(1)
#         await message.channel.send('Getting today\'s workout..')
#         await message.delete()
#         await postResults(await getDailyUpdate())
#         await message.channel.send('complete')
#         await asyncio.sleep(5)
#         await purgeChannel(config['channel_ids']['general'], 2)

# #---# Purge channels
#     if '!purge' in message.content.lower():
#         await asyncio.sleep(1)
#         await message.delete()
#         await purgeChannel(config['channel_ids']['general'], None)
#         #await purgeChannel(config['channel_ids']['workouts'], None)
#         #await purgeChannel(config['channel_ids']['motivation'], None)

# #---# Register for a class
#     if '!reg' in message.content.lower():
#         await asyncio.sleep(1)
#         await message.delete()

#         # Load the config file
#         with open('json/config.json') as f:
#             configFile = json.load(f)
#         with open('json/users/users.json') as f:
#             userConfig = json.load(f)
#         with open('json/http/headers.json') as f:
#             headersConfig = json.load(f)

#         for idx, user in enumerate(userConfig):        
#             if userConfig[user]['classRegistration']['monday']['shouldRun'].lower() == "true":
#                 await postResults(await register(userConfig[user]['classRegistration']['monday']['24hr_start_time'], userConfig[user]['classRegistration']['monday']['days_out'], users[idx].getSession(), users[idx].getDataToken(), users[idx].getUserId()))
#             else:
#                 await postToChannel("<@" + str(userConfig[user]['discord']) + "> " + "registration for Monday classes is disabled", '')

# #---# Get the class schedules
#     if '!sched' in message.content.lower():
#         await asyncio.sleep(1)
#         await message.delete()
#         # await postResults(await getSchedule())
#         # await postToChannel('', 'schedule_embed')
#         await announceSchedule()
