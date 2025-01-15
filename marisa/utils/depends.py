from nonebot.internal.adapter import Event


def get_user_id(event: Event) -> str:
    return event.get_user_id()
