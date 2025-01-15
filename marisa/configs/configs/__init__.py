from pydantic import BaseModel


class BaseConfig(BaseModel):
    """配置基类"""


from .beg import BegConfig as BegConfig
from .bet import BetConfig as BetConfig
from .sect import SectConfig as SectConfig
from .base import BasicConfig as BasicConfig
from .steal import StealConfig as StealConfig
from .sign_in import SignInConfig as SignInConfig
from .closing import ClosingConfig as ClosingConfig
from .rebirth import RebirthConfig as RebirthConfig
from .session import SessionConfig as SessionConfig
from .stamina import StaminaConfig as StaminaConfig
from .level_up import LevelUpConfig as LevelUpConfig
