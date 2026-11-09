

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotFoundErrorBodyErrorCode(enum.StrEnum):
    NOT_FOUND = "NOT_FOUND"

    def visit(self, not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotFoundErrorBodyErrorCode.NOT_FOUND:
            return not_found()
