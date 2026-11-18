

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsCodeZoneVariantType(enum.StrEnum):
    COMMON = "COMMON"
    CUSTOMIZED = "CUSTOMIZED"

    def visit(self, common: typing.Callable[[], T_Result], customized: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsCodeZoneVariantType.COMMON:
            return common()
        if self is SimpleDataModelsCodeZoneVariantType.CUSTOMIZED:
            return customized()
