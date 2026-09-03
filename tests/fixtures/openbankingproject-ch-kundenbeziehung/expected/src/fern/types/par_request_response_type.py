

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParRequestResponseType(enum.StrEnum):
    """
    OAuth 2.1 response type (only code allowed)
    """

    CODE = "code"

    def visit(self, code: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParRequestResponseType.CODE:
            return code()
