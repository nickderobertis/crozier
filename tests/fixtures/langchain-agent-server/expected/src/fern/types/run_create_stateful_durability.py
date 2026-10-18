

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateStatefulDurability(enum.StrEnum):
    """
    Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.
    """

    SYNC = "sync"
    ASYNC = "async"
    EXIT = "exit"

    def visit(
        self,
        sync: typing.Callable[[], T_Result],
        async_: typing.Callable[[], T_Result],
        exit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunCreateStatefulDurability.SYNC:
            return sync()
        if self is RunCreateStatefulDurability.ASYNC:
            return async_()
        if self is RunCreateStatefulDurability.EXIT:
            return exit()
