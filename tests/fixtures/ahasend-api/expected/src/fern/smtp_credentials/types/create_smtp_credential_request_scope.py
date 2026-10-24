

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSmtpCredentialRequestScope(enum.StrEnum):
    """
    Credential scope - "global" or "scoped"
    """

    GLOBAL = "global"
    SCOPED = "scoped"

    def visit(self, global_: typing.Callable[[], T_Result], scoped: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSmtpCredentialRequestScope.GLOBAL:
            return global_()
        if self is CreateSmtpCredentialRequestScope.SCOPED:
            return scoped()
