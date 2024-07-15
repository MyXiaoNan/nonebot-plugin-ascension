import random
from typing import Any
from pathlib import Path

import ujson as json

from ..config import DATA_DIR
from ..schema import (
    SecBuff,
    SubBuff,
    MainBuff,
    RootType,
    ArmorBuff,
    LevelInfo,
    DharmaBuff,
    SectPosition,
)


class JsonData:
    """Ascension Json Data"""

    def __init__(self):
        self.root_path: Path = DATA_DIR / "data" / "灵根.json"
        self.level_path: Path = DATA_DIR / "data" / "境界.json"
        self.sect_path: Path = DATA_DIR / "data" / "宗门.json"
        self.level_up_rate_path: Path = DATA_DIR / "data" / "突破概率.json"
        self.mainbuff_path: Path = DATA_DIR / "data" / "功法" / "主功法.json"
        self.subuff_path: Path = DATA_DIR / "data" / "功法" / "辅修功法.json"
        self.secbuff_path: Path = DATA_DIR / "data" / "功法" / "神通.json"
        self.dharma_path: Path = DATA_DIR / "data" / "装备" / "法器.json"
        self.armor_path: Path = DATA_DIR / "data" / "装备" / "防具.json"

    def _get_level_data(self) -> dict[str, LevelInfo]:
        """获取境界数据"""
        return json.loads(self.level_path.read_text("utf-8"))

    def _get_sect_data(self) -> dict[str, SectPosition]:
        """获取宗门数据"""
        return json.loads(self.sect_path.read_text("utf-8"))

    def get_level_data(self, level: str) -> LevelInfo:
        """
        获取境界数据
        参数：
            level: 境界（若填入 `-1`，则返回最后一个境界信息）
        """
        if level == "-1":
            all_level_name: list = list(self._get_level_data().keys())
            last_level_name: str = all_level_name[-1]
            return LevelInfo.parse_obj(self._get_level_data()[last_level_name])
        return LevelInfo.parse_obj(self._get_level_data()[level])

    def get_next_level_data(self, level: str) -> LevelInfo:
        """获取用户下一境界数据"""
        all_level_name = list(self._get_level_data().keys())
        level_index = all_level_name.index(level)
        return LevelInfo.parse_obj(self.get_level_data(all_level_name[level_index + 1]))

    def get_all_root_data(self) -> dict[str, RootType]:
        """获取全部灵根数据"""
        return json.loads(self.root_path.read_text("utf-8"))

    def get_root_data(self, name: str) -> RootType:
        """获取灵根数据"""
        return RootType.parse_obj(self.get_all_root_data()[name])

    def get_mainbuff_data(self, key: str | int) -> MainBuff:
        """获取功法数据"""
        return MainBuff.parse_obj(
            json.loads(self.mainbuff_path.read_text("utf-8"))[str(key)]
        )

    def get_secbuff_data(self, key: str | int) -> SecBuff:
        """获取神通数据"""
        return SecBuff.parse_obj(
            json.loads(self.secbuff_path.read_text("utf-8"))[str(key)]
        )

    def get_subuff_data(self, key: str | int) -> SubBuff:
        """获取辅修数据"""
        return SubBuff.parse_obj(
            json.loads(self.subuff_path.read_text("utf-8"))[str(key)]
        )

    def get_dharma_data(self, key: str | int) -> DharmaBuff:
        """获取法器数据"""
        return DharmaBuff.parse_obj(
            json.loads(self.dharma_path.read_text("utf-8"))[str(key)]
        )

    def get_armor_data(self, key: str | int) -> ArmorBuff:
        """获取防具数据"""
        return ArmorBuff.parse_obj(
            json.loads(self.armor_path.read_text("utf-8"))[str(key)]
        )

    def select_root(self) -> tuple[str, str]:
        data = self.get_all_root_data()
        root_types: list[str] = list(data.keys())
        root_rate = [data[root_type].type_rate for root_type in root_types]

        select_root_type: str = random.choices(root_types, weights=root_rate, k=1)[0]
        select_root: str = random.choice(data[select_root_type].type_list)

        return select_root, select_root_type

    def _get_level_up_rate_data(self) -> dict[str, Any]:
        """获取境界突破概率数据"""
        return json.loads(self.level_up_rate_path.read_text("utf-8"))

    def get_user_level_up_rate(self, level) -> str:
        """
        获取用户突破概率
        参数:
            level: 当前等级
        """
        return self._get_level_up_rate_data()[level]


jsondata = JsonData()
