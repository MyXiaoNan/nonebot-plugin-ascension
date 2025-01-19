from pydantic import BaseModel


class Sect(BaseModel):
    """宗门"""

    position: str
    """职位"""
    max_exp: int
    """完成任务获取的修为上限"""
