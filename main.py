# 1. We import FastAPI to build the server and "app" to initialize it.
from fastapi import FastAPI

app = FastAPI()

# 2. A 'GET' route for a health check. This tells us the server is "alive".
@app.get("/")
def health_check():
    return {"status": "AI Receptionist Online"}

# 3. A 'POST' route because the AI (Vapi) will "SEND" us data to process.
# We use Type Hinting (service_name: str) to ensure the AI doesn't send junk.
@app.post("/check-price")
def get_service_price(service_name: str):
    
    # 4. We store prices in a Dictionary for easy lookup.
    # Keys are lowercase to make searching easier.
    prices = {
        "leak": 150, 
        "clog": 200, 
        "heater": 500
    }
    
    # 5. We use .get() instead of prices[service_name]. 
    # Why? If the service isn't found, .get() returns "None" instead of crashing.
    result = prices.get(service_name.lower())
    
    # 6. Logic Gate: If price exists, return it. If not, give a fallback.
    if result:
        return {"price": f"${result}", "found": True}
    else:
        return {"price": "Custom quote needed", "found": False}