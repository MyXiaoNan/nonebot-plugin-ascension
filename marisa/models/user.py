from enum import Enum
from typing import TYPE_CHECKING
from typing_extensions import Self

from nonebot_plugin_orm import Model, get_session
from sqlalchemy.orm import Mapped, relationship, selectinload, mapped_column
from sqlalchemy import String, Boolean, DateTime, ForeignKey, and_, func, select

if TYPE_CHECKING:
    from . import Sect, Backpack


class UserStatusType(Enum):
    """用户状态"""

    NONE = 0
    """无状态"""
    MEDITATING = 1
    """闭关"""
    WORKING = 2
    """悬赏令"""
    EXPLORING = 3
    """秘境"""
    PRACTICING = 4
    """修炼"""


class User(Model):
    """用户表"""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    """用户 ID"""
    user_name: Mapped[str] = mapped_column(String(15), unique=True)
    """用户名"""
    user_title: Mapped[str | None]
    """称号"""
    root: Mapped[str]
    """灵根"""
    root_type: Mapped[str]
    """灵根类型"""
    level: Mapped[int]
    """等级"""
    exp: Mapped[int]
    """经验"""
    stone: Mapped[int]
    """灵石"""
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    """创建时间"""
    last_check_time: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
    """上次检查时间"""

    sect: Mapped["UserSect"] = relationship(
        "UserSect", back_populates=None, uselist=False
    )
    status: Mapped["UserStatus"] = relationship(
        "UserStatus", back_populates=None, uselist=False
    )
    backpack: Mapped[list["Backpack"]] = relationship("Backpack", back_populates=None)

    @classmethod
    async def create_user(cls, user: Self):
        """创建用户"""
        sect = UserSect(id=user.id, user_id=user.id)
        status = UserStatus(id=user.id, user_id=user.id)

        objects = [user, sect, status]

        session = get_session()
        async with session.begin():
            session.add_all(objects)

    @classmethod
    async def delete_user(cls, user: Self):
        """删除用户"""
        session = get_session()
        async with session.begin():
            stmt = (
                select(cls).options(
                    selectinload(cls.sect),
                    selectinload(cls.backpack),
                    selectinload(cls.status),
                )
            ).where(cls.id == user.id)
            obj = (await session.execute(stmt)).scalar()
            if obj:
                if obj.sect:
                    await session.delete(obj.sect)
                if obj.status:
                    await session.delete(obj.status)
                for backpack_item in obj.backpack:
                    await session.delete(backpack_item)
                await session.delete(obj)

    @classmethod
    async def is_user_exist(cls, id: int, user_name: str) -> bool:
        """判断用户是否存在"""
        session = get_session()
        async with session.begin():
            stmt = select(User).where(and_(User.id == id, User.user_name == user_name))
            user = (await session.execute(stmt)).scalar()
            if not user:
                return False
            return True


class UserSect(Model):
    """用户宗门信息表"""

    __tablename__ = "user_sect"

    id: Mapped[str] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    """用户 ID"""
    sect_id: Mapped[int | None] = mapped_column(ForeignKey("sect.id"))
    """宗门 ID"""
    position: Mapped[str | None]
    """职务"""
    task: Mapped[int] = mapped_column(default=0)
    """任务"""
    contribution: Mapped[int] = mapped_column(default=0)
    """贡献"""
    elixir_get: Mapped[int] = mapped_column(default=0)
    """丹药获取"""

    info: Mapped["Sect"] = relationship("Sect", back_populates=None)


class UserStatus(Model):
    """用户状态信息表"""

    __tablename__ = "user_status"

    id: Mapped[str] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
    )
    """用户 ID"""
    status: Mapped[UserStatusType] = mapped_column(default=UserStatusType.NONE)
    """状态"""
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    """创建时间"""
    scheduled_time: Mapped[int | None]
    """计划时间"""
    is_sign: Mapped[bool] = mapped_column(Boolean, default=False)
    """是否签到"""
    is_beg: Mapped[bool] = mapped_column(Boolean, default=False)
    """是否参与仙途奇缘"""
    is_ban: Mapped[bool] = mapped_column(Boolean, default=False)
    """是否被禁"""
    level_up_cd: Mapped[DateTime | None] = mapped_column(DateTime)
    """突破 CD（单位：分钟）"""
    level_up_rate: Mapped[int | None]
    """突破概率"""
    work_refresh_times: Mapped[int] = mapped_column(default=0)
    """悬赏令刷新次数"""
