

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes2(enum.StrEnum):
    ENRICHER = "Enricher"

    def visit(self, enricher: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes2.ENRICHER:
            return enricher()
