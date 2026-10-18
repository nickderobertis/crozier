

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRunStatusResponseOutputMessage(enum.StrEnum):
    OK = "ok"

    def visit(self, ok: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateRunStatusResponseOutputMessage.OK:
            return ok()
