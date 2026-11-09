

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertDataItemAlertSource(enum.StrEnum):
    """
    The source of the alert
    """

    APP = "app"
    DEVICE = "device"

    def visit(self, app: typing.Callable[[], T_Result], device: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertDataItemAlertSource.APP:
            return app()
        if self is AlertDataItemAlertSource.DEVICE:
            return device()
