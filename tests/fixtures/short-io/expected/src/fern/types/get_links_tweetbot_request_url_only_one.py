

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetLinksTweetbotRequestUrlOnlyOne(enum.StrEnum):
    ZERO = "0"

    def visit(self, zero: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetLinksTweetbotRequestUrlOnlyOne.ZERO:
            return zero()
