

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileProcessingStatus(enum.StrEnum):
    PENDING = "pending"
    PARSING = "parsing"
    EMBEDDING = "embedding"
    COMPLETED = "completed"
    ERROR = "error"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        parsing: typing.Callable[[], T_Result],
        embedding: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileProcessingStatus.PENDING:
            return pending()
        if self is FileProcessingStatus.PARSING:
            return parsing()
        if self is FileProcessingStatus.EMBEDDING:
            return embedding()
        if self is FileProcessingStatus.COMPLETED:
            return completed()
        if self is FileProcessingStatus.ERROR:
            return error()
