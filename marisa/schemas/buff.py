from pydantic import Field, BaseModel


class MainBuff(BaseModel):
    """主功法"""

    name: str
    hpbuff: float
    mpbuff: float
    atkbuff: float
    ratebuff: float
    crit_buff: int
    def_buff: int
    dan_exp: int
    reap_buff: int
    exp_buff: int
    critatk: int
    two_buff: int
    number: int
    clo_exp: int
    clo_rs: int
    random_buff: int
    ew: int
    desc: str
    rank: str
    level: str


class SecBuff(BaseModel):
    """神通"""

    name: str
    skill_type: int
    atkvalue: list[float]
    hpcost: float
    mpcost: float
    turncost: int
    desc: str
    rate: int
    rank: str
    level: str


class SubBuff(BaseModel):
    """辅修"""

    name: str
    buff_type: str
    buff: str
    buff2: str
    stone: int
    integral: int
    jin: int
    drop: int
    fan: int
    abreak: int = Field(..., alias="break")
    exp: int
    desc: str
    rank: str
    level: str


class DharmaBuff(BaseModel):
    """法器"""

    name: str
    atk_buff: int | float
    crit_buff: float
    def_buff: float
    critatk: float
    zw: int
    mp_buff: int
    rank: int
    level: str
    type: str


class ArmorBuff(BaseModel):
    """防具"""

    name: str
    def_buff: float
    atk_buff: int | float
    crit_buff: float
    rank: int
    level: str
    type: str
