from typing import Literal, TypeAlias

from pydantic import BaseModel, ConfigDict

from marisa.schemas.buff import Buff
from marisa.schemas.limit import Limit
from marisa.schemas.enums import LevelType, QualityType

ItemType: TypeAlias = Literal[
    "dharma",  # 法器
    "armor",  # 防具
    "main_tech",  # 主功法
    "second_tech",  # 辅修
    "divine_tech",  # 神通
    "elixir",  # 丹药
    "drug_material",  # 药材
]


class Item(BaseModel):
    """物品"""

    model_config = ConfigDict(extra="allow")

    id: int | None = None
    name: str
    type: ItemType

    level: LevelType | None = None
    """等级"""
    quality: QualityType | None = None
    """品质"""

    buff: list[Buff] | None = None
    """增幅"""
    limit: Limit | None = None
    """限制"""
