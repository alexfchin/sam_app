from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import settings

from datetime import datetime, timedelta

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    GMT_OFF = '-04:00'
    event = {
        'summary': 'Dinner with friends',
        'description': None,
        'start': {
            'dateTime':'2019-04-10T19:00:00',
            'timeZone': 'America/New_York',},
        'end': {
            'dateTime': '2019-04-10T20:00:00',
            'timeZone': 'America/New_York',
        }
    }

    #
    # event = service.events().insert(calendarId='primary', body=event).execute()
    # #
    # print('Event created: %s' % event.get('htmlLink'))
    #
    dt = datetime.now()
    td = timedelta(days=4)
    # your calculated date
    print(td)
    print(type(td))
    my_date = dt + td
    print(str(my_date.date()))
    print(type(my_date))
if __name__ == '__main__':
    main()

# import json
#
# data = {}
# data['key'] = 'value'
# json_data = json.dumps(data)