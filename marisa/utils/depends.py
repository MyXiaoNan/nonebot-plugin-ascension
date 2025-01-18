from nonebot_plugin_user import UserSession


def get_user_id(session: UserSession) -> int:
    return session.user_id
