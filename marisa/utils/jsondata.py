import random
from pathlib import Path

import ujson as json

from marisa.schemas.buff import Buff

from ..schemas import Root, BuffType
from ..configs import DATA_DIR, config


class JsonData:
    """Ascension Json Data"""

    def __init__(self) -> None:
        self.root_path: Path = DATA_DIR / "root.json"
        self.level_path: Path = DATA_DIR / "level" / f"{config.level_up.theme}.json"
        self.sect_path: Path = DATA_DIR / "sect.json"

    def _get_level_data(self) -> dict[str, str]:
        """获取境界数据"""
        return json.loads(self.level_path.read_text("utf-8"))

    def _get_all_root_data(self) -> list[Root]:
        """获取全部灵根数据"""
        data = json.loads(self.root_path.read_text("utf-8"))["root"]
        return [Root(**root) for root in data]

    def get_level_name(self, level: int) -> str:
        """获取对应境界名称"""
        return self._get_level_data()[str(level)]

    def get_level_exp(self, level: int) -> int:
        """获取对应境界所需经验"""
        cfg = config.level_up
        return round(int(cfg.base_exp * (cfg.cardinality**level)) / 10) * 10

    def get_level_up_probability(self, level: int) -> float:
        """获取对应境界突破概率"""
        return max(0, 100 - 2 * level)

    def get_root_data(self, name: str) -> Root:
        """获取灵根数据"""
        roots: list[Root] = self._get_all_root_data()
        return list(filter(lambda root: root.name == name, roots))[0]

    def select_root(self) -> Root:
        """随机选择灵根"""
        roots: list[Root] = self._get_all_root_data()
        roots_with_dr: list[Root] = [
            root
            for root in roots
            if any(buff.type == BuffType.dr for buff in root.buff)
        ]

        weighted_roots = []
        for root in roots_with_dr:
            dr_buff: Buff = next(buff for buff in root.buff if buff.type == BuffType.dr)
            weight: float = dr_buff.value
            weighted_roots.extend([root] * int(weight * 10))

        chosen_root: Root = random.choice(weighted_roots)
        chosen_type: str = random.choice(chosen_root.type)

        chosen_root.type = chosen_type

        return chosen_root


jsondata = JsonData()
