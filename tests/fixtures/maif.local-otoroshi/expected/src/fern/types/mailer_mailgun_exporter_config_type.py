

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MailerMailgunExporterConfigType(enum.StrEnum):
    """
    Type of mailer
    """

    MAILGUN = "mailgun"

    def visit(self, mailgun: typing.Callable[[], T_Result]) -> T_Result:
        if self is MailerMailgunExporterConfigType.MAILGUN:
            return mailgun()
