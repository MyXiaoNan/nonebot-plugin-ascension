from pydantic import Field, BaseModel


class LevelInfo(BaseModel):
    """境界信息"""

    power: int
    ATK: int = Field(int, alias="atk")
    AC: int = Field(int, alias="ac")
    spend: int | float
    HP: int = Field(int, alias="hp")
    MP: int = Field(int, alias="mp")
    comment: int
    rate: int
    exp: int
    SP: int = Field(int, alias="sp")
    SP_RA: float = Field(float, alias="sp_ra")
