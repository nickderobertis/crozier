

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserCollaboratorType(enum.StrEnum):
    USER = "USER"

    def visit(self, user: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserCollaboratorType.USER:
            return user()
