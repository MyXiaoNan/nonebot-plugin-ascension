from typing import Any

from nonebot_plugin_htmlrender import template_to_pic

from marisa.configs import TEMPLATE_DIR


async def render(info: dict[str, Any]) -> bytes:
    return await template_to_pic(
        template_path=str(TEMPLATE_DIR),
        template_name="info.html",
        templates={"info": info},
        pages={
            "viewport": {"width": 600, "height": 800},
            "base_url": f"file://{TEMPLATE_DIR}",
        },
    )
