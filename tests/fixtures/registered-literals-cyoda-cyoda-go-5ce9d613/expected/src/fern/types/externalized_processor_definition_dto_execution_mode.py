

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExternalizedProcessorDefinitionDtoExecutionMode(enum.StrEnum):
    SYNC = "SYNC"
    ASYNC_SAME_TX = "ASYNC_SAME_TX"
    ASYNC_NEW_TX = "ASYNC_NEW_TX"

    def visit(
        self,
        sync: typing.Callable[[], T_Result],
        async_same_tx: typing.Callable[[], T_Result],
        async_new_tx: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExternalizedProcessorDefinitionDtoExecutionMode.SYNC:
            return sync()
        if self is ExternalizedProcessorDefinitionDtoExecutionMode.ASYNC_SAME_TX:
            return async_same_tx()
        if self is ExternalizedProcessorDefinitionDtoExecutionMode.ASYNC_NEW_TX:
            return async_new_tx()
