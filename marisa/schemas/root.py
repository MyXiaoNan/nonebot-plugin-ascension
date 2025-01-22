from pydantic import BaseModel

from marisa.schemas.buff import Buff


class Root(BaseModel):
    """灵根"""

    name: str
    type: str | list[str]
    count: int
    buff: list[Buff]
