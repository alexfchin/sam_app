from flask import Flask, request, url_for, redirect, render_template
from gcal import createEvent
from twilio.twiml.messaging_response import Message, MessagingResponse
import models
from flask_sqlalchemy_core import FlaskSQLAlchemy
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

@app.route("/createEvent", methods=['POST'])
def createEvent():
    messageResponse = MessagingResponse()
    textBody = str(request.values.get('Body', None))
    eventName = ''
    eventTime = ''
    #handle today, tomorrow

    messageResponse.message("OK, I've created an event: " + eventName + " for " + eventTime)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    # The text to translate
    # The target language

    resp = MessagingResponse()
    text = str(request.values.get('Body', None))
    print(text)

    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))

    # doctor, clinic

    if 'hello' in text:
        resp.message("You need a doctor")
    # Add a message
    return str(resp)

if __name__ == "__main__":
    app.run()