from pydantic import BaseModel
from typing import List, Optional

class Component(BaseModel):
    name: str
    version: Optional[str] = None
    license: Optional[str] = None

class SBOMRequest(BaseModel):
    components: List[Component]
