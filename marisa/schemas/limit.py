from pydantic import Field, BaseModel

from marisa.schemas.enums import DistributionMethod


class Limit(BaseModel):
    """物品限制"""

    level: int | None
    """限制等级"""
    stone: int | None
    """花费灵石"""
    cooldown: int | None
    """冷却时间"""
    count: int | None
    """使用次数"""
    distribution: DistributionMethod = Field(DistributionMethod.all)
    """发放途径"""
