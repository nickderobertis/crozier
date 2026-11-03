

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PageV2Edition(enum.StrEnum):
    TWO0 = "2.0"

    def visit(self, two0: typing.Callable[[], T_Result]) -> T_Result:
        if self is PageV2Edition.TWO0:
            return two0()
