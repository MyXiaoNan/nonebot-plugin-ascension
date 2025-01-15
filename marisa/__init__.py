from nonebot import require, get_driver
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_orm")
require("nonebot_plugin_uninfo")
require("nonebot_plugin_waiter")
require("nonebot_plugin_alconna")
require("nonebot_plugin_htmlrender")

from . import migrations
from .models import Buff as Buff
from .models import Sect as Sect
from .models import User as User
from .plugins import base as base
from .plugins import info as info
from .models import UserCD as UserCD
from .configs import configs as configs
from .models import Backpack as Backpack
from .utils.resource import check_resource
from .extension import text_to_pic as text_to_pic
from .configs import config_manager as config_manager

__plugin_meta__ = PluginMetadata(
    name="羽化登仙",
    description="破除桎梏，蜕变凡尘，欢迎来到修真界",
    usage="详见文档",
    type="application",
    homepage="https://github.com/MyXiaoNan/Marisa",
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_uninfo", "nonebot_plugin_alconna"
    ),
    extra={
        "unique_name": "Marisa",
        "orm_version_location": migrations,
        "author": "Komorebi <mute231010@gmail.com>",
        "version": "0.1.0",
    },
)

driver = get_driver()


@driver.on_startup
async def check_res_integrity():
    await check_resource()
