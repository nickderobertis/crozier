

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileUploadCompleteState(enum.StrEnum):
    OK = "ok"
    NOK = "nok"

    def visit(self, ok: typing.Callable[[], T_Result], nok: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileUploadCompleteState.OK:
            return ok()
        if self is FileUploadCompleteState.NOK:
            return nok()
