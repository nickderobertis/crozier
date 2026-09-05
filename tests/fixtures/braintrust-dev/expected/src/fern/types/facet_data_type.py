

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FacetDataType(enum.StrEnum):
    FACET = "facet"

    def visit(self, facet: typing.Callable[[], T_Result]) -> T_Result:
        if self is FacetDataType.FACET:
            return facet()
