from pydantic import BaseModel


class Rift(BaseModel):
    """秘境"""

    name: str
    rank: int
    rate: int
    count: int
    duration: int
