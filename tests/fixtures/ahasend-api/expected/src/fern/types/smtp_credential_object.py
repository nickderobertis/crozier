

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SmtpCredentialObject(enum.StrEnum):
    """
    Object type identifier
    """

    CREDENTIAL_SMTP = "credential_smtp"

    def visit(self, credential_smtp: typing.Callable[[], T_Result]) -> T_Result:
        if self is SmtpCredentialObject.CREDENTIAL_SMTP:
            return credential_smtp()
