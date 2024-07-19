from pydantic import BaseModel


class RootType(BaseModel):
    """灵根类型"""

    type_rate: int
    type_list: list[str]
    type_speeds: float
    type_flag: list[int | None]
