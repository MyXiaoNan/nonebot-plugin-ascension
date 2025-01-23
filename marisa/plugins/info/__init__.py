from sqlalchemy import or_, select
from sqlalchemy.orm import selectinload
from nonebot_plugin_uninfo import get_session
from nonebot.internal.adapter import Bot, Event
from nonebot_plugin_orm import async_scoped_session
from nonebot_plugin_user import UserSession, get_user
from nonebot_plugin_alconna import (
    At,
    Match,
    Button,
    Command,
    UniMessage,
    FallbackStrategy,
)

from marisa.models import User
from marisa.libs.renderer import userinfo_to_html
from marisa.libs.renderer.context import RankContext, UserContext

info = (
    Command("修仙信息 [target: At|str|int]")
    .config(fuzzy_match=False)
    .build(use_cmd_start=True)
)
info.shortcut("查看存档", {"command": "修仙信息", "fuzzy": True, "prefix": True})
info.shortcut("我的存档", {"command": "修仙信息", "fuzzy": False, "prefix": True})
info.shortcut("我的修仙信息", {"command": "修仙信息", "fuzzy": False, "prefix": True})


@info.handle()
async def _(
    bot: Bot,
    event: Event,
    target: Match[At | str | int],
    db_session: async_scoped_session,
    user_session: UserSession,
):
    if target.available:
        name = "此人"
        if isinstance(target.result, At):
            platform_id = target.result.target
            ident = (await get_user(user_session.platform, platform_id)).id
        else:
            ident = target.result
    else:
        name = "你"
        ident = user_session.user_id
    stmt = (
        select(User)
        .options(selectinload(User.sect), selectinload(User.backpack))
        .where(or_(User.id == ident, User.user_name == ident))
    )
    user_info = (await db_session.execute(stmt)).scalar()
    if user_info is None:
        await (
            UniMessage.text(
                f"修仙界没有{name}的足迹，输入 『 /我要修仙 』 加入修仙世界吧！"
            )
            .keyboard(Button("input", "我要修仙", text="/我要修仙"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
    session = await get_session(bot, event)
    if session is None:
        return

    user_avatar = (
        session.user.avatar
        or "https://avatars.githubusercontent.com/u/170725170?s=200&v=4"
    )

    register_query = select(User.id, User.create_time).order_by(User.create_time.asc())
    register_rank = await db_session.execute(register_query)
    user_register_rank = next(
        (
            rank
            for rank, (user_id, create_time) in enumerate(register_rank, start=1)
            if user_id == user_info.id
        )
    )
    exp_query = select(User.id, User.exp).order_by(User.exp.desc())
    exp_rank = await db_session.execute(exp_query)
    user_exp_rank = next(
        (
            rank
            for rank, (user_id, exp) in enumerate(exp_rank, start=1)
            if user_id == user_info.id
        )
    )
    stone_query = select(User.id, User.stone).order_by(User.stone.desc())
    stone_rank = await db_session.execute(stone_query)
    user_stone_rank = next(
        (
            rank
            for rank, (user_id, stone) in enumerate(stone_rank, start=1)
            if user_id == user_info.id
        )
    )

    context = UserContext.from_user(user_info)
    rank = RankContext(
        register=user_register_rank, exp=user_exp_rank, stone=user_stone_rank
    )
    context.header.avatar = user_avatar
    context.rank = rank

    img = await userinfo_to_html(context)
    await db_session.commit()
    await UniMessage.image(raw=img).finish(at_sender=True)
