

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ListEntitlementsResponseOutputEntitlementsItemFeatureType(enum.StrEnum):
    BOOLEAN = "boolean"
    NUMERIC = "numeric"
    SET = "set"

    def visit(
        self,
        boolean: typing.Callable[[], T_Result],
        numeric: typing.Callable[[], T_Result],
        set_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureType.BOOLEAN:
            return boolean()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureType.NUMERIC:
            return numeric()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureType.SET:
            return set_()
