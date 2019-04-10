import settings
from datetime import timedelta
import re
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
            }
        }
    def setSummary(self, text):
        self.event['summary'] = text

    def setTime(self,day,start,end):
        date = self.findDate(day)
        start = self.convertTo24(start)
        end = self.convertTo24(end)

        start = date + "T" + start
        end = date + "T" + end

        self.event['start']['dateTime'] = start
        self.event['end']['dateTime'] = end

    def findDate(self,day): #accounts for weekday in english
        day = day.lower()
        weekday = settings.DAY_OF_WEEK.index(day)

        dayOffset = 0
        if weekday == settings.CURRENT_DAY:
            dayOffset = 7
        elif weekday < settings.CURRENT_DAY:
            dayOffset = weekday+(7-settings.CURRENT_DAY)
        elif weekday > settings.CURRENT_DAY:
            dayOffset = weekday - settings.CURRENT_DAY

        print(dayOffset)
        date = settings.CURRENT_DATE + timedelta(days=dayOffset)
        print(date)
        return str(date)
    def convertTo24(self, time):
        time = time.lower()
        pm = False
        if 'pm' in time:
            pm = True

        time = time.replace(':', ' ').split()
        for i in range(len(time)):
            time[i] = re.sub("[^0-9]", "", time[i])

        print(time)

        hour,minute = '00','00'

        if len(time) > 1:
            hour, minute = time[0], time[1][:2]
        else:
            if len(time[0]) == 1:
                hour = '0' + time[0]
            else:
                hour = time[0]

        if pm and hour != '12':
            hour = str(int(hour) + 12)
        formatted = hour + ":" + minute + ":00"
        return formatted






