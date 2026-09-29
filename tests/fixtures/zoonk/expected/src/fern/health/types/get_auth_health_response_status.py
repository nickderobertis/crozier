

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthHealthResponseStatus(enum.StrEnum):
    OK = "ok"

    def visit(self, ok: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAuthHealthResponseStatus.OK:
            return ok()
