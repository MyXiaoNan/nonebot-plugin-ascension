from enum import Enum, IntEnum


class BuffType(str, Enum):
    """Buff 类型"""

    atk = "atk"
    """攻击力"""
    ac = "ac"
    """防御值"""
    boost = "boost"
    """倍率"""
    cr = "cr"
    """暴击率"""
    crd = "crd"
    """暴击伤害"""
    cp = "cp"
    """战力"""
    dm = "dm"
    """免伤"""
    dr = "dr"
    """掉落率"""
    ew = "ew"
    """专属武器"""
    exp = "exp"
    """经验值"""
    hp = "hp"
    """生命值"""
    mp = "mp"
    """真元"""
    sp = "sp"
    """体力"""


class LevelType(IntEnum):
    """装备等级"""

    INFERIOR = 1
    """下品"""
    SUPERIOR = 2
    """上品"""


class QualityType(IntEnum):
    """装备品质"""

    NORMAL = 1
    """普通"""
    RARE = 2
    """稀有"""
    EPIC = 3
    """史诗"""
    LEGENDARY = 4
    """传说"""


class DistributionMethod(str, Enum):
    """发放途径"""

    none = "none"
    """不发放"""
    all = "all"
    """所有途径"""
    quest = "quest"
    """悬赏令"""
    shop = "shop"
    """商店"""
    rift = "rift"
    """秘境"""
    gift = "gift"
    """礼物"""
    exchange = "exchange"
    """兑换"""
    craft = "craft"
    """合成"""
    reward = "reward"
    """奖励"""
    sect = "sect"
    """宗门"""
