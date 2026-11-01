

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class CaptionMediaRequestDialect(enum.StrEnum):
    BSL = "bsl"
    ASL = "asl"

    def visit(self, bsl: typing.Callable[[], T_Result], asl: typing.Callable[[], T_Result]) -> T_Result:
        if self is CaptionMediaRequestDialect.BSL:
            return bsl()
        if self is CaptionMediaRequestDialect.ASL:
            return asl()
