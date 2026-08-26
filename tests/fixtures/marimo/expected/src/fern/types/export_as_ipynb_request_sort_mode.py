

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExportAsIpynbRequestSortMode(enum.StrEnum):
    TOP_DOWN = "top-down"
    TOPOLOGICAL = "topological"

    def visit(self, top_down: typing.Callable[[], T_Result], topological: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExportAsIpynbRequestSortMode.TOP_DOWN:
            return top_down()
        if self is ExportAsIpynbRequestSortMode.TOPOLOGICAL:
            return topological()
