import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACC_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN']
# TYpically the sandbox number assigned
send_from = os.environ['TWILIO_SEND_FROM']
# Typically list of numbers allowed to link to sandbox
send_to= os.environ['TWILIO_SEND_TO_LIST']


client = Client(account_sid, auth_token)


def whatsappnotify(event, context):
    print(event); #Write to CLoudwatch log streams
    print(send_to)
    message = client.messages.create(body="An event has occured. Cause: {} ".format(event['detail']['Cause']),from_= send_from,to = send_to)
    return
