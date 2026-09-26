

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveCredentialsResponseTensorlakeSource(enum.StrEnum):
    MANAGED = "managed"
    CONNECTION = "connection"

    def visit(self, managed: typing.Callable[[], T_Result], connection: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeResolveCredentialsResponseTensorlakeSource.MANAGED:
            return managed()
        if self is PostInternalSandboxRuntimeResolveCredentialsResponseTensorlakeSource.CONNECTION:
            return connection()
