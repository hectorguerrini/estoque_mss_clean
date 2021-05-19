from pydantic import BaseModel
from typing import Optional, Any


class HttpResponse(BaseModel):
    statusCode: int
    body: Any


class HttpRequest(BaseModel):
    body: Optional[Any]
