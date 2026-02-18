# 🤖 AI Voice Receptionist
A high-leverage, low-latency voice agent system designed to automate lead qualification, capture, and dynamic pricing for service-based businesses.

## 🛠️ System Architecture
- **Inbound Voice Processing: Vapi.ai handles real-time transcription and intent detection.**
- **Secure Webhook Layer: FastAPI receives structured JSON payloads via a secure ngrok tunnel.**
- **Data Validation: Pydantic models enforce strict schema validation, ensuring no data corruption.**
- **Logic & Intelligence: A Python-based engine performs keyword matching and intent classification to handle natural language variations (e.g., "clogged pipe" vs "sewer clog").**
- **Data Persistence: Integrated SQLite3 database captures and stores lead metadata (Name, Phone, Service, Price) for CRM integration.**
- **Voice Synthesis: Structured results are returned to Vapi for sub-1-second response delivery.**

## Technical Stack
- **Backend:** FastAPI (Python 3.10+)
- **Database:** SQLite3 (Local Persistence)
- **Tunneling:** ngrok (Secure Global Exposure)
- **AI Engine:** Vapi.ai (Function Calling & Latency Management)
- **Validation:** Pydantic for strict runtime data validation and schema enforcement.

## Key Features & Edge Case Handling
- **Dynamic Pricing Engine: A dictionary-based lookup system with $O(1)$ complexity for instant price retrieval.**
- **Graceful Fallbacks: Logic-gate implementation for "Unknown Services," directing users to custom quotes rather than returning system errors.**
- **Asynchronous Processing: Built with async def to ensure the voice conversation remains fluid without blocking threads.**
- **Keyword Logic: Implements partial string matching to retrieve the price based on specific keyword/service name from the user's statement.**
- **Mandatory Lead Capture: Logic-gate architecture ensures no price is provided until user contact info is validated and stored.**


## 🚀 Execution Commands

### 1. Environment Setup
```bash
python -m venv venv
# Windows:
.\\venv\\Scripts\\Activate.ps1
# Mac:
source venv/bin/activate
pip install fastapi uvicorn pydantic

# Run once to set up the leads table
python database.py

2. Fire Up the Backend
uvicorn main:app --reload

3. Launch Ngrok Tunnel
ngrok http 8000
