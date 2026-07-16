

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MailerMailgunExporterConfigType(str, enum.Enum):
    """
    Type of mailer
    """

    MAILGUN = "mailgun"

    def visit(self, mailgun: typing.Callable[[], T_Result]) -> T_Result:
        if self is MailerMailgunExporterConfigType.MAILGUN:
            return mailgun()
