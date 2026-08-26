

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SetCodeType(enum.StrEnum):
    SET_CODE = "set-code"

    def visit(self, set_code: typing.Callable[[], T_Result]) -> T_Result:
        if self is SetCodeType.SET_CODE:
            return set_code()
