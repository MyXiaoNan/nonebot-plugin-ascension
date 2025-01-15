from pydantic import Field, BaseModel


class LevelInfo(BaseModel):
    """境界信息"""

    power: int
    """战力"""
    atk: int = Field(..., alias="ATK")
    ac: int = Field(..., alias="AC")
    spend: int | float
    hp: int = Field(..., alias="hp")
    mp: int = Field(..., alias="MP")
    comment: int
    rate: int
    exp: int
    """修为"""
    sp: int = Field(..., alias="SP")
    sp_ra: float = Field(..., alias="SP_RA")
