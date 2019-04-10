import settings
from datetime import timedelta
class User(object):
    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone

class CalEvent(object):
    def __init__(self, timeZone = 'America/New_York'):
        self.event = {
            'summary': None,
            'location': None,
            'description': None,
            'start': {
                'dateTime': None,
                'timeZone': timeZone,
            },
            'end': {
                'dateTime': None,
                'timeZone': timeZone,
            },
            'attendees': [
                {'email': None}
            ]
        }
    def setSummary(self, text):
        self.event['summary'] = text

    def setTime(self,day,start,end):
        date = self.findDate(day)
        start = self.convertTo24(start)
        end = self.convertTo24(end)

        start = date + "T" + start
        end = date + "T" + end

        self.event['start'['dateTime']] = start
        self.event['end'['dateTime']] = end

    def findDate(self,day): #accounts for weekday in english
        day = day.lower()
        weekday = -1
        if day == 'monday':
            weekday = 0
        elif day == 'tuesday':
            weekday = 1
        elif day == 'wednesday':
            weekday = 2
        elif day == 'thursday':
            weekday = 3
        elif day == 'friday':
            weekday = 4
        elif day == 'saturday':
            weekday = 5
        elif day == 'sunday':
            weekday = 6
        if weekday == -1:
            return "ERROR: INVALID DAY"

        dayOffset = 0
        if weekday == settings.CURRENT_DAY:
            dayOffset = 7
        elif weekday < settings.CURRENT_DAY:
            dayOffset = weekday - settings.CURRENT_DAY
        elif weekday > settings.CURRENT_DAY:
            dayOffset = 7 + weekday

        date = settings.CURRENT_DATE - timedelta(days=dayOffset)
        date = date.date()
        return str(date)
    def convertTo24(self, time):
        time = time.replace(':', ' ').split()
        if len(time) > 1:
            hour, minute = time[0], time[1][:2]
        else:
            if len(time[0]) == 1:
                hour = '0' + time[0]
            else:
                hour = time[0]

        if len(time) == 3: #check PM
            if time[2].lower() == 'pm' and hour != '12':
                hour = str(int(hour) + 12)
        formatted = hour + ":" + minute + ":00"
        return formatted






