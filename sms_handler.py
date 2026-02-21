import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')


def send_quote_sms(phone, name, service, price):
    
    try:
    
      client = Client(SID, AUTH_TOKEN)
      body=f"Hi {name}! , it's Sam here from the plumbing team. "
      f"Just confirming your quote of ${price} for the {service}. "
      f"Reply BOOK to schedule if you haven't done so already."
      
      message = client.messages.create(
            body=body,
            from_=TWILIO_NUMBER,
            to=phone
      )
      print(f"✅ SMS Sent! SID: {message.sid}")
    except Exception as e:
        # Ruthless error catching: This will tell you if your number isn't verified
        print(f"❌ Twilio Error: {e}")
    
