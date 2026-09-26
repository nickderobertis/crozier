

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperationOperationKind(enum.StrEnum):
    START = "start"
    RESUME = "resume"

    def visit(self, start: typing.Callable[[], T_Result], resume: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperationOperationKind.START:
            return start()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperationOperationKind.RESUME:
            return resume()
