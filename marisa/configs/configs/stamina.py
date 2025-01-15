from pydantic import Field

from . import BaseConfig


class StaminaConfig(BaseConfig):
    """体力"""

    max_stamina: int = Field(default=240, alias="体力上限")
    """体力上限"""
