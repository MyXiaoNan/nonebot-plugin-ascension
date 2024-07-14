from pydantic import BaseModel


class SectPosition(BaseModel):
    """宗门职务"""

    title: str
    speeds: str
    max_exp: int
