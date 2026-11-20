

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UasZoneVersionVariant(enum.StrEnum):
    COMMON = "COMMON"
    CUSTOMIZED = "CUSTOMIZED"

    def visit(self, common: typing.Callable[[], T_Result], customized: typing.Callable[[], T_Result]) -> T_Result:
        if self is UasZoneVersionVariant.COMMON:
            return common()
        if self is UasZoneVersionVariant.CUSTOMIZED:
            return customized()
