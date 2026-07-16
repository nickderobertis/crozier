

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MailerMailjetExporterConfigType(enum.StrEnum):
    """
    Type of mailer
    """

    MAILJET = "mailjet"

    def visit(self, mailjet: typing.Callable[[], T_Result]) -> T_Result:
        if self is MailerMailjetExporterConfigType.MAILJET:
            return mailjet()
