

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Status(str, enum.Enum):
    """
    The status of the webhook.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is Status.ENABLED:
            return enabled()
        if self is Status.DISABLED:
            return disabled()
