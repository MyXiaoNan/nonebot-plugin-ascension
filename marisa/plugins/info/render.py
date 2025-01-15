from typing import Any

from nonebot_plugin_htmlrender import template_to_pic

from marisa.config import DATA_DIR


async def render(info: dict[str, Any]) -> bytes:
    template_path = str(DATA_DIR / "templates")

    return await template_to_pic(
        template_path=template_path,
        template_name="info.html",
        templates={"info": info},
        pages={
            "viewport": {"width": 600, "height": 800},
            "base_url": f"file://{template_path}",
        },
    )
