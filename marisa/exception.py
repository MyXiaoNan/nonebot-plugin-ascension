from nonebot.exception import NoneBotException


class MarisaException(NoneBotException):
    """异常基类"""


class ItemNotFoundError(MarisaException):
    """物品未找到异常"""

    def __init__(self, item_id: int) -> None:
        self.item_id = item_id

    def __repr__(self) -> str:
        return f"ItemNotFoundError(item_id={self.item_id})"
