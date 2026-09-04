

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutOauthClientClientIdResponseResponseStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutOauthClientClientIdResponseResponseStatus.ACTIVE:
            return active()
        if self is PutOauthClientClientIdResponseResponseStatus.INACTIVE:
            return inactive()
