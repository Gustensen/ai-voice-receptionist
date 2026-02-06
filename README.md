# 🤖 AI Voice Receptionist (HVAC/Plumbing)
A high-leverage voice agent system built to automate lead qualification and pricing for local trades.

## 🛠️ System Architecture
- **Backend:** FastAPI (Python 3.10+)
- **Tunneling:** ngrok (Secure Global Exposure)
- **AI Brain:** Vapi.ai (Function Calling & Latency Management)

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
