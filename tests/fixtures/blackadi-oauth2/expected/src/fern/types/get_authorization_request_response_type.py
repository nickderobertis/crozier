

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthorizationRequestResponseType(enum.StrEnum):
    CODE = "code"

    def visit(self, code: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAuthorizationRequestResponseType.CODE:
            return code()
