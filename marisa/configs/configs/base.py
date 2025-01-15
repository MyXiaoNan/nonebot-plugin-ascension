import re
import random
import string

from pydantic import Field, field_validator

from . import BaseConfig


def generate_password(length=20) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


class BasicConfig(BaseConfig):
    """基础配置"""

    enable_webui: bool = Field(default=True, alias="启用后台管理")
    """是否启用 WebUI"""
    webui_password: str = Field(
        default=generate_password(), min_length=8, max_length=20, alias="后台管理密码"
    )
    send_with_image: bool = Field(default=True, alias="启用文转图")
    """是否使用图片发送消息"""
    log_file: str = Field(
        default="ERROR", alias="日志保存等级", description="必须为等级名称"
    )
    """日志保存等级，必须为等级名称"""
    log_expire_timeout: int = Field(
        default=7, alias="日志过期时间", description="单位: 天"
    )
    """日志文件过期时间"""

    @field_validator("webui_password")
    def validate_password(cls, value):
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number.")
        return value
