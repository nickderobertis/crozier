

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TxIsolation(enum.StrEnum):
    READ_COMMITTED = "read-committed"
    REPEATABLE_READ = "repeatable-read"
    SERIALIZABLE = "serializable"

    def visit(
        self,
        read_committed: typing.Callable[[], T_Result],
        repeatable_read: typing.Callable[[], T_Result],
        serializable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TxIsolation.READ_COMMITTED:
            return read_committed()
        if self is TxIsolation.REPEATABLE_READ:
            return repeatable_read()
        if self is TxIsolation.SERIALIZABLE:
            return serializable()
