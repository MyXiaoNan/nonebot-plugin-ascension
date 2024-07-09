from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")

from .config import Config

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
        "author": "Komorebi <mute231010@gmail.com>",
        "version": "0.1.0",
    },
)
