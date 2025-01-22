from typing import Generic, TypeVar

from marisa.models import User

T = TypeVar("T", bound=User)


class BuffManager(Generic[T]):
    def __init__(self, user: T) -> None:
        self.user = user

    @property
    def atk(self) -> float:
        return self.user.exp * 0.1
