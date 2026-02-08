# 🤖 AI Voice Receptionist
A high-leverage voice agent system built to automate lead qualification and pricing for local trades.

## 🛠️ System Architecture
-User speaks to the AI.
-Vapi transcribes the voice and detects a "Tool Call" intent.
-Vapi sends a POST request with a nested JSON payload.
-FastAPI validates the payload via Pydantic.
-Logic Engine calculates the price and returns a structured response.
-Vapi speaks the price back to the User in under 1 second.

## Technical Stack
- **Backend:** FastAPI (Python 3.10+)
- **Tunneling:** ngrok (Secure Global Exposure)
- **AI Brain:** Vapi.ai (Function Calling & Latency Management)
- **Validation:** Pydantic for strict runtime data validation and schema enforcement.

## Key Features & Edge Case Handling
- Dynamic Pricing Engine: A dictionary-based lookup system with $O(1)$ complexity for instant price retrieval.
- Graceful Fallbacks: Logic-gate implementation for "Unknown Services," directing users to custom quotes rather than returning system errors.
- Asynchronous Processing: Built with async def to ensure the voice conversation remains fluid without blocking threads.

## Challenges & Solutions
-Problem: ngrok Free Tier browser warnings causing HTTP 401 errors for the AI Agent.
-Solution: Implemented the ngrok-skip-browser-warning header within the Vapi Tool configuration to allow seamless machine-to-machine communication.


## 🚀 Execution Commands

### 1. Environment Setup
```bash
python -m venv venv
# Windows:
.\\venv\\Scripts\\Activate.ps1
# Mac:
source venv/bin/activate
pip install fastapi uvicorn


2. Fire Up the Backend
Bash
uvicorn main:app --reload

3. Launch Secure Tunnel
Bash
ngrok http 8000 --basic-auth "username:password"
