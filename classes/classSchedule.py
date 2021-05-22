# Import the discord library
import json
import asyncio
import requests
from datetime import datetime, timezone, timedelta
import calendar

async def getSchedule():
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
        userID = json_data['data']['ID']
        
        # Get todays date
        todaysDate = datetime.now().date()

        # P360 Mind-Body get classes
        classes_payload = {
            "Waitlist": False, 
            "end_date": str(todaysDate + timedelta(days=7)),
            "start_date": str(todaysDate),
            "userID": userID
        }
        classes_headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Content-Length': '89',
            'Host': 'p360ppt.com',
            'Connection':'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.10.0'
        }
        MindBodyClasses = s.post("https://p360ppt.com/granjur/api/auth/mind-body/get-classes?token=" + token, json=classes_payload, headers=classes_headers)
        json_data = json.loads(MindBodyClasses.text)

        # Store the pb classes
        pbClasses = []
        obClasses = []
        bpClasses = []

        for workoutClass in json_data['data']['classes']:
            # Pacific Beach
            if workoutClass['ClassDescription']['Name'] == 'PSC: Pacific Beach':
                pbclass = {
                    "Location": workoutClass['ClassDescription']['Name'],
                    "class sched id": workoutClass['ClassScheduleID'],
                    "class id": workoutClass['ID'],
                    "maxcapacity": workoutClass['MaxCapacity'],
                    "# booked": workoutClass['TotalBooked'],
                    "# waitlisted": workoutClass['TotalBookedWaitlist'],
                    "Start time": workoutClass['StartDateTime'],
                    "instructor": workoutClass['Staff']['Name'],
                    "regId":0
                }
                pbClasses.append(pbclass)

            # Ocean Beach
            if workoutClass['ClassDescription']['Name'] == 'PSC: Ocean Beach':
                obClass = {
                    "Location": workoutClass['ClassDescription']['Name'],
                    "class sched id": workoutClass['ClassScheduleID'],
                    "class id": workoutClass['ID'],
                    "maxcapacity": workoutClass['MaxCapacity'],
                    "# booked": workoutClass['TotalBooked'],
                    "# waitlisted": workoutClass['TotalBookedWaitlist'],
                    "Start time": workoutClass['StartDateTime'],
                    "instructor": workoutClass['Staff']['Name'],
                    "regId":0
                }
                obClasses.append(obClass)

            # Bay Park
            if workoutClass['ClassDescription']['Name'] == 'PSC: Bay Park':
                bpClass = {
                    "Location": workoutClass['ClassDescription']['Name'],
                    "class sched id": workoutClass['ClassScheduleID'],
                    "class id": workoutClass['ID'],
                    "maxcapacity": workoutClass['MaxCapacity'],
                    "# booked": workoutClass['TotalBooked'],
                    "# waitlisted": workoutClass['TotalBookedWaitlist'],
                    "Start time": workoutClass['StartDateTime'],
                    "instructor": workoutClass['Staff']['Name'],
                    "regId":0
                }
                bpClasses.append(bpClass)

        # Sort the classes in order of start time
        pbClasses = sorted(
            pbClasses,
            key=lambda x: datetime.strptime(x['Start time'], '%Y-%m-%dT%H:%M:%S'), reverse=False
        )
        obClasses = sorted(
            obClasses,
            key=lambda x: datetime.strptime(x['Start time'], '%Y-%m-%dT%H:%M:%S'), reverse=False
        )
        bpClasses = sorted(
            bpClasses,
            key=lambda x: datetime.strptime(x['Start time'], '%Y-%m-%dT%H:%M:%S'), reverse=False
        )

        # Create a registration id
        pbReg= 1
        obReg= 1
        bpReg= 1
        for wkClass in pbClasses:
            wkClass['regId'] = 'pb-'+ str(pbReg)
            pbReg+=1
        for wkClass in obClasses:
            wkClass['regId'] = 'ob-'+ str(obReg)
            obReg+=1
        for wkClass in bpClasses:
            wkClass['regId'] = 'bay-'+ str(bpReg)
            bpReg+=1

        # Group classes by day
        pbClassesByDay = {}

        for wkClass in pbClasses:
            # Get the day of the week
            dayofWeek = calendar.day_name[datetime.strptime(wkClass['Start time'], '%Y-%m-%dT%H:%M:%S').weekday()].lower()

            # If day of week exists
            if hasattr(pbClassesByDay, dayofWeek):
                pbClassesByDay[dayofWeek].append(wkClass)
            # If day of week doesn't exist
            else:
                pbClassesByDay[dayofWeek] = wkClass
        
        print(pbClassesByDay['monday'])
        # Group classes by day
        obClassesByDay = {
            "monday":[],
            "tuesday":[],
            "wednesday":[],
            "thursday":[],
            "friday":[],
            "saturday":[],
            "sunday":[]
        }
        for wkClass in obClasses:
            # Get the day of the week
            dayofWeek = calendar.day_name[datetime.strptime(wkClass['Start time'], '%Y-%m-%dT%H:%M:%S').weekday()].lower()
            obClassesByDay[dayofWeek].append(wkClass)

        # Group classes by day
        bpClassesByDay = {
            "monday":[],
            "tuesday":[],
            "wednesday":[],
            "thursday":[],
            "friday":[],
            "saturday":[],
            "sunday":[]
        }
        for wkClass in bpClasses:
            # Get the day of the week
            dayofWeek = calendar.day_name[datetime.strptime(wkClass['Start time'], '%Y-%m-%dT%H:%M:%S').weekday()].lower()
            bpClassesByDay[dayofWeek].append(wkClass)
            
        # Dump the information to the json file
        with open('json/classes_pb.json', 'w') as outfile:
            json.dump(pbClassesByDay, outfile)
        with open('json/classes_ob.json', 'w') as outfile:
            json.dump(obClassesByDay, outfile)
        with open('json/classes_bp.json', 'w') as outfile:
            json.dump(bpClassesByDay, outfile)
        
        result.append({'data':'Fetched classes', 'embed':''})

        # Close the session
        s.close()
    
    # Return the result
    return result
