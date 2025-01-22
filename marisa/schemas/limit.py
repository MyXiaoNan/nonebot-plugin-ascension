from pydantic import Field, BaseModel

from marisa.schemas.enums import DistributionMethod


class Limit(BaseModel):
    """物品限制"""

    level: int | None = None
    """限制等级"""
    stone: int | None = None
    """花费灵石"""
    cooldown: int | None = None
    """冷却时间"""
    count: int | None = None
    """使用次数"""
    distribution: DistributionMethod | list[DistributionMethod] = Field(
        DistributionMethod.all
    )
    """发放途径"""
