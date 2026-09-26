

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveCredentialsResponseE2BSource(enum.StrEnum):
    MANAGED = "managed"
    CONNECTION = "connection"

    def visit(self, managed: typing.Callable[[], T_Result], connection: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeResolveCredentialsResponseE2BSource.MANAGED:
            return managed()
        if self is PostInternalSandboxRuntimeResolveCredentialsResponseE2BSource.CONNECTION:
            return connection()
