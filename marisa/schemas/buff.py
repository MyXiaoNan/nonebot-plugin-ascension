from typing import Literal

from pydantic import Field, BaseModel

from marisa.schemas.enums import BuffType


class Buff(BaseModel):
    """增益效果"""

    type: BuffType
    """类型"""
    calc: Literal["add", "mul"]
    """
    计算方式
        - `add`: 加法
        - `mul`: 乘法
    """
    value: float
    """数值"""
    duration: int = Field(-1)
    """持续时间"""
    state: Literal["active", "inactive"] = Field("inactive")
    """状态"""

    @property
    def desc(self):
        duration = f"在 {self.duration}s 内" if self.duration != -1 else ""
        unit = "点" if self.calc == "add" else "%"
        return duration + f"{self.type.value} + {self.value}{unit}"
