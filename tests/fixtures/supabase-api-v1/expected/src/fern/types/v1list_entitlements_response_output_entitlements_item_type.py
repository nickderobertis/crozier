

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ListEntitlementsResponseOutputEntitlementsItemType(enum.StrEnum):
    BOOLEAN = "boolean"
    NUMERIC = "numeric"
    SET = "set"

    def visit(
        self,
        boolean: typing.Callable[[], T_Result],
        numeric: typing.Callable[[], T_Result],
        set_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ListEntitlementsResponseOutputEntitlementsItemType.BOOLEAN:
            return boolean()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemType.NUMERIC:
            return numeric()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemType.SET:
            return set_()
