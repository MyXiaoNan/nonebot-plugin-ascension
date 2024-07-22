import random

from nonebot_plugin_waiter import waiter
from sqlalchemy.exc import IntegrityError
from nonebot.internal.adapter import Event
from nonebot_plugin_orm import async_scoped_session
from nonebot_plugin_userinfo import UserInfo, EventUserInfo
from nonebot_plugin_alconna import Match, Command, UniMessage

from ..models import User
from ..config import config
from ..schema import RootType
from ..utils.jsondata import jsondata

start_ascension = Command("我要修仙").build(use_cmd_start=True)
rebirth_ascension = Command("重入仙途").alias("自断筋脉").build(use_cmd_start=True)
rename = Command("改名 [name:str]").build(use_cmd_start=True)
sign_in = Command("签到").build(use_cmd_start=True)
level_up = Command("突破").build(use_cmd_start=True)


@start_ascension.handle()
async def _(user_info: UserInfo = EventUserInfo()):

    user_id = user_info.user_id
    user_name = user_info.user_name

    root_data = jsondata.get_all_root_data()
    root, root_type = jsondata.select_root()
    power: int = int(
        100 * float(RootType.model_validate(root_data[root_type]).type_speeds)
    )

    user = User(
        user_id=user_id,
        user_name=user_name,
        root=root,
        root_type=root_type,
        level="江湖好手",
        stone=0,
        power=power,
    )

    if not await User.is_user_exist(user_id):
        await User.create_user(user)
        await UniMessage(
            f"欢迎来到修真界。你的灵根为：{root}，类型是：{root_type}。你的战力为：{power}。当前境界：江湖好手"
        ).finish(at_sender=True)
    await UniMessage("你已迈入修仙世界，输入 『 /我的修仙信息 』查看信息吧").finish(
        at_sender=True
    )


@rebirth_ascension.handle()
async def _(event: Event, session: async_scoped_session):
    user_info = await session.get(User, event.get_user_id())

    if user_info is None:
        await UniMessage(
            "修仙界没有你的足迹，输入 『 /我要修仙 』 加入修仙世界吧！"
        ).finish(at_sender=True)

    if user_info.stone < config.rebirth_cost:
        await UniMessage("你的灵石还不够呢，快去赚点灵石吧！").finish(at_sender=True)

    root_data = jsondata.get_all_root_data()
    root, root_type = jsondata.select_root()
    power: int = int(100 * float(root_data[root_type].type_speeds))

    user = User(
        user_id=user_info.user_id,
        user_name=user_info.user_name,
        root=root,
        root_type=root_type,
        level="江湖好手",
        stone=0,
        power=power,
    )

    await User.delete_user(user_info)
    await User.create_user(user)
    await session.commit()
    await UniMessage(
        f"欢迎来到修真界。你的灵根为：{root}，类型是：{root_type}。你的战力为：{power}。当前境界：江湖好手"
    ).finish(at_sender=True)


@rename.handle()
async def _(event: Event, name: Match[str], session: async_scoped_session):
    user_info = await session.get(User, event.get_user_id())
    if user_info is None:
        await UniMessage(
            "修仙界没有你的足迹，输入 『 /我要修仙 』 加入修仙世界吧！"
        ).finish(at_sender=True)

    if name.available:
        new_name = name.result
    else:
        await UniMessage("请输入名字").send(at_sender=True)

        @waiter(waits=["message"], keep_session=True)
        async def check(event: Event):
            return event.get_plaintext()

        resp = await check.wait(timeout=30)

        if resp is None:
            await UniMessage("等待超时，想好了再来喔").finish(at_sender=True)
        if resp.isdigit():
            await UniMessage("不能为纯数字，再想想吧").finish(at_sender=True)
        new_name = resp

    if len(new_name) >= 15:
        await UniMessage("长度过长，请修改后重试！").finish(at_sender=True)

    user_info.user_name = new_name
    try:
        await session.commit()
    except IntegrityError:
        await UniMessage("已存在该道号！道友再想想别的吧").finish(at_sender=True)
    await UniMessage("改名成功").finish(at_sender=True)


@sign_in.handle()
async def _(event: Event, session: async_scoped_session):
    user_info = await session.get(User, event.get_user_id())
    if user_info is None:
        await UniMessage(
            "修仙界没有你的足迹，输入 『 /我要修仙 』 加入修仙世界吧！"
        ).finish(at_sender=True)

    if user_info.is_sign:
        await UniMessage("贪心的人是不会有好运的").finish(at_sender=True)

    stone = random.randint(config.sign_in[0], config.sign_in[1])
    user_info.stone += stone
    user_info.is_sign = True
    await session.commit()
    await UniMessage(f"签到成功，获得 {stone} 块灵石").finish(at_sender=True)


@level_up.handle()
async def _(event: Event, session: async_scoped_session):
    user_info = await session.get(User, event.get_user_id())
    if user_info is None:
        await UniMessage(
            "修仙界没有你的足迹，输入 『 /我要修仙 』 加入修仙世界吧！"
        ).finish(at_sender=True)

    # TODO
