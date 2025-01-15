from pydantic import Field

from . import BaseConfig


class BegConfig(BaseConfig):
    """仙途奇缘"""

    max_level: str = Field(default="铭纹境圆满", alias="最高境界")
    """能领取灵石的最高境界"""
    max_days: int = Field(default=3, alias="天数上线")
    """可领取灵石的天数上限"""
    stone: list[int] = Field(default=[200000, 500000], alias="灵石奖励范围")
    """灵石奖励范围 (下限，上限)"""
