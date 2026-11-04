

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActGetActionResponseType(enum.StrEnum):
    STATUS = "status"

    def visit(self, status: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActGetActionResponseType.STATUS:
            return status()
