

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveCredentialsResponseModalSource(enum.StrEnum):
    MANAGED = "managed"
    CONNECTION = "connection"

    def visit(self, managed: typing.Callable[[], T_Result], connection: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeResolveCredentialsResponseModalSource.MANAGED:
            return managed()
        if self is PostInternalSandboxRuntimeResolveCredentialsResponseModalSource.CONNECTION:
            return connection()
