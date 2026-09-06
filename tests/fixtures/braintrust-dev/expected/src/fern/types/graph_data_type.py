

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GraphDataType(enum.StrEnum):
    GRAPH = "graph"

    def visit(self, graph: typing.Callable[[], T_Result]) -> T_Result:
        if self is GraphDataType.GRAPH:
            return graph()
