# We import FastAPI to build the server and "app" to initialize it.
from fastapi import FastAPI, Header, HTTPException
from schemas import VapiPayload
import json

app = FastAPI()

# A 'GET' route for a health check. This tells us the server is "alive".
@app.get("/")
def health_check():
    return {"status": "AI Receptionist Online"}

# A 'POST' route because the AI (Vapi) will "SEND" us data to process.
# We use Type Hinting to ensure the AI doesn't send junk.
@app.post("/check-price")
async def handle_vapi_tool_call(payload: VapiPayload, x_vapi_secret: str = Header(None)):
    if x_vapi_secret != "your-super-long-random-string":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    tool_call = payload.message.toolCallList[0]  
    
    # Unwrap the arguments
    args = json.loads(tool_call.function.arguments)
    # Get the service name  and Default to empty string if not provided
    service = args.get("service_name", "").lower()  

    # Pricing Database: A simple dictionary to hold our service prices.
    pricing_sheet = {
        "leak": 150, 
        "clog": 200, 
        "heater": 500
    }
    
    # Lookup Logic
    price = pricing_sheet.get(service)
    
    # Logic Gate: If price exists, return it. If not, give a fallback.
    if price:
        response_sheet = f"The price for fixing that {service} is ${price}."
    else:
        response_sheet = "I'll need to have a technician provide a custom quote for that specific issue."
        
    # Return the response in a format Vapi expects with the associated call id and response for that call.
    return {
        "results" :[
            {
                "toolCallId": tool_call.id,
                "result": response_sheet
            }
        ]
    }