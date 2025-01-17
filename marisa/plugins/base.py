import random

from nonebot_plugin_uninfo import Uninfo
from nonebot_plugin_waiter import waiter
from sqlalchemy.exc import IntegrityError
from nonebot.internal.adapter import Event
from nonebot_plugin_user import UserSession
from nonebot_plugin_orm import async_scoped_session
from nonebot_plugin_alconna import Match, Button, Command, UniMessage, FallbackStrategy

from ..models import User
from ..schemas import Root
from ..configs import config
from ..utils.jsondata import jsondata
from ..utils.annotated import UserInfo

start_ascension = Command("我要修仙").build(use_cmd_start=True)
rebirth_ascension = Command("重入仙途").alias("自断筋脉").build(use_cmd_start=True)
rename = Command("改名 [name:str]").build(use_cmd_start=True)
sign_in = Command("签到").build(use_cmd_start=True)
level_up = Command("突破").build(use_cmd_start=True)


@start_ascension.handle()
async def _(session: Uninfo, user_session: UserSession):
    user_name = session.user.name or "无名客"

    root_data = jsondata.get_all_root_data()
    root, root_type = jsondata.select_root()
    power: int = int(100 * float(Root.model_validate(root_data[root_type]).speeds))

    user = User(
        id=user_session.user.id,
        user_name=user_name,
        root=root,
        root_type=root_type,
        level="江湖好手",
        stone=0,
    )

    if not await User.is_user_exist(user.id, user_name):
        try:
            await User.create_user(user)
        except IntegrityError:
            await UniMessage(f"您的道号『 {user_name} 』已被占用，请输入新的道号").send(
                at_sender=True
            )

            @waiter(waits=["message"], keep_session=True)
            async def check(event: Event):
                return event.get_plaintext()

            new_name = await check.wait(timeout=30)

            if new_name is None:
                await (
                    UniMessage.text("等待超时，想好了再来喔")
                    .keyboard(Button("input", "重试", text="/我要修仙"))
                    .finish(at_sender=True, fallback=FallbackStrategy.ignore)
                )
            user.user_name = new_name
            await User.create_user(user)

        await UniMessage(
            f"欢迎来到修真界。你的灵根为：{root}，类型是：{root_type}。你的战力为：{power}。当前境界：江湖好手"
        ).finish(at_sender=True)
    await (
        UniMessage.text("你已迈入修仙世界，输入 『 /我的修仙信息 』查看信息吧")
        .keyboard(Button("input", "我的信息", text="/我的修仙信息"))
        .finish(at_sender=True, fallback=FallbackStrategy.ignore)
    )


@rebirth_ascension.handle()
async def _(user_info: UserInfo, session: async_scoped_session):
    if user_info.stone < config.rebirth.cost:
        await UniMessage("你的灵石还不够呢，快去赚点灵石吧！").finish(at_sender=True)

    root_data = jsondata.get_all_root_data()
    root, root_type = jsondata.select_root()
    power: int = int(100 * float(root_data[root_type].speeds))

    user = User(
        id=user_info.id,
        user_name=user_info.user_name,
        root=root,
        root_type=root_type,
        level="江湖好手",
        stone=0,
    )

    await User.delete_user(user_info)
    await User.create_user(user)
    await session.commit()
    await UniMessage(
        f"欢迎来到修真界。你的灵根为：{root}，类型是：{root_type}。你的战力为：{power}。当前境界：江湖好手"
    ).finish(at_sender=True)


@rename.handle()
async def _(
    name: Match[str],
    user_info: UserInfo,
    session: async_scoped_session,
):
    if name.available:
        new_name = name.result
    else:
        await UniMessage("请输入名字").send(at_sender=True)

        @waiter(waits=["message"], keep_session=True)
        async def check(event: Event):
            return event.get_plaintext()

        resp = await check.wait(timeout=30)

        if resp is None:
            await (
                UniMessage.text("等待超时，想好了再来喔")
                .keyboard(Button("input", "重试", text="/改名"))
                .finish(at_sender=True, fallback=FallbackStrategy.ignore)
            )
        if resp.isdigit():
            await (
                UniMessage.text("不能为纯数字，再想想吧")
                .keyboard(Button("input", "重试", text="/改名"))
                .finish(at_sender=True, fallback=FallbackStrategy.ignore)
            )
        new_name = resp

    if len(new_name) >= 15:
        await (
            UniMessage.text("长度过长，请修改后重试！")
            .keyboard(Button("input", "重试", text="/改名"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )

    user_info.user_name = new_name
    try:
        await session.commit()
    except IntegrityError:
        await (
            UniMessage.text("已存在该道号！道友再想想别的吧")
            .keyboard(Button("input", "重试", text="/改名"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
    await UniMessage("改名成功").finish(at_sender=True)


@sign_in.handle()
async def _(user_info: UserInfo, session: async_scoped_session):
    if user_info.status.is_sign:
        await UniMessage("贪心的人是不会有好运的").finish(at_sender=True)

    stone = random.randint(config.sign_in.stone[0], config.sign_in.stone[1])
    user_info.stone += stone
    user_info.status.is_sign = True
    await session.commit()
    await UniMessage(f"签到成功，获得 {stone} 块灵石").finish(at_sender=True)


@level_up.handle()
async def _(user_info: UserInfo, session: async_scoped_session):
    # TODO
    ...
