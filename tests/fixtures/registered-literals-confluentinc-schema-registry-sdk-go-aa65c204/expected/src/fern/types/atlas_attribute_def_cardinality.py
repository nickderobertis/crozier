

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AtlasAttributeDefCardinality(enum.StrEnum):
    SINGLE = "SINGLE"
    LIST = "LIST"
    SET = "SET"

    def visit(
        self,
        single: typing.Callable[[], T_Result],
        list_: typing.Callable[[], T_Result],
        set_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AtlasAttributeDefCardinality.SINGLE:
            return single()
        if self is AtlasAttributeDefCardinality.LIST:
            return list_()
        if self is AtlasAttributeDefCardinality.SET:
            return set_()
