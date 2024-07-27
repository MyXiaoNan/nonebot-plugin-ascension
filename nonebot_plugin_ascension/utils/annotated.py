from typing import Annotated

from sqlalchemy import select
from nonebot.params import Depends
from nonebot_plugin_orm import SQLDepends
from nonebot_plugin_userinfo import UserInfo as _UserInfo
from nonebot_plugin_userinfo import EventUserInfo as _EventUserInfo

from .depends import get_user_id
from ..models import Buff as _Buff
from ..models import User as _User
from ..models import UserCD as _UserCD
from ..models import Backpack as _Backpack

EventUserInfo = Annotated[_UserInfo, _EventUserInfo()]
UserInfo = Annotated[
    _User, SQLDepends(select(_User).where(_User.user_id == Depends(get_user_id)))
]
BuffInfo = Annotated[
    _Buff, SQLDepends(select(_Buff).where(_Buff.user_id == Depends(get_user_id)))
]
BackpackInfo = Annotated[
    _Backpack, SQLDepends(select(_Buff).where(_Buff.user_id == Depends(get_user_id)))
]
UserCDInfo = Annotated[
    _UserCD, SQLDepends(select(_UserCD).where(_UserCD.user_id == Depends(get_user_id)))
]
