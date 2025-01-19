from pydantic import Field, BaseModel


class Buff(BaseModel):
    """增益效果"""

    attack: float = Field(..., alias="atk")
    """攻击力"""
    armor_class: float = Field(..., alias="ac")
    """防御值"""
    boost: float = Field(..., alias="boost")
    """倍率"""
    critical_rate: float = Field(..., alias="cr")
    """暴击率"""
    critical_damage: float = Field(..., alias="crd")
    """暴击伤害"""
    combat_power: float = Field(..., alias="cp")
    """战力"""
    damage_mitigation: float = Field(..., alias="dm")
    """免伤"""
    drop_rate: float = Field(..., alias="dr")
    """掉落率"""
    exclusive_weapon: float = Field(..., alias="ew")
    """专属武器"""
    experience: float = Field(..., alias="exp")
    """经验值"""
    health_point: float = Field(..., alias="hp")
    """生命值"""
    mana_point: float = Field(..., alias="mp")
    """真元"""
    stamina_point: float = Field(..., alias="sp")
    """体力"""
