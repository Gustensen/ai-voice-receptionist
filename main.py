# We import FastAPI to build the server and "app" to initialize it.
from fastapi import FastAPI, Header, HTTPException
from schemas import VapiPayload

app = FastAPI()

# A 'GET' route for a health check. This tells us the server is "alive".
@app.get("/")
def health_check():
    return {"status": "AI Receptionist Online"}

# A 'POST' route because the AI (Vapi) will "SEND" us data to process.
# We use Type Hinting to ensure the AI doesn't send junk.
@app.post("/check-price")
async def handle_vapi_tool_call(payload: VapiPayload, x_vapi_secret: str = Header(None)):

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
        price = pricing_sheet.get(service)

        # New Keyword Matching logic with negative handling
        price = None
        matched_keyword = None
        #negation_words = ["no", "not", "don't", "dont", "wasn't", "wont"]
        #words = service.split()
        
        for keyword in pricing_sheet:
            if keyword in service:
                # Check for 3 words before the keyword for negation
                #keyword_parts = words(keyword)[0].split()
                #recent_context = keyword_parts[-3:]  # Get the last 3 words before the keyword
                #if any(neg in recent_context for neg in negation_words):
                    #print(f"Negation found near {keyword}, skipping...")
                    #continue  # Skip this keyword if negation is found
                
                price = pricing_sheet[keyword]
                matched_keyword = keyword
                break
        
        
        if price:
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