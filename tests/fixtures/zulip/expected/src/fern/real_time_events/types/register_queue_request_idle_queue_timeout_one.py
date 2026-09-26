

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RegisterQueueRequestIdleQueueTimeoutOne(enum.StrEnum):
    MOBILE = "mobile"

    def visit(self, mobile: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegisterQueueRequestIdleQueueTimeoutOne.MOBILE:
            return mobile()
