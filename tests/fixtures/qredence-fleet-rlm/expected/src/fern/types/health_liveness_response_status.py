

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthLivenessResponseStatus(enum.StrEnum):
    OK = "ok"

    def visit(self, ok: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthLivenessResponseStatus.OK:
            return ok()
