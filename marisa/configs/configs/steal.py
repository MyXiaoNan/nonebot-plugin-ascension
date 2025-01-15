from pydantic import Field

from . import BaseConfig


class StealConfig(BaseConfig):
    """偷灵石"""

    punishment: int = Field(default=100000, alias="惩罚值")
    """惩罚值"""
    limit: list[float] = Field(default=[0.01, 0.50], alias="范围")
    """偷灵石范围 (单位：百分比)"""
