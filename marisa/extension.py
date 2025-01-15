from nonebot_plugin_htmlrender import text_to_pic
from nonebot_plugin_alconna.uniseg import UniMessage
from nonebot.internal.adapter import Bot, Event, Message
from nonebot_plugin_alconna.extension import Extension, add_global_extension

from .config import TEMPLATE_DIR, config


class TextToImageExtension(Extension):
    @property
    def priority(self) -> int:
        return 10

    @property
    def id(self) -> str:
        return "text_to_image"

    async def send_wrapper(
        self, bot: Bot, event: Event, send: str | Message | UniMessage
    ):
        if config.send_with_image:
            return UniMessage.image(
                raw=await text_to_pic(
                    str(send), css_path=str(TEMPLATE_DIR / "message.css")
                )
            )
        return send


add_global_extension(TextToImageExtension())
