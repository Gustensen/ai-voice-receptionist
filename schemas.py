from pydantic import BaseModel
from typing import List, Dict, Any

# Data incoming from the Vapi payload. We need to match this structure to parse it correctly.
class FunctionCall(BaseModel):
    name : str
    arguments:str
    
class ToolCall(BaseModel):
    id: str
    type: str
    function: FunctionCall
    
class Message(BaseModel):
    toolCallList: List[ToolCall]
    
class VapiPayload(BaseModel):
    message: Message
    
