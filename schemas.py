from pydantic import BaseModel
from typing import List, Optional

# Data incoming from the Vapi payload. We need to match this structure to parse it correctly.
class ToolFunction(BaseModel):
    name : str
    arguments: dict
    
class ToolCall(BaseModel):
    id: str
    function: ToolFunction
    
class VapiMessage(BaseModel):
    type: str
    toolCalls: Optional[List[ToolCall]] = None 

class VapiPayload(BaseModel):
    message: VapiMessage
    
