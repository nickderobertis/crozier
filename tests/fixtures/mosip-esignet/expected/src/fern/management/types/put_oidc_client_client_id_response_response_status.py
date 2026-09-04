

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutOidcClientClientIdResponseResponseStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutOidcClientClientIdResponseResponseStatus.ACTIVE:
            return active()
        if self is PutOidcClientClientIdResponseResponseStatus.INACTIVE:
            return inactive()
