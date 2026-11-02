

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StartFiringResponse(enum.StrEnum):
    LIT = "lit"

    def visit(self, lit: typing.Callable[[], T_Result]) -> T_Result:
        if self is StartFiringResponse.LIT:
            return lit()
