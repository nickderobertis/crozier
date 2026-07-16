

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MailerMailjetExporterConfigType(str, enum.Enum):
    """
    Type of mailer
    """

    MAILJET = "mailjet"

    def visit(self, mailjet: typing.Callable[[], T_Result]) -> T_Result:
        if self is MailerMailjetExporterConfigType.MAILJET:
            return mailjet()
