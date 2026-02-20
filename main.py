# We import FastAPI to build the server and "app" to initialize it.
from fastapi import FastAPI, Header, HTTPException, BackgroundTasks
from sms_handler import send_quote_sms
from schemas import VapiPayload
from database import save_lead

app = FastAPI()

# A 'GET' route for a health check. This tells us the server is "alive".
@app.get("/")
def health_check():
    return {"status": "AI Receptionist Online"}

# A 'POST' route because the AI (Vapi) will "SEND" us data to process.
# We use Type Hinting to ensure the AI doesn't send junk.
@app.post("/check-price")
async def handle_vapi_tool_call(payload: VapiPayload, background_tasks: BackgroundTasks, x_vapi_secret: str = Header(None)):

    # 1. Skip security for non-tool calls (Status updates, etc.)
    if payload.message.type != "tool-calls":
        return {"status": "success"}

    # 2. Strict Security for actual Tool Calls
    if x_vapi_secret != "plumber123":
        print(f"BLOCKING: Secret was {x_vapi_secret}")
        raise HTTPException(status_code=401)
    # 3. Extract the data using the RAW structure we just saw
    try:
        
        if not payload.message.toolCalls:
             return {"results": []}

        tool_call = payload.message.toolCalls[0]
        tool_call_id = tool_call.id
        
        # Vapi sends arguments as a dictionary already in this version!
        service = tool_call.function.arguments.get("service_name", "").lower()

        pricing_sheet = {"leak": 150, "clog": 200, "heater": 500}

        # Keywords to check for in the service description
        price = None
        matched_keyword = None
        
        
        for keyword in pricing_sheet:
            if keyword in service:
                price = pricing_sheet[keyword]
                matched_keyword = keyword
                break
        
        
        if price:
            # Grab the extra info Sam collected
            customer_name = tool_call.function.arguments.get("name", "Unknown")
            customer_phone = tool_call.function.arguments.get("phone", "Unknown")
            
            # SAVE TO DATABASE
            save_lead(customer_name, customer_phone, service, price)
            # Trigger SMS (Background - doesn't block the voice!)
            background_tasks.add_task(send_quote_sms, customer_phone, customer_name,service ,price)
            result = f"The price for fixing that {matched_keyword} is ${price}."
        else:
            result = "I'll need to have a technician provide a custom quote for that specific issue."

        return {
            "results": [
                {
                    "toolCallId": tool_call_id,
                    "result": result
                }
            ]
        }
    except Exception as e:
        print(f"Logic Error: {e}")
        return {"error": "Failed to process tool call"}, 500