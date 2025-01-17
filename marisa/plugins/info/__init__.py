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

from marisa.models import Buff, User
from marisa.utils.jsondata import jsondata

from .render import render

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
        .options(selectinload(User.sect), selectinload(User.buff))
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

    # Avatar
    user_avatar = (
        session.user.avatar
        or "https://avatars.githubusercontent.com/u/170725170?s=200&v=4"
    )

    # Level Up Info
    level_rate = jsondata.get_level_data(user_info.level).spend
    last_level = jsondata.get_level_data("-1")

    if user_info.level == last_level:
        level_up_status = "位面至高"
    else:
        need_exp = jsondata.get_next_level_data(user_info.level).power - user_info.exp
        if need_exp > 0:
            level_up_status = f"还需 {need_exp} 修为可突破！"
        else:
            level_up_status = "即刻突破！"

    # Buff Info
    buff_info = await db_session.get(Buff, user_info.id)
    if buff_info is None:
        mainbuff_name = subuff_name = secbuff_name = dharma_name = armor_name = "无"
    else:
        mainbuff_name = (
            f"""
            {jsondata.get_mainbuff_data(buff_info.main_buff).name}（{jsondata.get_mainbuff_data(buff_info.main_buff).level}）
            """
            if buff_info.main_buff != 0
            else "无"
        )
        subuff_name = (
            f"""
            {jsondata.get_subuff_data(buff_info.sub_buff).name}（{jsondata.get_subuff_data(buff_info.sub_buff).level}）
            """
            if buff_info.sub_buff != 0
            else "无"
        )
        secbuff_name = (
            f"""
            {jsondata.get_secbuff_data(buff_info.sec_buff).name}（{jsondata.get_secbuff_data(buff_info.sec_buff).level}）
            """
            if buff_info.sec_buff != 0
            else "无"
        )
        dharma_name = (
            f"""
            {jsondata.get_dharma_data(buff_info.dharma).name}（{jsondata.get_dharma_data(buff_info.dharma).level}）
            """
            if buff_info.dharma != 0
            else "无"
        )
        armor_name = (
            f"""
            {jsondata.get_armor_data(buff_info.armor).name}（{jsondata.get_armor_data(buff_info.armor).level}）
            """
            if buff_info.armor != 0
            else "无"
        )

    # Sect Info
    sect_id = user_info.sect.sect_id
    if sect_id:
        sect_name = user_info.sect.info.name
        sect_position = user_info.sect.position
    else:
        sect_name = sect_position = "无"

    # Rank
    register_query = select(User.id, User.create_time).order_by(User.create_time.asc())
    register_rank = await db_session.execute(register_query)
    user_register_rank = next(
        (
            rank
            for rank, (user_id, create_time) in enumerate(register_rank, start=1)
            if user_id == user_info.id
        ),
        None,
    )

    exp_query = select(User.id, User.exp).order_by(User.exp.desc())
    exp_rank = await db_session.execute(exp_query)
    user_exp_rank = next(
        (
            rank
            for rank, (user_id, exp) in enumerate(exp_rank, start=1)
            if user_id == user_info.id
        ),
        None,
    )

    stone_query = select(User.id, User.stone).order_by(User.stone.desc())
    stone_rank = await db_session.execute(stone_query)
    user_stone_rank = next(
        (
            rank
            for rank, (user_id, stone) in enumerate(stone_rank, start=1)
            if user_id == user_info.id
        ),
        None,
    )

    info_map = {
        "avatar": user_avatar,
        "title": user_info.user_title if user_info.user_title else "暂无",
        "name": user_info.user_name,
        "level": user_info.level,
        "exp": user_info.exp,
        "stone": user_info.stone,
        "root": f"{user_info.root}（{user_info.root_type} + {level_rate * 100} %）",
        "level_up_status": f"{level_up_status}",
        "mainbuff": mainbuff_name,
        "secbuff": secbuff_name,
        "subuff": subuff_name,
        "atk": f"{user_info.buff.atk}，攻修等级：{user_info.buff.atk_level} 级",
        "dharma": dharma_name,
        "armor": armor_name,
        "sect_name": sect_name,
        "sect_position": sect_position,
        "register_rank": f"道友是踏入修仙世界的第 {user_register_rank} 人",
        "exp_rank": f"第 {user_exp_rank} 名",
        "stone_rank": f"第 {user_stone_rank} 名",
    }

    img = await render(info_map)
    await db_session.commit()
    await UniMessage.image(raw=img).finish(at_sender=True)
