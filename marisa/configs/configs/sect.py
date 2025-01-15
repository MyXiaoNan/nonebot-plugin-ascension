from pydantic import Field

from . import BaseConfig


class SectConfig(BaseConfig):
    """宗门"""

    min_level: str = Field(default="铭纹境圆满", alias="创建宗门的最低境界")
    """创建宗门的最低境界"""
    create_cost: int = Field(default=5000000, alias="创建宗门的消耗")
    """创建宗门的消耗"""
    rename_cost: int = Field(default=50000000, alias="宗门改名消耗")
    """宗门改名消耗"""
    rename_cd: int = Field(default=1, alias="宗门改名冷却时间", description="单位: 天")
    """宗门改名冷却时间 (天)"""
    auto_change_sect_owner_cd: int = Field(
        default=7, alias="宗主长时间未在线的自动转让冷却时间", description="单位: 天"
    )
    """宗主长时间未在线的自动转让冷却时间 (天)"""
