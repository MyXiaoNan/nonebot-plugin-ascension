from nonebot_plugin_htmlrender import text_to_pic
from nonebot.internal.adapter import Bot, Event, Message
from nonebot_plugin_alconna.uniseg import Text, UniMessage
from nonebot_plugin_alconna.extension import Extension, add_global_extension

from .configs import TEMPLATE_DIR, config


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
        plain_text = (
            send.extract_plain_text()
            if isinstance(send, Message | UniMessage)
            else send
        )
        extra_segment = send.exclude(Text) if isinstance(send, UniMessage) else send
        if config.basic.send_with_image and plain_text != "":
            return (
                UniMessage.image(
                    raw=await text_to_pic(
                        plain_text, css_path=str(TEMPLATE_DIR / "message.css")
                    )
                )
                + extra_segment
            )
        return send


add_global_extension(TextToImageExtension())
