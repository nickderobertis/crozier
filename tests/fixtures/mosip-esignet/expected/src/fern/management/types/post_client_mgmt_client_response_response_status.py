

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostClientMgmtClientResponseResponseStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostClientMgmtClientResponseResponseStatus.ACTIVE:
            return active()
        if self is PostClientMgmtClientResponseResponseStatus.INACTIVE:
            return inactive()
