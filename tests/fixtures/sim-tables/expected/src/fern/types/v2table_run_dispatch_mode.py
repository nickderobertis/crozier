

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableRunDispatchMode(enum.StrEnum):
    """
    Which cells the dispatch targets: `all` re-runs settled cells, `incomplete` skips them, `new` covers only cells that have never run.
    """

    ALL = "all"
    INCOMPLETE = "incomplete"
    NEW = "new"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
        new: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2TableRunDispatchMode.ALL:
            return all_()
        if self is V2TableRunDispatchMode.INCOMPLETE:
            return incomplete()
        if self is V2TableRunDispatchMode.NEW:
            return new()
