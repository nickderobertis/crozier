

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeStartProfileInstanceResponseStatus(enum.StrEnum):
    ACCEPTED = "accepted"

    def visit(self, accepted: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeStartProfileInstanceResponseStatus.ACCEPTED:
            return accepted()
