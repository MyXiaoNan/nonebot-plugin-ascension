from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, mapped_column


class Sect(Model):
    """宗门"""

    __tablename__ = "sect"

    sect_id: Mapped[str] = mapped_column(primary_key=True)
    """宗门 ID"""
    sect_name: Mapped[str]
    """宗门名称"""
    sect_owner: Mapped[str]
    """宗主 ID"""
    sect_scale: Mapped[int | None]
    """宗门规模"""
    sect_stone_amount: Mapped[int]
    """灵石储备"""
    sect_fairyland: Mapped[int | None]
    """洞天福地"""
    sect_materials: Mapped[int]
    """材料"""
    main_buff: Mapped[str | None]
    """宗门功法"""
    sec_buff: Mapped[str | None]
    """宗门神通"""
    elixir_room_level: Mapped[int]
    """宗门丹房等级"""
