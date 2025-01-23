import random

from nonebot_plugin_htmlrender import template_to_pic

from marisa.configs import TEMPLATE_DIR

from .context import UserContext


async def userinfo_to_html(context: UserContext) -> bytes:
    return await template_to_pic(
        template_path=str(TEMPLATE_DIR),
        template_name="views/profile.html.jinja",
        templates={"context": context},
        filters={"random": lambda _: random.randint(1, 6)},
        pages={
            "viewport": {"width": 400, "height": 50},
            "base_url": f"file://{TEMPLATE_DIR}",
        },
    )
