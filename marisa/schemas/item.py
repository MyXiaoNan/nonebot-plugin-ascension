from typing import Literal, TypeAlias

from pydantic import BaseModel, model_validator

from marisa.schemas import Buff, Limit
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

    id: int
    name: str
    type: ItemType

    level: LevelType | None
    """等级"""
    quality: QualityType | None
    """品质"""

    buff: Buff | None
    """增幅"""
    limit: Limit | None
    """限制"""

    @model_validator(mode="after")
    def validate_equipment(self):
        type = self.type
        level = self.level
        quality = self.quality

        if type in ["dharma", "armor"]:
            if level is None or quality is None:
                raise ValueError(
                    "level and quality must be set when type is 'dharma' or 'armor'"
                )

        return self
