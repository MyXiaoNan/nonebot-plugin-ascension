from nonebot import require, get_driver
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_orm")
require("nonebot_plugin_waiter")
require("nonebot_plugin_alconna")
require("nonebot_plugin_userinfo")
require("nonebot_plugin_htmlrender")

from . import migrations
from .config import Config
from .models import Buff as Buff
from .models import Sect as Sect
from .models import User as User
from .handlers import base as base
from .handlers import buff as buff
from .handlers import info as info
from .models import UserCD as UserCD
from .models import Backpack as Backpack
from .utils.resource import check_resource
from .extension import text_to_pic as text_to_pic

__plugin_meta__ = PluginMetadata(
    name="羽化登仙",
    description="破除桎梏，蜕变凡尘，欢迎来到修真界",
    usage="详见文档",
    type="application",
    config=Config,
    homepage="https://github.com/MyXiaoNan/nonebot-plugin-ascension",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={
        "unique_name": "Ascension",
        "orm_version_location": migrations,
        "author": "Komorebi <mute231010@gmail.com>",
        "version": "0.1.0",
    },
)

driver = get_driver()


@driver.on_startup
async def check_res_integrity():
    await check_resource()
