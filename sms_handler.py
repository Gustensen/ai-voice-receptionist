import os

def send_quote_sms(phone, name, service, price):
    # For now, we simulate the logic. 
    # Soon, we will plug in Twilio here.
    print(f"--- OUTGOING SMS ---")
    print(f"To: {phone}")
    print(f"Message: Hi {name}! , it's Sam here from the plumbing team. "
          f"Just confirming your quote of ${price} for the {service}. "
          f"Reply BOOK to get started if you haven't already made an appointment!")
    print(f"--------------------")
    
