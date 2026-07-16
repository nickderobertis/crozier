

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MailerSendgridExporterConfigType(str, enum.Enum):
    """
    Type of mailer
    """

    SENDGRID = "sendgrid"

    def visit(self, sendgrid: typing.Callable[[], T_Result]) -> T_Result:
        if self is MailerSendgridExporterConfigType.SENDGRID:
            return sendgrid()
