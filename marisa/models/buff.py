from sqlalchemy import ForeignKey
from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, mapped_column


class Buff(Model):
    """Buff 信息"""

    __tablename__ = "buff"

    id: Mapped[str] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    """用户 ID"""
    hp: Mapped[int] = mapped_column(default=0)
    """生命值"""
    mp: Mapped[int] = mapped_column(default=0)
    """真元"""
    atk: Mapped[int] = mapped_column(default=0)
    """攻击力"""
    vit: Mapped[int] = mapped_column(default=240)
    """体力"""
    exp: Mapped[int] = mapped_column(default=0)
    """经验"""
    atk_level: Mapped[int] = mapped_column(default=0)
    """攻击修炼等级"""
    atk_buff: Mapped[int] = mapped_column(default=0)
    """攻击加成"""
    main_buff: Mapped[int] = mapped_column(default=0)
    """主功法"""
    sec_buff: Mapped[int] = mapped_column(default=0)
    """神通"""
    sub_buff: Mapped[int] = mapped_column(default=0)
    """辅修"""
    dharma: Mapped[int] = mapped_column(default=0)
    """法宝"""
    armor: Mapped[int] = mapped_column(default=0)
    """防具"""
