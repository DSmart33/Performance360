# Import the discord library
import json
import asyncio
import requests
from datetime import datetime, timezone, timedelta

async def register(startTime, daysOut):
    # Load the config file
    with open('json/config.json') as f:
        configFile = json.load(f)

    # Create the result to return
    result = []
    
    # Create the session
    with requests.session() as s:

        # P360ppt Login
        p360_payload = {
            "email": "***REMOVED***", 
            "password": "***REMOVED***"
        }
        p360_headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Content-Length': '66',
            'Host': 'p360ppt.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.10.0'
        }
        r = s.post("https://p360ppt.com/granjur/api/auth/login", json=p360_payload, headers=p360_headers)
        json_data = json.loads(r.text)
        token = json_data['data']['token']

        with open('json_data1.json', 'w') as outfile:
            json.dump(json_data, outfile)

        # P360ppt Mind-Body Login
        mindBody_payload = {
            "password": "***REMOVED***",
            "username": "***REMOVED***"
        }
        mindbody_headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Content-Length': '59',
            'Host': 'p360ppt.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.10.0'
        }
        MindBodyLogin = s.post("https://p360ppt.com/granjur/api/auth/mind-body/get-client-id?token=" + token, json=mindBody_payload, headers=mindbody_headers)
        json_data = json.loads(MindBodyLogin.text)
        
        with open('json_data.json', 'w') as outfile:
            json.dump(json_data, outfile)
        
        userID = json_data['data']['ID']

        print(userID)
        
    #     # Get tomorrows date
    #     tomorrowsDate = datetime.now().date() + timedelta(days=int(daysOut))
        
    #     # P360 Mind-Body get classes
    #     classes_payload = {
    #         "Waitlist": False, 
    #         "end_date": str(tomorrowsDate),
    #         "start_date": str(tomorrowsDate),
    #         "userID": userID
    #     }
    #     classes_headers = {
    #         'Content-Type': 'application/json; charset=UTF-8',
    #         'Content-Length': '89',
    #         'Host': 'p360ppt.com',
    #         'Connection':'Keep-Alive',
    #         'Accept-Encoding': 'gzip',
    #         'User-Agent': 'okhttp/3.10.0'
    #     }
    #     MindBodyClasses = s.post("https://p360ppt.com/granjur/api/auth/mind-body/get-classes?token=" + token, json=classes_payload, headers=classes_headers)
    #     json_data = json.loads(MindBodyClasses.text)

    #     # Store the pb classes
    #     pbClasses = []

    #     for workoutClass in json_data['data']['classes']:
    #         if workoutClass['ClassDescription']['Name'] == 'PSC: Pacific Beach':
    #             pbclass = {
    #                 "class sched id": workoutClass['ClassScheduleID'],
    #                 "class id": workoutClass['ID'],
    #                 "maxcapacity": workoutClass['MaxCapacity'],
    #                 "# booked": workoutClass['TotalBooked'],
    #                 "# waitlisted": workoutClass['TotalBookedWaitlist'],
    #                 "Start time": workoutClass['StartDateTime'],
    #                 "instructor": workoutClass['Staff']['Name']
    #             }
    #             pbClasses.append(pbclass)

    #     # Sort the classes in order of start time
    #     pbClasses = sorted(
    #         pbClasses,
    #         key=lambda x: datetime.strptime(x['Start time'], '%Y-%m-%dT%H:%M:%S'), reverse=False
    #     )
        
    #     # Look for the desired class
    #     for pbclass in pbClasses:
    #         # Match the time
    #         if 'T' + startTime + ':00' in pbclass['Start time']:

    #                 # Subscribe to 4:30 class
    #                 subscribe_payload = {
    #                     'Waitlist': False, 
    #                     'classIDs': [pbclass['class id']],
    #                     'userID': userID
    #                 }
    #                 subscribe_headers = {
    #                     'Content-Type': 'application/json; charset=UTF-8',
    #                     'Content-Length': '59',
    #                     'Host': 'p360ppt.com',
    #                     'Connection':'Keep-Alive',
    #                     'Accept-Encoding': 'gzip',
    #                     'User-Agent': 'okhttp/3.10.0'
    #                 }
    #                 isSubscribed = s.post("https://p360ppt.com/granjur/api/auth/mind-body/class-subscribe?token=" + token, json=subscribe_payload, headers=subscribe_headers)
    #                 json_data = json.loads(isSubscribed.text)

    #                 # Save the response
    #                 result.append({"data":"<@" + str(configFile['p360_admins']['talker9']) + "> " + json_data['data']['message'], "embed":""})

    #                 # Close the session
    #                 s.close()

    # # Return the result
    # return result
