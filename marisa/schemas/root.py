from pydantic import BaseModel

from marisa.schemas.buff import Buff


class Root(BaseModel):
    """灵根"""

    name: str
    type: list[str]
    buff: Buff
    count: int
