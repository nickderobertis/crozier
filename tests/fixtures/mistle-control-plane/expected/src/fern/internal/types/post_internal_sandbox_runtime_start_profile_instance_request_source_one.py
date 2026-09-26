

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeStartProfileInstanceRequestSourceOne(enum.StrEnum):
    WEBHOOK = "webhook"

    def visit(self, webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeStartProfileInstanceRequestSourceOne.WEBHOOK:
            return webhook()
