from typing_extensions import Self

from nonebot.internal.adapter import Event
from sqlalchemy.orm import Mapped, mapped_column
from nonebot_plugin_orm import Model, get_session


class Buff(Model):
    """Buff 信息"""

    __tablename__ = "buff"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    """用户 ID"""
    main_buff: Mapped[int] = mapped_column(default=0)
    """主功法"""
    sec_buff: Mapped[int] = mapped_column(default=0)
    """神通"""
    sub_buff: Mapped[int] = mapped_column(default=0)
    """辅修"""
    dharma_buff: Mapped[int] = mapped_column(default=0)
    """法宝"""
    armor_buff: Mapped[int] = mapped_column(default=0)
    """防具"""
    atk_buff: Mapped[int] = mapped_column(default=0)
    """攻击加成"""
    blessed_spot: Mapped[int] = mapped_column(default=0)
    """洞天福地"""

    @classmethod
    async def get_buff_info(cls, event: Event) -> Self | None:
        """获取 Buff 信息"""
        session = get_session()
        async with session.begin():
            buff = await session.get(Buff, event.get_user_id())
            return buff
