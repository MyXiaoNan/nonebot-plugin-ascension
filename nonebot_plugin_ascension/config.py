from pathlib import Path

from pydantic import Field, BaseModel
from nonebot.plugin import get_plugin_config

BOT_DIR = Path.cwd()
"""Bot 根目录"""

DATA_DIR = BOT_DIR / "data" / "ascension"
"""数据保存目录"""
TEMPLATE_DIR = DATA_DIR / "templates"
"""模板保存目录"""


class ScopedConfig(BaseModel):
    # 基础
    send_with_image: bool = True
    """是否使用图片发送消息"""

    # 签到
    sign_in: tuple[int, int] = (10000, 50000)
    """签到奖励（下限，上限）"""

    # 体力
    max_stamina: int = 240
    """体力上限"""

    # 偷灵石
    steal_punishment: int = 100000
    """偷灵石惩罚"""
    steal_limit: tuple[float, float] = (0.01, 0.50)
    """偷灵石限制（值：下限、上限）（单位：百分比）"""

    # 突破
    level_up_cd: int = 0
    """突破 CD（单位：分钟）"""
    level_punishment_limit: tuple[int, int] = (10, 35)
    """突破失败扣除修为，惩罚限制（值：下限、上限）（单位：百分比）"""
    level_up_probability: float = 0.2
    """突破失败增加突破概率的比例"""

    # 闭关
    closing_exp: int = 60
    """闭关每分钟获取的修为"""
    closing_exp_upper_limit: float = 1.5
    """闭关获取修为的上限阈值（例如：1.5 下个境界的修为数 * 1.5）"""

    # 重入仙途
    rebirth_cost: int = 100000
    """重入仙途的消费"""

    # 金银阁（赌坊）
    bet_cd: int = 10
    """金银阁 CD（单位：秒）"""

    # 仙途奇缘
    beg_max_level: str = "铭纹境圆满"
    """仙途奇缘能领灵石最高境界"""
    beg_max_days: int = 3
    """仙途奇缘能领灵石最多天数"""
    beg_stone: tuple[int, int] = (200000, 500000)
    """仙途奇缘灵石奖励（下限，上限）"""

    # 千世轮回
    transmigration_min_level: str = "祭道境圆满"
    """千世轮回最低境界"""

    # 宗门
    sect_min_level: str = "铭纹境圆满"
    """创建宗门最低境界"""
    sect_create_cost: int = 5000000
    """创建宗门消耗"""
    sect_rename_cost: int = 50000000
    """宗门改名消耗"""
    sect_rename_cd: int = 1
    """宗门改名 CD（单位：天）"""
    auto_change_sect_owner_cd: int = 7
    """自动换长时间不玩的宗主 CD（单位：天）"""


class Config(BaseModel):
    ascension: ScopedConfig = Field(default_factory=ScopedConfig)
    """Ascension Config"""


config: ScopedConfig = get_plugin_config(Config).ascension
