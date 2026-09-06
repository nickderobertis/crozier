

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BatchedFacetDataType(enum.StrEnum):
    BATCHED_FACET = "batched_facet"

    def visit(self, batched_facet: typing.Callable[[], T_Result]) -> T_Result:
        if self is BatchedFacetDataType.BATCHED_FACET:
            return batched_facet()
