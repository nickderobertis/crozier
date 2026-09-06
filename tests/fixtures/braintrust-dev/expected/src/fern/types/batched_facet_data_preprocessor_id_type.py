

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BatchedFacetDataPreprocessorIdType(enum.StrEnum):
    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is BatchedFacetDataPreprocessorIdType.FUNCTION:
            return function()
