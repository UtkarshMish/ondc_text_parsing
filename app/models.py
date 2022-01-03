from typing import Dict, Optional

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
        intent: Optional[Dict[Dict[str, any]]]
        fulfillment: Optional[Dict[Dict[str, any]]]

    context: ContextType
    message: MessageType
