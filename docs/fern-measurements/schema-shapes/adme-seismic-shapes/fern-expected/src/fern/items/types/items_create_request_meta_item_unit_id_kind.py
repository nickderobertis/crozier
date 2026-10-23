

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ItemsCreateRequestMetaItemUnitIdKind(enum.StrEnum):
    UNIT = "Unit"

    def visit(self, unit: typing.Callable[[], T_Result]) -> T_Result:
        if self is ItemsCreateRequestMetaItemUnitIdKind.UNIT:
            return unit()
