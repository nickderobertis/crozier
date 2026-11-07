

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class KvStoreWatchRequestInclude(enum.StrEnum):
    LAST_VALUE = "lastValue"
    ALL_HISTORY = "allHistory"
    UPDATES_ONLY = "updatesOnly"

    def visit(
        self,
        last_value: typing.Callable[[], T_Result],
        all_history: typing.Callable[[], T_Result],
        updates_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KvStoreWatchRequestInclude.LAST_VALUE:
            return last_value()
        if self is KvStoreWatchRequestInclude.ALL_HISTORY:
            return all_history()
        if self is KvStoreWatchRequestInclude.UPDATES_ONLY:
            return updates_only()
