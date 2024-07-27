from pydantic import Field, BaseModel


class LevelInfo(BaseModel):
    """境界信息"""

    power: int
    """战力"""
    atk: int = Field(int, alias="ATK")
    ac: int = Field(int, alias="AC")
    spend: int | float
    hp: int = Field(int, alias="hp")
    mp: int = Field(int, alias="MP")
    comment: int
    rate: int
    exp: int
    """修为"""
    sp: int = Field(int, alias="SP")
    sp_ra: float = Field(float, alias="SP_RA")
