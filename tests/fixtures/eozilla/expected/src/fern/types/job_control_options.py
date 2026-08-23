

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobControlOptions(enum.StrEnum):
    SYNC_EXECUTE = "sync-execute"
    ASYNC_EXECUTE = "async-execute"
    DISMISS = "dismiss"

    def visit(
        self,
        sync_execute: typing.Callable[[], T_Result],
        async_execute: typing.Callable[[], T_Result],
        dismiss: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobControlOptions.SYNC_EXECUTE:
            return sync_execute()
        if self is JobControlOptions.ASYNC_EXECUTE:
            return async_execute()
        if self is JobControlOptions.DISMISS:
            return dismiss()
