

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveCredentialsResponseDockerSource(enum.StrEnum):
    MANAGED = "managed"

    def visit(self, managed: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeResolveCredentialsResponseDockerSource.MANAGED:
            return managed()
