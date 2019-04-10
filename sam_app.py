from flask import Flask, request, url_for, redirect, render_template
from gcal import addEvent
from twilio.twiml.messaging_response import Message, MessagingResponse
import models
import settings
import json #used to convert dictionary object to json for calendar creation
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('calendar'))
    return render_template('index.html')



@app.route("/calendar", methods=['GET', 'POST'])
def calendar():
    if request.method == 'POST':
        createEvent()
    return render_template('calendar.html')

#TODO: handle tomorrow and today
@app.route("/sms", methods=['GET','POST'])
def createEvent():
    resp = MessagingResponse()
    dayIndex = None
    textBody = str(request.values.get('Body', None)).split()

    if not textBody: return "ERROR"

    for i in range(len(textBody)):
        if textBody[i].lower() in settings.DAY_OF_WEEK:
            dayIndex = i
            break

    summary = ' '.join(textBody[:dayIndex])
    day = textBody[dayIndex]
    eventTime = textBody[dayIndex+1].split('-') #TODO make times flexible
    start,end = eventTime[0],eventTime[1]

    e = models.CalEvent()
    e.setSummary(summary)
    e.setTime(day,start,end)
    addEvent(e.event)
    print("OK, I've created an event: " + summary + " for " + day + " "+ start + ' to ' + end + '.')
    resp.message("OK, I've created an event: " + summary + " for " + day + " "+ start + ' to ' + end + '.')
    return str(resp)

@app.route("/testPoint", methods=['POST'])
def testPoint():

    textBody = str(request.get_data()).split()
    print(textBody)
    if not textBody:
        return

    dayIndex = None

    for i in range(len(textBody)):
        if textBody[i].lower() in settings.DAY_OF_WEEK:
            dayIndex = i
            break

    summary = ' '.join(textBody[:dayIndex])
    day = textBody[dayIndex]
    eventTime = textBody[dayIndex+1].split('-')
    start,end = eventTime[0],eventTime[1]

    e = models.CalEvent()
    e.setSummary(summary)
    e.setTime(day,start,end)
    addEvent(e.event)
    print("OK, I've created an event: " + summary + " for " + day + " "+ start + ' to ' + end + '.')
    return "OK"

@app.route("/sms_test", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()
    textBody = str(request.values.get('Body', None)).split()
    print(textBody)
    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")

    # Add a picture message
    return 'ok'
if __name__ == "__main__":
    app.run()