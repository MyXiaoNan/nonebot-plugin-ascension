from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, mapped_column


class Sect(Model):
    """宗门"""

    __tablename__ = "sect"

    id: Mapped[int] = mapped_column(primary_key=True)
    """宗门 ID"""
    name: Mapped[str]
    """宗门名称"""
    owner: Mapped[str]
    """宗主 ID"""
    scale: Mapped[int | None]
    """宗门建设度"""
    stone_amount: Mapped[int]
    """灵石储备"""
    fairyland: Mapped[int | None]
    """洞天福地"""
    materials: Mapped[int]
    """宗门资材"""
    main_buff: Mapped[str | None]
    """宗门功法"""
    sec_buff: Mapped[str | None]
    """宗门神通"""
    elixir_room_level: Mapped[int]
    """宗门丹房等级"""
