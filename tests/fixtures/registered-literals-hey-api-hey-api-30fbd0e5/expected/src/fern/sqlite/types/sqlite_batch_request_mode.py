

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SqliteBatchRequestMode(enum.StrEnum):
    WRITE = "write"
    READ = "read"
    DEFERRED = "deferred"

    def visit(
        self,
        write: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        deferred: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SqliteBatchRequestMode.WRITE:
            return write()
        if self is SqliteBatchRequestMode.READ:
            return read()
        if self is SqliteBatchRequestMode.DEFERRED:
            return deferred()
