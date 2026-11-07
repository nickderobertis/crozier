

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompactResourceObject(enum.StrEnum):
    """
    The object type. Always `response.compaction`.
    """

    RESPONSE_COMPACTION = "response.compaction"

    def visit(self, response_compaction: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompactResourceObject.RESPONSE_COMPACTION:
            return response_compaction()
