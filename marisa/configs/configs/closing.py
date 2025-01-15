from pydantic import Field

from . import BaseConfig


class ClosingConfig(BaseConfig):
    """闭关"""

    exp: int = Field(default=60, alias="每分钟修为收益")
    """每分钟修为收益"""
    exp_upper_limit: float = Field(default=1.5, alias="修为收益上限")
    """修为收益上限"""
