# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json
from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+17372508034",
    to="whatsapp:+917355628489",
    content_sid="HXfe5ab5f00277942d4d4200328b4d403c",
    body="bring an umbrella"
)

print(message.body)
