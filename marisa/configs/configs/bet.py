from pydantic import Field

from . import BaseConfig


class BetConfig(BaseConfig):
    """金银阁"""

    cd: int = Field(default=10, alias="冷却", description="单位: 秒")
    """金银阁冷却时间（秒）"""
