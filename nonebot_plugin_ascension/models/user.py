from enum import Enum
from typing_extensions import Self

from sqlalchemy.orm import Mapped, mapped_column
from nonebot_plugin_orm import Model, get_session
from sqlalchemy import String, Boolean, DateTime, func


class UserStatus(Enum):
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

    user_id: Mapped[str] = mapped_column(primary_key=True)
    """用户 ID"""
    user_name: Mapped[str] = mapped_column(String(15), primary_key=True, unique=True)
    """用户名"""
    user_title: Mapped[str | None]
    """称号"""
    root: Mapped[str]
    """灵根"""
    root_type: Mapped[str]
    """灵根类型"""
    level: Mapped[str]
    """等级"""
    stone: Mapped[int]
    """灵石"""
    power: Mapped[int] = mapped_column(default=0)
    """战力"""
    user_stamina: Mapped[int] = mapped_column(default=240)
    """体力"""
    exp: Mapped[int] = mapped_column(default=0)
    """经验"""
    sect_id: Mapped[str | None]
    """宗门 ID"""
    sect_position: Mapped[str | None]
    """宗门职务"""
    sect_task: Mapped[int] = mapped_column(default=0)
    """宗门任务"""
    sect_contribution: Mapped[int] = mapped_column(default=0)
    """宗门贡献"""
    sect_elixir_get: Mapped[int] = mapped_column(default=0)
    """宗门丹药获取"""
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
    hp: Mapped[int] = mapped_column(default=0)
    """生命值"""
    mp: Mapped[int] = mapped_column(default=0)
    """真元"""
    atk: Mapped[int] = mapped_column(default=0)
    """攻击力"""
    atk_practice: Mapped[int] = mapped_column(default=0)
    """攻击修炼等级"""
    blessed_spot_name: Mapped[str | None]
    """洞天福地名称"""
    blessed_spot_flag: Mapped[int] = mapped_column(default=0)
    """洞天福地标志"""
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    """创建时间"""
    last_check_time: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
    """上次检查时间"""

    @classmethod
    async def create_user(cls, user: Self):
        """创建用户"""
        session = get_session()
        async with session.begin():
            session.add(user)

    @classmethod
    async def delete_user(cls, user: Self):
        """删除用户"""
        session = get_session()
        async with session.begin():
            await session.delete(user)

    @classmethod
    async def is_user_exist(cls, user_id: str) -> bool:
        """判断用户是否存在"""
        session = get_session()
        async with session.begin():
            user = await session.get(User, user_id)
            if not user:
                return False
            return True


class UserCD(Model):
    """用户 CD"""

    __tablename__ = "user_cd"

    user_id: Mapped[str] = mapped_column(primary_key=True)
    """用户 ID"""
    status: Mapped[UserStatus] = mapped_column(default=UserStatus.NONE)
    """状态"""
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    """创建时间"""
    scheduled_time: Mapped[int | None]
    """计划时间"""
