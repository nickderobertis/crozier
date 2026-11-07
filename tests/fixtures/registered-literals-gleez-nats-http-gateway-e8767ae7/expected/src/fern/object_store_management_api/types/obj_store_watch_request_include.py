

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ObjStoreWatchRequestInclude(enum.StrEnum):
    LAST_VALUE = "lastValue"
    ALL_HISTORY = "allHistory"
    UPDATES_ONLY = "updatesOnly"

    def visit(
        self,
        last_value: typing.Callable[[], T_Result],
        all_history: typing.Callable[[], T_Result],
        updates_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObjStoreWatchRequestInclude.LAST_VALUE:
            return last_value()
        if self is ObjStoreWatchRequestInclude.ALL_HISTORY:
            return all_history()
        if self is ObjStoreWatchRequestInclude.UPDATES_ONLY:
            return updates_only()
