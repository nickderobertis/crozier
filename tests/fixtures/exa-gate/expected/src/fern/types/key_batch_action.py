

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KeyBatchAction(enum.StrEnum):
    DISABLE = "disable"
    ENABLE = "enable"
    RESET = "reset"
    TEST = "test"

    def visit(
        self,
        disable: typing.Callable[[], T_Result],
        enable: typing.Callable[[], T_Result],
        reset: typing.Callable[[], T_Result],
        test: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KeyBatchAction.DISABLE:
            return disable()
        if self is KeyBatchAction.ENABLE:
            return enable()
        if self is KeyBatchAction.RESET:
            return reset()
        if self is KeyBatchAction.TEST:
            return test()
