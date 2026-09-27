

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceUnavailableErrorBodyStatus(enum.StrEnum):
    NOT_READY = "NOT_READY"

    def visit(self, not_ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServiceUnavailableErrorBodyStatus.NOT_READY:
            return not_ready()
