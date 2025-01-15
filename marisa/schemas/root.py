from pydantic import Field, BaseModel


class Root(BaseModel):
    """灵根类型"""

    rate: int = Field(..., alias="type_rate")
    """抽取概率"""
    type_list: list[str]
    """灵根类型"""
    speeds: float = Field(..., alias="type_speeds")
    """闭关的修为倍率"""
    flag: list[int | None] = Field(..., alias="type_flag")
