

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MailerGenericExporterConfigType(str, enum.Enum):
    """
    Type of mailer
    """

    GENERIC = "generic"

    def visit(self, generic: typing.Callable[[], T_Result]) -> T_Result:
        if self is MailerGenericExporterConfigType.GENERIC:
            return generic()
