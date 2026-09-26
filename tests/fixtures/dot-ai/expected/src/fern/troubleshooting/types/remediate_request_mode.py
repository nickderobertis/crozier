

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RemediateRequestMode(enum.StrEnum):
    """
    Execution mode: manual requires user approval, automatic executes based on thresholds
    """

    MANUAL = "manual"
    AUTOMATIC = "automatic"

    def visit(self, manual: typing.Callable[[], T_Result], automatic: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemediateRequestMode.MANUAL:
            return manual()
        if self is RemediateRequestMode.AUTOMATIC:
            return automatic()
