

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error403Name(enum.StrEnum):
    NOT_AUTHORIZED = "NOT_AUTHORIZED"

    def visit(self, not_authorized: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error403Name.NOT_AUTHORIZED:
            return not_authorized()
