

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SmtpCredentialScope(enum.StrEnum):
    """
    Credential scope
    """

    GLOBAL = "global"
    SCOPED = "scoped"

    def visit(self, global_: typing.Callable[[], T_Result], scoped: typing.Callable[[], T_Result]) -> T_Result:
        if self is SmtpCredentialScope.GLOBAL:
            return global_()
        if self is SmtpCredentialScope.SCOPED:
            return scoped()
