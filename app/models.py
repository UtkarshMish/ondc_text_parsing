from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class BecknResponse(BaseModel):
    class ContextType(BaseModel):
        domain: str
        country: str
        city: str
        action: str
        core_version: str
        bap_id: str
        bpp_uri: str
        transaction_id: str
        message_id: str
        timestamp: str

    class MessageType(BaseModel):
        intent: Optional[List[Dict[str, Any]]]
        fulfillment: Optional[List[Dict[str, Any]]]

    context: ContextType
    message: MessageType
