from pydantic import Field

from . import BaseConfig


class SignInConfig(BaseConfig):
    """签到"""

    stone: list[int] = Field(default=[10000, 50000], alias="灵石奖励范围")
    """签到奖励范围 (下限，上限)"""
