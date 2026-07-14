

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NotificationType(str, enum.Enum):
    SLACK = "slack"
    CUSTOMERIO = "customerio"

    def visit(self, slack: typing.Callable[[], T_Result], customerio: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotificationType.SLACK:
            return slack()
        if self is NotificationType.CUSTOMERIO:
            return customerio()
