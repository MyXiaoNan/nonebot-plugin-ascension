from typing import Literal

from pydantic import BaseModel

from marisa.schemas import Buff, Item


class Reward(BaseModel):
    """奖励"""

    stone: int | None
    """灵石"""
    item: list[Item] | None
    """物品"""
    buff: Buff | None
    """增幅"""


class Ending(BaseModel):
    """结局"""

    description: str
    """描述"""
    reward: Reward
    """奖励"""


class Quest(BaseModel):
    """悬赏令"""

    name: str
    type: Literal["assassin", "picking", "repress"]
    ending: Ending
