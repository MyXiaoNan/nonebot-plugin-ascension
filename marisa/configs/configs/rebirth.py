from pydantic import Field

from . import BaseConfig


class RebirthConfig(BaseConfig):
    """重入仙途"""

    cost: int = Field(default=100000, alias="重入仙途消费")
    """重入仙途消费"""
