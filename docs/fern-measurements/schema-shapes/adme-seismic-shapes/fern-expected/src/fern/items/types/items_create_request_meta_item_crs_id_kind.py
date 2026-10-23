

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ItemsCreateRequestMetaItemCrsIdKind(enum.StrEnum):
    CRS = "Crs"

    def visit(self, crs: typing.Callable[[], T_Result]) -> T_Result:
        if self is ItemsCreateRequestMetaItemCrsIdKind.CRS:
            return crs()
