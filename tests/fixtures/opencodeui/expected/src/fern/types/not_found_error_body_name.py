

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotFoundErrorBodyName(enum.StrEnum):
    NOT_FOUND_ERROR = "NotFoundError"

    def visit(self, not_found_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotFoundErrorBodyName.NOT_FOUND_ERROR:
            return not_found_error()
