from nonebot.internal.adapter import Event
from nonebot_plugin_userinfo import UserInfo, EventUserInfo


def get_user_id(event: Event) -> str:
    return event.get_user_id()


def get_user_name(event_user: UserInfo = EventUserInfo()) -> str:
    return event_user.user_name
