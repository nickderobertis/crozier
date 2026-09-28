

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OperationMetadataState(enum.StrEnum):
    """
    Current state of the batch operation.
    """

    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"

    def visit(
        self,
        state_unspecified: typing.Callable[[], T_Result],
        created: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OperationMetadataState.STATE_UNSPECIFIED:
            return state_unspecified()
        if self is OperationMetadataState.CREATED:
            return created()
        if self is OperationMetadataState.RUNNING:
            return running()
        if self is OperationMetadataState.DONE:
            return done()
        if self is OperationMetadataState.CANCELLED:
            return cancelled()
