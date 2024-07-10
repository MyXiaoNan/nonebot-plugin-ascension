from nonebot_plugin_orm import Model
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class Backpack(Model):
    """背包"""

    __tablename__ = "backpack"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    """用户 ID"""
    goods_id: Mapped[int]
    """物品 ID"""
    goods_name: Mapped[str]
    """物品名称"""
    goods_type: Mapped[str]
    """物品类型"""
    goods_amount: Mapped[int]
    """物品数量"""
    bind_amount: Mapped[int] = mapped_column(default=0)
    """绑物数量"""
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    """创建时间"""
    update_time: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
    """更新时间"""
