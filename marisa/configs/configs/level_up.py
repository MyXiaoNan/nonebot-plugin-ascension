from pydantic import Field

from . import BaseConfig


class LevelUpConfig(BaseConfig):
    """突破"""

    cd: int = Field(default=0, alias="冷却时间")
    """突破 CD (分钟)"""
    punishment: list[int] = Field(default=[10, 35], alias="失败后扣除修为范围")
    """突破失败扣除修为范围 (百分比）"""
    probability: float = Field(default=0.2, alias="失败后增加突破概率的比例")
    """突破失败增加突破概率的比例"""
