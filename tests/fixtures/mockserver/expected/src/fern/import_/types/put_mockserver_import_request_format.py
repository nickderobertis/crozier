

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverImportRequestFormat(enum.StrEnum):
    HAR = "har"
    POSTMAN = "postman"
    RECORDING = "recording"

    def visit(
        self,
        har: typing.Callable[[], T_Result],
        postman: typing.Callable[[], T_Result],
        recording: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutMockserverImportRequestFormat.HAR:
            return har()
        if self is PutMockserverImportRequestFormat.POSTMAN:
            return postman()
        if self is PutMockserverImportRequestFormat.RECORDING:
            return recording()
